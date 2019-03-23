def decompose(character):
    return CHARACTER_DECOMPOSITIONS.get(character, (character, NO_ACCENT))


def compose(character, accent):
    global CHARACTER_COMPOSITIONS
    if CHARACTER_COMPOSITIONS is None:
        CHARACTER_COMPOSITIONS = {val: key for key, val in CHARACTER_DECOMPOSITIONS.items()}
    return CHARACTER_COMPOSITIONS.get((character, accent), character)


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

SUPPORTED = [ACUTE, GRAVE, CIRCUMFLEX, BREVE, CEDILLA, UMLAUT, DOUBLE_GRAVE,
             TILDE, RING, UNDER_RING, STROKE, OGONEK, MACRON, DOUBLE_GRAVE, DOUBLE_ACUTE, COMMA]

CHARACTER_COMPOSITIONS = None
CHARACTER_DECOMPOSITIONS = {
    # The character decomposition was written ad hoc and only tested on czech and french
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