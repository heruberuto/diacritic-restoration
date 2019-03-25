# -*- coding: utf-8 -*-
"""evaluate.py

This is a simple ad-hoc bulk evaluator of the pre trained corpora matching the path:
pretrained/{language_code}/{1,..,4}-gram.pickle

Once ran, this file will start printing the Json-encoded resulting counters after concluded
experiments to the STDOUT. It will also notify reaching a milestone once per 1000 test sentences."""

import json

from diacritics_restorer import HmmNgramRestorer

DIR = "pretrained"
TRAINING_FILE = "target_test.detok.txt"
for language in ["hr", "cs", "sk", "ga", "hu", "pl", "ro", "fr", "es", "lv", ]:
    for n in [1, 2, 3, 4]:
        print("Testing {}-gram model for language {}".format(n, language))
        # load the Diacritics restorer from file and feed it the test sentences
        accuracy_counter = HmmNgramRestorer.load("/".join(["pretrained", language, str(n) + "-gram.pickle"])) \
            .test("/".join(["corpora", language, TRAINING_FILE]), 1000)
        print("Result: {}".format(json.dumps(accuracy_counter.as_dict())))
