# -*- coding: utf-8 -*-
"""pretrain.py

This is an ad-hoc bulk trainer of HmmNgramRestorer diacritics restorers trained over
corpora/{language_code}/target_train.detok.txt corpora using {1,...,6}-gram models.

Once ran, this file will start training such a restorers (taggers) and saving them on the path:
pretrained/{language_code}/{1,..,6}-gram.pickle
It will also notify reaching a milestone once every 10000 training sentences."""

from diacritics_restorer import HmmNgramRestorer

DIR = "pretrained"
TRAINING_FILE = "target_train.detok.txt"
for language in ["hr", "cs", "sk", "ga", "hu", "pl", "ro", "fr", "es", "lv", ]:
    for n in range(1, 7):
        print("Training {}-gram model for language {}".format(n, language))
        HmmNgramRestorer(n) \
            .train("/".join(["corpora", language, TRAINING_FILE])) \
            .save("/".join(["pretrained", language, str(n) + "-gram.pickle"]))
