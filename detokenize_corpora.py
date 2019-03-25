# -*- coding: utf-8 -*-
"""detokenize_corpora.py

This is a simple ad-hoc bulk detokenizer used for preparing the corpora from internet
for the character-based n-gram methods."""

import itertools
import sys
from nltk.tokenize.treebank import TreebankWordDetokenizer
from corpora.diacritization_stripping_data import strip_diacritization_uninames

OUTPUT_SUFFIX = "detok"


def detokenized_file_name(filename):
    """
    Augments the given filename by a constant suffix (OUTPUT_SUFFIX above)
    :param filename: original filename
    :type filename: str
    :return: augmented filename
    :rtype: str
    """
    name_slices = filename.split(".")
    name_slices.insert(-1, OUTPUT_SUFFIX)
    return ".".join(name_slices)


FILES_DEFAULT = [
    # lists file names "corpora/{ga,cs,es,...}/{target_test,target_train}.txt"
    "/".join(triple) for triple in itertools.product(
        ["corpora"],
        ["ga", "cs", "es", "fr", "hr", "hu", "lv", "pl", "ro", "sk"],
        ["target_test.txt", "target_train.txt"]
    )]

files = sys.argv[1:] if len(sys.argv) > 1 else FILES_DEFAULT
translation_table = str.maketrans(strip_diacritization_uninames)
detokenizer = TreebankWordDetokenizer()

for file in files:
    #  Detokenize listed files using Moses' detokenizer
    with open(file, 'r', encoding="utf8") as infile:
        print("Detokenizing file " + file)
        with open(detokenized_file_name(file), 'w', encoding="utf8") as outfile:
            for line in infile:
                line = detokenizer.detokenize(line.split())
                print(line, file=outfile)
