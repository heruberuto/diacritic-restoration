from diacritic_restorer import HmmNgramRestorer

DIR = "pretrained"
TRAINING_FILE = "target_train.detok.txt"
for language in ["cs"]:
    for n in [ 8, ]:
        print("Training {}-gram model for language {}".format(n, language))
        HmmNgramRestorer(n) \
            .train("/".join(["corpora", language, TRAINING_FILE])) \
            .save("/".join(["pretrained", language, str(n) + "-gram.pickle"]))
