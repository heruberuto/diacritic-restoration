# -*- coding: utf-8 -*-
"""accents.py

This module sets the basic constants and functions for proccessing diacritics, their separation and composition
with the characters. Handles transitions (char<=>tuple): diacritical character <=> (character, diac. mark)"""


def decompose(character):
    """
    Decomposes a single diacritical character to its non-diacritical version and the
    removed diacritical mark.

    :param character: the diacritical character to be stripped
    :type: chr
    :return: a couple: Character without diacritics, Diacritical mark
    :rtype: tuple
    """
    return CHARACTER_DECOMPOSITIONS.get(character, (character, NO_ACCENT))


def compose(character, accent=None):
    """
    Takes a couple of non-diacritical character and a diacritical mark
    (or a list of such a couples) and returns the matching single diacritical
    character (or a string).
    Lazy-loads the character_compositions global that makes this problem easy.

    :param character: the character to be composed with accent | list of chr,accent couples
    :type: chr|list
    :param accent: diacritical mark to be added to the character
    :return: the character with the desired diacritical mark | list of such
    :rtype: chr|str
    """
    if isinstance(character, list):
        return "".join([compose(char, accent) for char, accent in character])
    global character_compositions
    if character_compositions is None:
        character_compositions = {val: key for key, val in CHARACTER_DECOMPOSITIONS.items()}
    return character_compositions.get((character, accent), character)


def strip(string):
    """
    Strips given string of diacritics.
    :param string: string to be stripped of diacritical marks
    :type: str
    :return: the input string stripped of diacritical marks
    :rtype: str
    """
    global stripping_table
    if stripping_table is None:
        stripping_table = str.maketrans({key: val[0] for key, val in CHARACTER_DECOMPOSITIONS.items()})
    return string.translate(stripping_table)


def is_alphabetic(character):
    """
    Decides whether the character should be considered alphabetics (primarily for the use of alpha-word
    accuracy) i. e. whether the character is a upper- or lowercase letter of latin alphabet (other alphabets
    neglected)
    :param character:
    :type: chr
    :return: true iff the character is alphabetic
    """
    return ord('a') <= ord(character) <= ord('z') or ord('A') <= ord(character) <= ord('Z')


#  Diacritical mark constants:
NO_ACCENT = ' '  # A printable character is used (instead of None) to make the (de)serialization easy
ACUTE = '´'
GRAVE = '`'
CIRCUMFLEX = 'ˆ'
CARON = 'ˇ'
BREVE = '˘'
INVERTED_BREVE = '̑'
CEDILLA = '¸'
UMLAUT = '¨'
DOT = '·'
TILDE = '͂'
RING = '˚'
UNDER_RING = '˳'
STROKE = '-'
OGONEK = '˛'
MACRON = 'ˉ'
DOUBLE_ACUTE = '˝'
DOUBLE_GRAVE = '̏'
COMMA = ','

SUPPORTED = (NO_ACCENT, ACUTE, GRAVE, CIRCUMFLEX, BREVE, CEDILLA, UMLAUT, DOUBLE_GRAVE,
             TILDE, RING, STROKE, OGONEK, MACRON, DOUBLE_GRAVE, DOUBLE_ACUTE, COMMA)
stripping_table = None
character_compositions = None
CHARACTER_DECOMPOSITIONS = {
    # Only tested on the 10 languages subject to the semester project.
    # If You find any decomposition missing, please make a pull-request.
    'À': ('A', GRAVE),
    'Á': ('A', ACUTE),
    'Â': ('A', CIRCUMFLEX),
    'Ã': ('A', TILDE),
    'Ä': ('A', UMLAUT),
    'Å': ('A', RING),
    'Ç': ('C', CEDILLA),
    'È': ('E', GRAVE),
    'É': ('E', ACUTE),
    'Ê': ('E', CIRCUMFLEX),
    'Ë': ('E', UMLAUT),
    'Ì': ('I', GRAVE),
    'Í': ('I', ACUTE),
    'Î': ('I', CIRCUMFLEX),
    'Ï': ('I', UMLAUT),
    'Ñ': ('N', TILDE),
    'Ò': ('O', GRAVE),
    'Ó': ('O', ACUTE),
    'Ô': ('O', CIRCUMFLEX),
    'Õ': ('O', TILDE),
    'Ö': ('O', UMLAUT),
    'Ø': ('O', STROKE),
    'Ù': ('U', GRAVE),
    'Ú': ('U', ACUTE),
    'Û': ('U', CIRCUMFLEX),
    'Ü': ('U', UMLAUT),
    'Ý': ('Y', ACUTE),
    'à': ('a', GRAVE),
    'á': ('a', ACUTE),
    'â': ('a', CIRCUMFLEX),
    'ã': ('a', TILDE),
    'ä': ('a', UMLAUT),
    'å': ('a', RING),
    'ç': ('c', CEDILLA),
    'è': ('e', GRAVE),
    'é': ('e', ACUTE),
    'ê': ('e', CIRCUMFLEX),
    'ë': ('e', UMLAUT),
    'ì': ('i', GRAVE),
    'í': ('i', ACUTE),
    'î': ('i', CIRCUMFLEX),
    'ï': ('i', UMLAUT),
    'ñ': ('n', TILDE),
    'ò': ('o', GRAVE),
    'ó': ('o', ACUTE),
    'ô': ('o', CIRCUMFLEX),
    'õ': ('o', TILDE),
    'ö': ('o', UMLAUT),
    'ø': ('o', STROKE),
    'ù': ('u', GRAVE),
    'ú': ('u', ACUTE),
    'û': ('u', CIRCUMFLEX),
    'ü': ('u', UMLAUT),
    'ý': ('y', ACUTE),
    'ÿ': ('y', UMLAUT),
    'Ā': ('A', TILDE),
    'ā': ('a', TILDE),
    'Ă': ('A', BREVE),
    'ă': ('a', BREVE),
    'Ą': ('A', OGONEK),
    'ą': ('a', OGONEK),
    'Ć': ('C', ACUTE),
    'ć': ('c', ACUTE),
    'Ĉ': ('C', CIRCUMFLEX),
    'ĉ': ('c', CIRCUMFLEX),
    'Ċ': ('C', DOT),
    'ċ': ('c', DOT),
    'Č': ('C', CARON),
    'č': ('c', CARON),
    'Ď': ('D', CARON),
    'ď': ('d', CARON),
    'Đ': ('D', STROKE),
    'đ': ('d', STROKE),
    'Ē': ('E', MACRON),
    'ē': ('e', MACRON),
    'Ĕ': ('E', BREVE),
    'ĕ': ('e', BREVE),
    'Ė': ('E', DOT),
    'ė': ('e', DOT),
    'Ę': ('E', OGONEK),
    'ę': ('e', OGONEK),
    'Ě': ('E', CARON),
    'ě': ('e', CARON),
    'Ĝ': ('G', CIRCUMFLEX),
    'ĝ': ('g', CIRCUMFLEX),
    'Ğ': ('G', BREVE),
    'ğ': ('g', BREVE),
    'Ġ': ('G', DOT),
    'ġ': ('g', DOT),
    'Ģ': ('G', CEDILLA),
    'ģ': ('g', CEDILLA),
    'Ĥ': ('H', CIRCUMFLEX),
    'ĥ': ('h', CIRCUMFLEX),
    'Ħ': ('H', STROKE),
    'ħ': ('h', STROKE),
    'Ĩ': ('I', TILDE),
    'ĩ': ('i', TILDE),
    'Ī': ('I', MACRON),
    'ī': ('i', MACRON),
    'Ĭ': ('I', BREVE),
    'ĭ': ('i', BREVE),
    'Į': ('I', OGONEK),
    'į': ('i', OGONEK),
    'İ': ('I', DOT),
    'Ĵ': ('J', CIRCUMFLEX),
    'ĵ': ('j', CIRCUMFLEX),
    'Ķ': ('K', CEDILLA),
    'ķ': ('k', CEDILLA),
    'Ĺ': ('L', ACUTE),
    'ĺ': ('l', ACUTE),
    'Ļ': ('L', CEDILLA),
    'ļ': ('l', CEDILLA),
    'Ľ': ('L', CARON),
    'ľ': ('l', CARON),
    'Ŀ': ('L', DOT),
    'ŀ': ('l', DOT),
    'Ł': ('L', STROKE),
    'ł': ('l', STROKE),
    'Ń': ('N', ACUTE),
    'ń': ('n', ACUTE),
    'Ņ': ('N', CEDILLA),
    'ņ': ('n', CEDILLA),
    'Ň': ('N', CARON),
    'ň': ('n', CARON),
    'Ō': ('O', MACRON),
    'ō': ('o', MACRON),
    'Ŏ': ('O', BREVE),
    'ŏ': ('o', BREVE),
    'Ő': ('O', DOUBLE_ACUTE),
    'ő': ('o', DOUBLE_ACUTE),
    'Ŕ': ('R', ACUTE),
    'ŕ': ('r', ACUTE),
    'Ŗ': ('R', CEDILLA),
    'ŗ': ('r', CEDILLA),
    'Ř': ('R', CARON),
    'ř': ('r', CARON),
    'Ś': ('S', ACUTE),
    'ś': ('s', ACUTE),
    'Ŝ': ('S', CIRCUMFLEX),
    'ŝ': ('s', CIRCUMFLEX),
    'Ş': ('S', CEDILLA),
    'ş': ('s', CEDILLA),
    'Š': ('S', CARON),
    'š': ('s', CARON),
    'Ţ': ('T', CEDILLA),
    'ţ': ('t', CEDILLA),
    'Ť': ('T', CARON),
    'ť': ('t', CARON),
    'Ŧ': ('T', STROKE),
    'ŧ': ('t', STROKE),
    'Ũ': ('U', TILDE),
    'ũ': ('u', TILDE),
    'Ū': ('U', MACRON),
    'ū': ('u', MACRON),
    'Ŭ': ('U', BREVE),
    'ŭ': ('u', BREVE),
    'Ů': ('U', RING),
    'ů': ('u', RING),
    'Ű': ('U', DOUBLE_ACUTE),
    'ű': ('u', DOUBLE_ACUTE),
    'Ų': ('U', OGONEK),
    'ų': ('u', OGONEK),
    'Ŵ': ('W', CIRCUMFLEX),
    'ŵ': ('w', CIRCUMFLEX),
    'Ŷ': ('Y', CIRCUMFLEX),
    'ŷ': ('y', CIRCUMFLEX),
    'Ÿ': ('Y', UMLAUT),
    'Ź': ('Z', ACUTE),
    'ź': ('z', ACUTE),
    'Ż': ('Z', DOT),
    'ż': ('z', DOT),
    'Ž': ('Z', CARON),
    'ž': ('z', CARON),
    'ƀ': ('b', STROKE),
    'Ɨ': ('I', STROKE),
    'Ǎ': ('A', CARON),
    'ǎ': ('a', CARON),
    'Ǐ': ('I', CARON),
    'ǐ': ('i', CARON),
    'Ǒ': ('O', CARON),
    'ǒ': ('o', CARON),
    'Ǔ': ('U', CARON),
    'ǔ': ('u', CARON),
    'Ǣ': ('Æ', MACRON),
    'ǣ': ('æ', MACRON),
    'Ǥ': ('G', STROKE),
    'ǥ': ('g', STROKE),
    'Ǧ': ('G', CARON),
    'ǧ': ('g', CARON),
    'Ǩ': ('K', CARON),
    'ǩ': ('k', CARON),
    'Ǫ': ('O', OGONEK),
    'ǫ': ('o', OGONEK),
    'ǰ': ('j', CARON),
    'Ǵ': ('G', ACUTE),
    'ǵ': ('g', ACUTE),
    'Ǹ': ('N', ACUTE),
    'ǹ': ('n', ACUTE),
    'Ȁ': ('A', DOUBLE_GRAVE),
    'ȁ': ('a', DOUBLE_GRAVE),
    'Ȅ': ('E', DOUBLE_GRAVE),
    'ȅ': ('e', DOUBLE_GRAVE),
    'Ȉ': ('I', DOUBLE_GRAVE),
    'ȉ': ('i', DOUBLE_GRAVE),
    'Ȍ': ('O', DOUBLE_GRAVE),
    'ȍ': ('o', DOUBLE_GRAVE),
    'Ȑ': ('R', DOUBLE_GRAVE),
    'ȑ': ('r', DOUBLE_GRAVE),
    'Ȕ': ('U', DOUBLE_GRAVE),
    'ȕ': ('u', DOUBLE_GRAVE),
    'Ș': ('S', COMMA),
    'ș': ('s', COMMA),
    'Ț': ('T', COMMA),
    'ț': ('t', COMMA),
    'Ȟ': ('H', CARON),
    'ȟ': ('h', CARON),
    'Ȧ': ('A', DOT),
    'ȧ': ('a', DOT),
    'Ȩ': ('E', CEDILLA),
    'Ȯ': ('O', DOT),
    'ȯ': ('o', DOT),
    'Ȳ': ('Y', MACRON),
    'ȳ': ('y', MACRON),
    'Ⱥ': ('A', STROKE),
    'Ȼ': ('C', STROKE),
    'ȼ': ('c', STROKE),
    'Ⱦ': ('T', STROKE),
    'Ƀ': ('B', STROKE)
}
