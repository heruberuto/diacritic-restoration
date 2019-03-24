import json
import pickle
import time

import numpy
from nltk.probability import MLEProbDist, DictionaryConditionalProbDist
from nltk.tag import hmm
from nltk.tag.hmm import HiddenMarkovModelTagger

import accents


class DiacriticRestorer:
    def train(self, file):
        return self

    def test(self, file):
        return 0

    def restore_accents(self, sentence):
        return


class HmmNgramRestorer(DiacriticRestorer):
    def __init__(self, n):
        self.tagger = None
        self.n = n

    def test(self, file, limit=None):
        buffer = CorpusNGramBuffer(file, self.n, 1000)
        right = wrong = words_right = words_wrong = diawords_right = diawords_wrong = 0
        word_right = True
        word_has_diacritics = False
        s = 0

        for sequence in buffer:
            if limit is not None and s >= limit: break
            else: s += 1
            tagged_sequence = self.tagger.tag([obs for obs, tag in sequence])
            for i in range(len(sequence)):
                if sequence[i][0][-1] == " " or i == len(sequence) - 1:
                    if word_right:
                        words_right += 1
                        if word_has_diacritics: diawords_right += 1
                    else:
                        words_wrong += 1
                        if word_has_diacritics: diawords_wrong += 1
                    word_right = True
                    word_has_diacritics = False
                elif sequence[i][1] != accents.NO_ACCENT:
                    word_has_diacritics = True
                if sequence[i][1] == tagged_sequence[i][1]:
                    right += 1
                else:
                    wrong += 1
                    word_right = False
        buffer.close()
        return {
            "accuracy": right / (right + wrong),
            "correct": right,
            "incorrect": wrong,
            "word_accuracy": words_right / (words_right + words_wrong),
            "words_correct": words_right,
            "words_incorrect": words_wrong,
            "diaword_accuracy": diawords_right / (diawords_right + diawords_wrong),
            "diawords_correct": diawords_right,
            "diawords_incorrect": diawords_wrong
        }

    def train(self, file):
        buffer = CorpusNGramBuffer(file, self.n)
        self.tagger = hmm.HiddenMarkovModelTrainer().train_supervised(buffer)
        buffer.close()
        sq("training done: ")
        return self

    def restore_accents(self, sentence):
        observations = []
        for i in range(1, len(sentence) + 1):
            observations.append(sentence[max(0, i - self.n):i])
        tagged_sequence = self.tagger.tag(observations)
        return "".join([accents.compose(observation[-1], accent) for observation, accent in tagged_sequence])

    def save(self, filename):
        with open(filename, 'wb') as file:
            dump = {
                "n": self.n,
                "tagger": {
                    "_symbols": self.tagger._symbols,
                    "_states": self.tagger._states,
                    "_transitions": self.tagger._transitions,
                    "_outputs": self.tagger._outputs,
                    "_priors": self.tagger._priors,
                }
            }
            for conditional in ["_transitions", "_outputs"]:
                probdist_dict = {}
                for key, val in dump["tagger"][conditional].items():
                    if isinstance(val, MLEProbDist):
                        probdist_dict[key] = val
                dump["tagger"][conditional] = DictionaryConditionalProbDist(probdist_dict)
            pickle.dump(dump, file)

    @classmethod
    def load(cls, filename):
        with open(filename, 'rb') as file:
            dump = pickle.load(file)
            hmm = cls(dump["n"])
            dump = dump["tagger"]
            hmm.tagger = HiddenMarkovModelTagger(dump["_symbols"], dump["_states"], dump["_transitions"],
                                                 dump["_outputs"], dump["_priors"])
        return hmm


class CorpusNGramBuffer:
    def __init__(self, filename, n, notify_after=10000):
        self.filename = filename
        self.file = open(filename, "r", encoding="utf8")
        self.n = n
        self.i = 0
        self.notify_after = notify_after

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if line == "":
            raise StopIteration
        line = line.rstrip()
        if self.i % self.notify_after == 0:
            print("BUFFERED line #{} of {} - \"{}\"".format(self.i, self.filename, line))
        self.i += 1
        buffer = []
        tagged_sequence = []
        for character in [accents.decompose(char) for char in line]:
            buffer.append(character[0])
            tagged_sequence.append(("".join(buffer), character[1]))
            if len(buffer) == self.n:
                buffer.pop(0)
        return tagged_sequence

    def close(self):
        self.file.close()


def sq(comment):
    global start
    print(comment + str(time.time() - start))
    start = time.time()


start = time.time()
