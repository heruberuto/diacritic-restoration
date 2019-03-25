import json

from diacritic_restorer import HmmNgramRestorer

DIR = "pretrained"
TRAINING_FILE = "target_test.detok.txt"
for language in ["es", "hu", "hr", "lv", "pl", "ro"]:
    for n in [1, 2, 3, 4]:
        print("Testing {}-gram model for language {}".format(n, language))
        accuracy = HmmNgramRestorer.load("/".join(["pretrained", language, str(n) + "-gram.pickle"])) \
            .test("/".join(["corpora", language, TRAINING_FILE]))
        print("Result: {}".format(json.dumps(accuracy)))
