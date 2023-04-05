""" Half-width and full-width characters mappings.
"""

half_to_full_letter_map = {
    '\uFF71': ('\u30A2', None, None),  # ｱ
    '\uFF72': ('\u30A4', None, None),  # ｲ
    '\uFF73': ('\u30A6', '\u30F4', None),  # ｳ
    '\uFF74': ('\u30A8', None, None),  # ｴ
    '\uFF75': ('\u30AA', None, None),  # ｵ
    '\uFF76': ('\u30AB', '\u30AC', None),  # ｶ
    '\uFF77': ('\u30AD', '\u30AE', None),  # ｷ
    '\uFF78': ('\u30AF', '\u30B0', None),  # ｸ
    '\uFF79': ('\u30B1', '\u30B2', None),  # ｹ
    '\uFF7A': ('\u30B3', '\u30B4', None),  # ｺ
    '\uFF7B': ('\u30B5', '\u30B6', None),  # ｻ
    '\uFF7C': ('\u30B7', '\u30B8', None),  # ｼ
    '\uFF7D': ('\u30B9', '\u30BA', None),  # ｽ
    '\uFF7E': ('\u30BB', '\u30BC', None),  # ｾ
    '\uFF7F': ('\u30BD', '\u30BE', None),  # ｿ
    '\uFF80': ('\u30BF', '\u30C0', None),  # ﾀ
    '\uFF81': ('\u30C1', '\u30C2', None),  # ﾁ
    '\uFF82': ('\u30C4', '\u30C5', None),  # ﾂ
    '\uFF83': ('\u30C6', '\u30C7', None),  # ﾃ
    '\uFF84': ('\u30C8', '\u30C9', None),  # ﾄ
    '\uFF85': ('\u30CA', None, None),  # ﾅ
    '\uFF86': ('\u30CB', None, None),  # ﾆ
    '\uFF87': ('\u30CC', None, None),  # ﾇ
    '\uFF88': ('\u30CD', None, None),  # ﾈ
    '\uFF89': ('\u30CE', None, None),  # ﾉ
    '\uFF8A': ('\u30CF', '\u30D0', '\u30D1'),  # ﾊ
    '\uFF8B': ('\u30D2', '\u30D3', '\u30D4'),  # ﾋ
    '\uFF8C': ('\u30D5', '\u30D6', '\u30D7'),  # ﾌ
    '\uFF8D': ('\u30D8', '\u30D9', '\u30DA'),  # ﾍ
    '\uFF8E': ('\u30DB', '\u30DC', '\u30DD'),  # ﾎ
    '\uFF8F': ('\u30DE', None, None),  # ﾏ
    '\uFF90': ('\u30DF', None, None),  # ﾐ
    '\uFF91': ('\u30E0', None, None),  # ﾑ
    '\uFF92': ('\u30E1', None, None),  # ﾒ
    '\uFF93': ('\u30E2', None, None),  # ﾓ
    '\uFF94': ('\u30E4', None, None),  # ﾔ
    '\uFF95': ('\u30E6', None, None),  # ﾕ
    '\uFF96': ('\u30E8', None, None),  # ﾖ
    '\uFF97': ('\u30E9', None, None),  # ﾗ
    '\uFF98': ('\u30EA', None, None),  # ﾘ
    '\uFF99': ('\u30EB', None, None),  # ﾙ
    '\uFF9A': ('\u30EC', None, None),  # ﾚ
    '\uFF9B': ('\u30ED', None, None),  # ﾛ
    '\uFF9C': ('\u30EF', '\u30F7', None),  # ﾜ
    '\uFF66': ('\u30F2', '\u30FA', None),  # ｦ
    '\uFF9D': ('\u30F3', None, None),  # ﾝ
    '\uFF6C': ('\u30E3', None, None),  # ｬ
    '\uFF6D': ('\u30E5', None, None),  # ｭ
    '\uFF6E': ('\u30E7', None, None),  # ｮ
    '\uFF6F': ('\u30C3', None, None),  # ｯ
    '\uFF67': ('\u30A1', None, None),  # ｧ
    '\uFF68': ('\u30A3', None, None),  # ｨ
    '\uFF69': ('\u30A5', None, None),  # ｩ
    '\uFF6A': ('\u30A7', None, None),  # ｪ
    '\uFF6B': ('\u30A9', None, None),  # ｫ
}

half_to_full_voicing_mark_map = {
    '\uFF9E': '\u309B',  # 濁点
    '\uFF9F': '\u309C',  # 半濁点
}

half_to_full_punctuation_map = {
    '\uFF64': '\u3001',  # 読点
    '\uFF61': '\u3002',  # 句点
}

half_to_full_corner_bracket_map = {
    '\uFF62': '\u300C',  # 鉤括弧始まり
    '\uFF63': '\u300D',  # 鉤括弧終わり
}

half_to_full_conjunction_mark_map = {
    '\uFF65': '\u30FB',  # 中黒
}

half_to_full_length_mark_map = {
    '\uFF70': '\u30FC',  # 長音
}

half_to_full_space_map = {
    '\u0020': '\u3000',  # 半角スペース
    '\u00A0': '\u3000',  # ノーブレークスペース
}

half_to_full_ascii_symbol_map = {
    '\u0021': '\uFF01',  # !
    '\u0022': '\uFF02',  # "
    '\u0023': '\uFF03',  # #
    '\u0024': '\uFF04',  # $
    '\u0025': '\uFF05',  # %
    '\u0026': '\uFF06',  # &
    '\u0027': '\uFF07',  # '
    '\u0028': '\uFF08',  # (
    '\u0029': '\uFF09',  # )
    '\u002A': '\uFF0A',  # *
    '\u002B': '\uFF0B',  # +
    '\u002C': '\uFF0C',  # ,
    '\u002D': '\uFF0D',  # -
    '\u002E': '\uFF0E',  # .
    '\u002F': '\uFF0F',  # /
    '\u003A': '\uFF1A',  # :
    '\u003B': '\uFF1B',  # ;
    '\u003C': '\uFF1C',  # <
    '\u003D': '\uFF1D',  # =
    '\u003E': '\uFF1E',  # >
    '\u003F': '\uFF1F',  # ?
    '\u0040': '\uFF20',  # @
    '\u005B': '\uFF3B',  # [
    '\u005C': '\uFF3C',  # \
    '\u005D': '\uFF3D',  # ]
    '\u005E': '\uFF3E',  # ^
    '\u005F': '\uFF3F',  # _
    '\u0060': '\uFF40',  # `
    '\u007B': '\uFF5B',  # {
    '\u007C': '\uFF5C',  # |
    '\u007D': '\uFF5D',  # }
    '\u007E': '\uFF5E',  # ~
}

half_to_full_ascii_digit_map = {
    '\u0030': '\uFF10',  # 0
    '\u0031': '\uFF11',  # 1
    '\u0032': '\uFF12',  # 2
    '\u0033': '\uFF13',  # 3
    '\u0034': '\uFF14',  # 4
    '\u0035': '\uFF15',  # 5
    '\u0036': '\uFF16',  # 6
    '\u0037': '\uFF17',  # 7
    '\u0038': '\uFF18',  # 8
    '\u0039': '\uFF19',  # 9
}

half_to_full_ascii_alphabet_map = {
    '\u0041': '\uFF21',  # A
    '\u0042': '\uFF22',  # B
    '\u0043': '\uFF23',  # C
    '\u0044': '\uFF24',  # D
    '\u0045': '\uFF25',  # E
    '\u0046': '\uFF26',  # F
    '\u0047': '\uFF27',  # G
    '\u0048': '\uFF28',  # H
    '\u0049': '\uFF29',  # I
    '\u004A': '\uFF2A',  # J
    '\u004B': '\uFF2B',  # K
    '\u004C': '\uFF2C',  # L
    '\u004D': '\uFF2D',  # M
    '\u004E': '\uFF2E',  # N
    '\u004F': '\uFF2F',  # O
    '\u0050': '\uFF30',  # P
    '\u0051': '\uFF31',  # Q
    '\u0052': '\uFF32',  # R
    '\u0053': '\uFF33',  # S
    '\u0054': '\uFF34',  # T
    '\u0055': '\uFF35',  # U
    '\u0056': '\uFF36',  # V
    '\u0057': '\uFF37',  # W
    '\u0058': '\uFF38',  # X
    '\u0059': '\uFF39',  # Y
    '\u005A': '\uFF3A',  # Z
    '\u0061': '\uFF41',  # a
    '\u0062': '\uFF42',  # b
    '\u0063': '\uFF43',  # c
    '\u0064': '\uFF44',  # d
    '\u0065': '\uFF45',  # e
    '\u0066': '\uFF46',  # f
    '\u0067': '\uFF47',  # g
    '\u0068': '\uFF48',  # h
    '\u0069': '\uFF49',  # i
    '\u006A': '\uFF4A',  # j
    '\u006B': '\uFF4B',  # k
    '\u006C': '\uFF4C',  # l
    '\u006D': '\uFF4D',  # m
    '\u006E': '\uFF4E',  # n
    '\u006F': '\uFF4F',  # o
    '\u0070': '\uFF50',  # p
    '\u0071': '\uFF51',  # q
    '\u0072': '\uFF52',  # r
    '\u0073': '\uFF53',  # s
    '\u0074': '\uFF54',  # t
    '\u0075': '\uFF55',  # u
    '\u0076': '\uFF56',  # v
    '\u0077': '\uFF57',  # w
    '\u0078': '\uFF58',  # x
    '\u0079': '\uFF59',  # y
    '\u007A': '\uFF5A',  # z
}

full_to_half_letter_map = {
    **{v[0]: k for k, v in half_to_full_letter_map.items() if v[0] is not None},
    **{v[1]: f'{k}\uFF9E' for k, v in half_to_full_letter_map.items() if v[1] is not None},
    **{v[2]: f'{k}\uFF9F' for k, v in half_to_full_letter_map.items() if v[2] is not None},
}

full_to_half_voicing_mark_map = {
    **{v: k for k, v in half_to_full_voicing_mark_map.items()},
    **{
        '\u3099': '\uFF9E',  # 濁点 (結合文字)
        '\u309A': '\uFF9F',  # 半濁点 (結合文字)
    }
}

full_to_half_punctuation_map = {v: k for k, v in half_to_full_punctuation_map.items()}

full_to_half_corner_bracket_map = {v: k for k, v in half_to_full_corner_bracket_map.items()}

full_to_half_conjunction_mark_map = {v: k for k, v in half_to_full_conjunction_mark_map.items()}

full_to_half_length_mark_map = {v: k for k, v in half_to_full_length_mark_map.items()}

full_to_half_space_map = {
    '\u3000': '\u0020',  # 全角スペース
}

full_to_half_ascii_symbol_map = {v: k for k, v in half_to_full_ascii_symbol_map.items()}

full_to_half_ascii_digit_map = {v: k for k, v in half_to_full_ascii_digit_map.items()}

full_to_half_ascii_alphabet_map = {v: k for k, v in half_to_full_ascii_alphabet_map.items()}

full_to_half_wave_dash = {
    '\u301C': '\u007E',
}
