__author__ = 'ssbushi'

# Import the toolkit and tags
import nltk
from nltk.corpus import treebank

# Train data - pretagged
training = []
with open("corpora/cs/target_train.txt", 'r', encoding="utf8") as tag:
    with open("corpora/cs/target_train.stripped.txt", "r", encoding="utf8") as observation:
        while True:
            tagline = tag.readline()
            obsline = observation.readline()
            if not tagline or not obsline:
                break
            tagline = tagline.split()
            obsline = obsline.split()

            if len(tagline) != len(obsline):
                print(tagline)
                print(obsline)
                continue
            training.append([(obsline[i], tagline[i]) for i in range(len(obsline))])

print(training[0])

# Import HMM module
from nltk.tag import hmm

# Setup a trainer with default(None) values
# And train with the data
trainer = hmm.HiddenMarkovModelTrainer()
tagger = trainer.train_supervised(training)

print(tagger)
# Prints the basic data about the tagger

print(tagger.tag("Today is a good day .".split()))

print(tagger.tag("Joe met Joanne in Delhi .".split()))

print(tagger.tag("Chicago is the birthplace of Ginny".split()))

"""
Output in order (Notice some tags are wrong :/):
[('Today', u'NN'), ('is', u'VBZ'), ('a', u'DT'), ('good', u'JJ'), ('day', u'NN'), ('.', u'.')]
[('Joe', u'NNP'), ('met', u'VBD'), ('Joanne', u'NNP'), ('in', u'IN'), ('Delhi', u'NNP'), ('.', u'NNP')]
[('Chicago', u'NNP'), ('is', u'VBZ'), ('the', u'DT'), ('birthplace', u'NNP'), ('of', u'NNP'), ('Ginny', u'NNP')]
"""
