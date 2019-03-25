# -*- coding: utf-8 -*-
"""diacritics_restorer.py

This module sets the basic classes and methods for the diacritics restoration using the methods outlined
in the project documentation (N-gram emitting HMM). That includes tagger, accuracy counter and a training/testing
set file buffer. To see how the diacritics are proccessed, see accents.py"""

import pickle
import time
import accents

from nltk.probability import MLEProbDist, DictionaryConditionalProbDist
from nltk.tag import hmm
from nltk.tag.hmm import HiddenMarkovModelTagger



class BaseDiacriticsRestorer:
    """Base class for the diacritic restoration models"""

    def train(self, file):
        """
        Trains the Diacritic Restorer on the training set from the given file.

        :param file: path to file with training set (sentences with diacritics, ideally detokenized)
        :type file: str
        :return: self for further use
        :rtype: BaseDiacriticsRestorer
        """
        return self

    def test(self, file):
        """
        Tests the accuracy of the restoration model and outputs a DiacriticsAccuracyCounter objects
        with updated significant scores

        :param file: path to file with testing set (sentences with diacritics, ideally detokenized)
        :type file: str
        :return: Counter object with the computed significant accuracy scores
        :rtype: DiacriticsAccuracyCounter
        """
        return None

    def restore_accents(self, sentence):
        """
        Given a sentence without diacritics, model tags it and composes the diacritical characters
        from the observations and the tags, thus returning the predicted diacritical string.
        :param sentence: non-diacritical sentence to be restored
        :type sentence: str
        :return: restored diacritical sentence
        :rtype: str
        """
        return

    def restore_diacritics(self, sentence):
        """
        Alias for self.restore_accents()
        :param sentence:
        :return:
        """
        return self.restore_accents(sentence)


class HmmNgramRestorer(BaseDiacriticsRestorer):
    """Class for training, testing and (de)serializing trained n-gram based
    HMM taggers of diacritics

    :param n: int the n-gram size
    :type n: int
    :param tagger: the NLTK HiddenMarkovModelTagger
    :type tagger: HiddenMarkovModelTagger"""

    def __init__(self, n):
        self.tagger = None
        self.n = n

    def test(self, file, limit=None):
        """
        Tests the accuracy of the restoration model and outputs a DiacriticsAccuracyCounter objects
        with updated significant scores

        :param file: path to file with testing set (sentences with diacritics, ideally detokenized)
        :type file: str
        :return: Counter object with the computed significant accuracy scores
        :rtype: DiacriticsAccuracyCounter
        """
        buffer = CorpusNgramBuffer(file, self.n, 1000)
        counter = DiacriticsAccuracyCounter()
        s = 0

        for expected_sequence in buffer:
            if limit is not None and s >= limit:
                break
            else:
                s += 1
            observed_sequence = self.tagger.tag([ngram for ngram, tag in expected_sequence])
            for i in range(len(expected_sequence)):
                counter.count(expected_sequence[i], observed_sequence[i])
            counter.break_word()
        buffer.close()
        return counter

    def train(self, file):
        """
        Trains the Diacritic Restorer on the training set from the given file using the HMM of n-grams.

        :param file: path to file with training set (sentences with diacritics, ideally detokenized)
        :type file: str
        :return: self for further use
        :rtype: BaseDiacriticsRestorer
        """
        buffer = CorpusNgramBuffer(file, self.n)
        self.tagger = hmm.HiddenMarkovModelTrainer().train_supervised(buffer)
        buffer.close()
        milestone("training done: ")
        return self

    def restore_accents(self, sentence):
        """
        Given a sentence without diacritics, model tags it and composes the diacritical characters
        from the observations and the tags, thus returning the predicted diacritical string using the HMM tagger.
        :param sentence: non-diacritical sentence to be restored
        :type sentence: str
        :return: restored diacritical sentence
        :rtype: str
        """
        observations = []
        for i in range(1, len(sentence) + 1):
            observations.append(sentence[max(0, i - self.n):i])
        tagged_sequence = self.tagger.tag(observations)
        return "".join([accents.compose(observation[-1], accent) for observation, accent in tagged_sequence])

    def save(self, filename):
        """
        Serializes this diacritics restorer using pickle and saves it to file on given path for later use.
        :param filename: save path
        :type filename: str
        :return: void
        """
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
        """
        Loads and deserializes the pickle file (Diacritics restorer) saved on given path
        :param filename: load path
        :return: The loaded diacritics restorer object
        :rtype: HmmNgramRestorer
        """
        with open(filename, 'rb') as file:
            dump = pickle.load(file)
            hmm = cls(dump["n"])
            dump = dump["tagger"]
            hmm.tagger = HiddenMarkovModelTagger(dump["_symbols"], dump["_states"], dump["_transitions"],
                                                 dump["_outputs"], dump["_priors"])
        return hmm


class CorpusNgramBuffer:
    """
    An iterable class that feeds the long corpus files to the nltk HMM trainer as ngram=>diacritical_mark couples
    :param filename: path to the buffered file
    :type filename: str
    :param file: internally used file object maintaining a pointer on the last read line
    :type file: TextIOWrapper
    :param n: size of n-grams to be buffered
    :type n: int
    :param current_line: the number of current line
    :type current_line: int
    :param notify_after: the number of lines read after which user wants to be notified (in our case,
        varies from the difficulty of task buffer is used for)
    :type notify_after: int
    """

    def __init__(self, filename, n, notify_after=10000):
        self.filename = filename
        self.file = open(filename, "r", encoding="utf8")
        self.n = n
        self.current_line = 0
        self.notify_after = notify_after

    def __iter__(self):
        return self

    def __next__(self):
        """
        Returns the ngram=>diacritical_mark couples parsed from the current line of the buffered file,
        :raise StopIteration: when the file is over.
        :return:
        """
        line = self.file.readline()
        if line == "":
            raise StopIteration
        line = line.rstrip()
        if self.current_line % self.notify_after == 0:
            print("BUFFERED line #{} of {} - \"{}\"".format(self.current_line, self.filename, line))
        self.current_line += 1
        buffer = []
        tagged_sequence = []
        for character in [accents.decompose(char) for char in line]:
            buffer.append(character[0])
            tagged_sequence.append(("".join(buffer), character[1]))
            if len(buffer) == self.n:
                buffer.pop(0)
        return tagged_sequence

    def close(self):
        """
        Closes the associated IO stream
        :return: void
        """
        self.file.close()


class DiacriticsAccuracyCounter:
    """
    A simple counter class collecting expected and observed obs=>tag couple in every step and
    measuring several accuracy scores, based on their comparisons.

    :param right: number of the correctly restored tags (diacritical marks)
    :type right: int
    :param wrong: number of the incorrectly restored tags (diacritical marks)
    :type wrong: int
    :param words_right: number of the correctly restored (entire) space-separated words
    :type words_right: int
    :param words_wrong: number of the incorrectly restored (entire) words
    :type words_wrong: int
    :param diawords_right:  number of the correctly restored words with at least one diacritical mark
    :type diawords_right: int
    :param diawords_wrong: number of the incorrectly restored words with at least one diacritical mark
    :type diawords_wrong: int
    :param alphawords_right: number of the correctly restored words with at least one alphabetical character
    :type alphawords_right: int
    :param alphawords_wrong: number of the incorrectly restored words with at least one alphabetical character
    :type alphawords_wrong: int
    :param word_dia: has the current word at least one diacritical mark?
    :type word_dia: bool
    :param word_alpha: has the current word at least one diacritical mark?
    :type word_alpha: bool
    :param word_right: was the current word restored correctly?
    :type word_right: bool
    """

    def __init__(self):
        self.right = self.wrong = self.words_right = self.words_wrong = 0
        self.diawords_right = self.diawords_wrong = self.alphawords_right = self.alphawords_wrong = 0
        self.word_right = True
        self.word_dia = self.word_alpha = False

    def break_word(self):
        """ Updates the word counters and resets the flags """
        if self.word_right:
            self.words_right += 1
            if self.word_dia: self.diawords_right += 1
            if self.word_alpha: self.alphawords_right += 1
        else:
            self.words_wrong += 1
            if self.word_dia: self.diawords_wrong += 1
            if self.word_alpha: self.alphawords_wrong += 1
        self.word_right = True
        self.word_dia = False
        self.word_alpha = False

    def count(self, expected, observed):
        """
        Updates the counter by a single observation of its result.
        :param expected: expected ngram => tag (dia mark) couple
        :type expected: tuple
        :param observed: observed ngram => tag (dia mark) couple
        :param observed: tuple
        :return:
        """
        expected_ngram, expected_tag = expected
        ngram, tag = observed

        if expected_ngram[-1] == " ":
            self.break_word()
        else:
            if expected_tag != accents.NO_ACCENT:
                self.word_dia = True
            if accents.is_alphabetic(expected_ngram[-1]):
                self.word_alpha = True
        if tag == expected_tag:
            self.right += 1
        else:
            self.wrong += 1
            self.word_right = False

    def as_dict(self):
        """
        Returns all the object attributes (+ computed accuracies) as a dictionary
        :rtype: dict
        """
        return {
            "accuracy": self.right / (self.right + self.wrong),
            "correct": self.right,
            "incorrect": self.wrong,
            "word_accuracy": self.words_right / (self.words_right + self.words_wrong),
            "words_correct": self.words_right,
            "words_incorrect": self.words_wrong,
            "diaword_accuracy": self.diawords_right / (self.diawords_right + self.diawords_wrong),
            "diawords_correct": self.diawords_right,
            "diawords_incorrect": self.diawords_wrong,
            "alphaword_accuracy": self.alphawords_right / (self.alphawords_right + self.alphawords_wrong),
            "alphawords_correct": self.alphawords_right,
            "alphawords_incorrect": self.alphawords_wrong,
        }


def milestone(comment):
    """
    Prints how much time passed since the last milestone in the program lifecycle.
    Used for debugging and estimating speeds
    :param comment: Comment to print with the time passed
    """
    global start
    print(comment + str(time.time() - start))
    start = time.time()


start = time.time()
