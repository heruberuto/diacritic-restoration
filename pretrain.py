from diacritic_restorer import HmmNgramRestorer

DIR = "pretrained"
TRAINING_FILE = "target_train.detok.txt"
for language in ["hu","hr","ro"]:
    for n in range(1,7):
        print("Training {}-gram model for language {}".format(n, language))
        HmmNgramRestorer(n) \
            .train("/".join(["corpora", language, TRAINING_FILE])) \
            .save("/".join(["pretrained", language, str(n) + "-gram.pickle"]))
