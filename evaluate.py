from diacritic_restorer import HmmNgramRestorer

DIR = "pretrained"
TRAINING_FILE = "target_test.detok.txt"
for language in ["ga"]:
    for n in [1, 2, 4, 6, 8, 16]:
        print("Testing {}-gram model for language {}".format(n, language))
        accuracy = HmmNgramRestorer.load("/".join(["pretrained", language, str(n) + "-gram.pickle"])) \
            .test("/".join(["corpora", language, TRAINING_FILE]))
        print("Accuracy: {}".format(accuracy))
