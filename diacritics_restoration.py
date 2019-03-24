import json
import pickle
import time

import numpy
from nltk.probability import MLEProbDist, DictionaryConditionalProbDist
from nltk.tag import hmm
from nltk.tag.hmm import HiddenMarkovModelTagger

import accents


class DiacriticRestorer:
    def train(self, accented_text):
        return self

    def train_from_file(self, filename):
        return self.train(open(filename, 'r', encoding='utf8').readlines())

    def test_from_file(self, filename):
        return self.test(open(filename, 'r', encoding='utf8').readlines())

    def test(self, accented_sentences):
        sq("io2 done: ")
        correct = incorrect = 0
        for sentence in accented_sentences:
            result = self.restore_accents(accents.strip(sentence))
            for i in range(len(sentence)):
                if sentence[i] == result[i]:
                    correct += 1
                else:
                    incorrect += 1
        return correct / (correct + incorrect)

    def restore_accents(self, sentence):
        return


class HmmNgramRestorer(DiacriticRestorer):
    def __init__(self, n):
        self.tagger = None
        self.n = n

    def train(self, accented_sentences):
        training_data = []
        for sentence in accented_sentences:
            characters = [accents.decompose(character) for character in sentence]
            buffer = []
            training_sentence = []
            for character in characters:
                buffer.append(character[0])
                training_sentence.append(("".join(buffer), character[1]))
                if len(buffer) == self.n:
                    buffer.pop(0)
            training_data.append(training_sentence)
        sq("io1 done: ")
        self.tagger = hmm.HiddenMarkovModelTrainer().train_supervised(training_data)
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


start = time.time()


def sq(comment):
    global start
    print(comment + str(time.time() - start))
    start = time.time()



restorer = HmmNgramRestorer.load("ga.pickle")
restorer.restore_accents("is eard ata sa bhiobla focal de , de reir mar a mheasann na criostaithe agus na giudaigh .\n")
"""restorer2 = HmmNgramRestorer(4).train_from_file("corpora/ga/target_train.txt")
restorer2.save("ga.pickle")
print(restorer2.test_from_file("corpora/ga/target_test.txt"))
sq("finished: ")
"""
