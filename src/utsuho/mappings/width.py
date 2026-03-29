"""
Width conversion mappings for deterministic Japanese text conversion.
"""

from .common import KanaLetterMapping, SimpleCharacterMap

# Base mappings for half-width to full-width conversion.
# Each value is (base, voiced, semi-voiced).
half_to_full_letter_map: dict[str, KanaLetterMapping] = {
    "\uff71": ("\u30a2", None, None),
    "\uff72": ("\u30a4", None, None),
    "\uff73": ("\u30a6", "\u30f4", None),
    "\uff74": ("\u30a8", None, None),
    "\uff75": ("\u30aa", None, None),
    "\uff76": ("\u30ab", "\u30ac", None),
    "\uff77": ("\u30ad", "\u30ae", None),
    "\uff78": ("\u30af", "\u30b0", None),
    "\uff79": ("\u30b1", "\u30b2", None),
    "\uff7a": ("\u30b3", "\u30b4", None),
    "\uff7b": ("\u30b5", "\u30b6", None),
    "\uff7c": ("\u30b7", "\u30b8", None),
    "\uff7d": ("\u30b9", "\u30ba", None),
    "\uff7e": ("\u30bb", "\u30bc", None),
    "\uff7f": ("\u30bd", "\u30be", None),
    "\uff80": ("\u30bf", "\u30c0", None),
    "\uff81": ("\u30c1", "\u30c2", None),
    "\uff82": ("\u30c4", "\u30c5", None),
    "\uff83": ("\u30c6", "\u30c7", None),
    "\uff84": ("\u30c8", "\u30c9", None),
    "\uff85": ("\u30ca", None, None),
    "\uff86": ("\u30cb", None, None),
    "\uff87": ("\u30cc", None, None),
    "\uff88": ("\u30cd", None, None),
    "\uff89": ("\u30ce", None, None),
    "\uff8a": ("\u30cf", "\u30d0", "\u30d1"),
    "\uff8b": ("\u30d2", "\u30d3", "\u30d4"),
    "\uff8c": ("\u30d5", "\u30d6", "\u30d7"),
    "\uff8d": ("\u30d8", "\u30d9", "\u30da"),
    "\uff8e": ("\u30db", "\u30dc", "\u30dd"),
    "\uff8f": ("\u30de", None, None),
    "\uff90": ("\u30df", None, None),
    "\uff91": ("\u30e0", None, None),
    "\uff92": ("\u30e1", None, None),
    "\uff93": ("\u30e2", None, None),
    "\uff94": ("\u30e4", None, None),
    "\uff95": ("\u30e6", None, None),
    "\uff96": ("\u30e8", None, None),
    "\uff97": ("\u30e9", None, None),
    "\uff98": ("\u30ea", None, None),
    "\uff99": ("\u30eb", None, None),
    "\uff9a": ("\u30ec", None, None),
    "\uff9b": ("\u30ed", None, None),
    "\uff9c": ("\u30ef", "\u30f7", None),
    "\uff66": ("\u30f2", "\u30fa", None),
    "\uff9d": ("\u30f3", None, None),
    "\uff6c": ("\u30e3", None, None),
    "\uff6d": ("\u30e5", None, None),
    "\uff6e": ("\u30e7", None, None),
    "\uff6f": ("\u30c3", None, None),
    "\uff67": ("\u30a1", None, None),
    "\uff68": ("\u30a3", None, None),
    "\uff69": ("\u30a5", None, None),
    "\uff6a": ("\u30a7", None, None),
    "\uff6b": ("\u30a9", None, None),
}

half_to_full_voicing_mark_map: SimpleCharacterMap = {
    "\uff9e": "\u309b",
    "\uff9f": "\u309c",
}

half_to_full_punctuation_map: SimpleCharacterMap = {
    "\uff64": "\u3001",
    "\uff61": "\u3002",
}

half_to_full_corner_bracket_map: SimpleCharacterMap = {
    "\uff62": "\u300c",
    "\uff63": "\u300d",
}

half_to_full_conjunction_mark_map: SimpleCharacterMap = {
    "\uff65": "\u30fb",
}

half_to_full_length_mark_map: SimpleCharacterMap = {
    "\uff70": "\u30fc",
}

half_to_full_space_map: SimpleCharacterMap = {
    "\u0020": "\u3000",
    "\u00a0": "\u3000",
}

half_to_full_ascii_symbol_map: SimpleCharacterMap = {
    "\u0021": "\uff01",
    "\u0022": "\uff02",
    "\u0023": "\uff03",
    "\u0024": "\uff04",
    "\u0025": "\uff05",
    "\u0026": "\uff06",
    "\u0027": "\uff07",
    "\u0028": "\uff08",
    "\u0029": "\uff09",
    "\u002a": "\uff0a",
    "\u002b": "\uff0b",
    "\u002c": "\uff0c",
    "\u002d": "\uff0d",
    "\u002e": "\uff0e",
    "\u002f": "\uff0f",
    "\u003a": "\uff1a",
    "\u003b": "\uff1b",
    "\u003c": "\uff1c",
    "\u003d": "\uff1d",
    "\u003e": "\uff1e",
    "\u003f": "\uff1f",
    "\u0040": "\uff20",
    "\u005b": "\uff3b",
    "\u005c": "\uff3c",
    "\u005d": "\uff3d",
    "\u005e": "\uff3e",
    "\u005f": "\uff3f",
    "\u0060": "\uff40",
    "\u007b": "\uff5b",
    "\u007c": "\uff5c",
    "\u007d": "\uff5d",
    "\u007e": "\uff5e",
}

half_to_full_ascii_digit_map: SimpleCharacterMap = {
    "\u0030": "\uff10",
    "\u0031": "\uff11",
    "\u0032": "\uff12",
    "\u0033": "\uff13",
    "\u0034": "\uff14",
    "\u0035": "\uff15",
    "\u0036": "\uff16",
    "\u0037": "\uff17",
    "\u0038": "\uff18",
    "\u0039": "\uff19",
}

half_to_full_ascii_alphabet_map: SimpleCharacterMap = {
    "\u0041": "\uff21",
    "\u0042": "\uff22",
    "\u0043": "\uff23",
    "\u0044": "\uff24",
    "\u0045": "\uff25",
    "\u0046": "\uff26",
    "\u0047": "\uff27",
    "\u0048": "\uff28",
    "\u0049": "\uff29",
    "\u004a": "\uff2a",
    "\u004b": "\uff2b",
    "\u004c": "\uff2c",
    "\u004d": "\uff2d",
    "\u004e": "\uff2e",
    "\u004f": "\uff2f",
    "\u0050": "\uff30",
    "\u0051": "\uff31",
    "\u0052": "\uff32",
    "\u0053": "\uff33",
    "\u0054": "\uff34",
    "\u0055": "\uff35",
    "\u0056": "\uff36",
    "\u0057": "\uff37",
    "\u0058": "\uff38",
    "\u0059": "\uff39",
    "\u005a": "\uff3a",
    "\u0061": "\uff41",
    "\u0062": "\uff42",
    "\u0063": "\uff43",
    "\u0064": "\uff44",
    "\u0065": "\uff45",
    "\u0066": "\uff46",
    "\u0067": "\uff47",
    "\u0068": "\uff48",
    "\u0069": "\uff49",
    "\u006a": "\uff4a",
    "\u006b": "\uff4b",
    "\u006c": "\uff4c",
    "\u006d": "\uff4d",
    "\u006e": "\uff4e",
    "\u006f": "\uff4f",
    "\u0070": "\uff50",
    "\u0071": "\uff51",
    "\u0072": "\uff52",
    "\u0073": "\uff53",
    "\u0074": "\uff54",
    "\u0075": "\uff55",
    "\u0076": "\uff56",
    "\u0077": "\uff57",
    "\u0078": "\uff58",
    "\u0079": "\uff59",
    "\u007a": "\uff5a",
}

# Derived reverse mappings for full-width to half-width conversion.
full_to_half_letter_map: SimpleCharacterMap = {
    **{v[0]: k for k, v in half_to_full_letter_map.items() if v[0] is not None},
    **{
        v[1]: f"{k}\uff9e"
        for k, v in half_to_full_letter_map.items()
        if v[1] is not None
    },
    **{
        v[2]: f"{k}\uff9f"
        for k, v in half_to_full_letter_map.items()
        if v[2] is not None
    },
}

full_to_half_voicing_mark_map: SimpleCharacterMap = {
    **{v: k for k, v in half_to_full_voicing_mark_map.items()},
    **{
        "\u3099": "\uff9e",
        "\u309a": "\uff9f",
    },
}

full_to_half_punctuation_map: SimpleCharacterMap = {
    v: k for k, v in half_to_full_punctuation_map.items()
}

full_to_half_corner_bracket_map: SimpleCharacterMap = {
    v: k for k, v in half_to_full_corner_bracket_map.items()
}

full_to_half_conjunction_mark_map: SimpleCharacterMap = {
    v: k for k, v in half_to_full_conjunction_mark_map.items()
}

full_to_half_length_mark_map: SimpleCharacterMap = {
    v: k for k, v in half_to_full_length_mark_map.items()
}

full_to_half_space_map: SimpleCharacterMap = {
    "\u3000": "\u0020",
}

full_to_half_ascii_symbol_map: SimpleCharacterMap = {
    v: k for k, v in half_to_full_ascii_symbol_map.items()
}

full_to_half_ascii_digit_map: SimpleCharacterMap = {
    v: k for k, v in half_to_full_ascii_digit_map.items()
}

full_to_half_ascii_alphabet_map: SimpleCharacterMap = {
    v: k for k, v in half_to_full_ascii_alphabet_map.items()
}

full_to_half_wave_dash: SimpleCharacterMap = {
    "\u301c": "\u007e",
}
