import itertools
import sys
import unidecode
from corpora.diacritization_stripping_data import strip_diacritization_uninames

NO_DIACRITICS_EXTENSION = "stripped"


def stripped_file_name(file):
    name_slices = file.split(".")
    name_slices.insert(-1, NO_DIACRITICS_EXTENSION)
    return ".".join(name_slices)


FILES_DEFAULT = ["/".join(triple) for triple in itertools.product(
    ["corpora"],
    ["ga", "cs", "es", "fr", "hr", "hu", "lv", "pl", "ro", "sk"],
    ["target_test.txt", "target_train.txt"]
)]  # lists file names "corpora/{ga,cs,es,...}/{target_test,target_train}.txt"

files = sys.argv[1:] if len(sys.argv) > 1 else FILES_DEFAULT
translation_table = str.maketrans(strip_diacritization_uninames)

for file in files:
    with open(file, 'r', encoding="utf8") as infile:
        print("Stripping file " + file)
        with open(stripped_file_name(file), 'w', encoding="utf8") as outfile:
            for line in infile:
                print(line.translate(translation_table), end="", file=outfile)
