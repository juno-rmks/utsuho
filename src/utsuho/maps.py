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
    '\uFF9E': ('\u309B', None, None),  # 濁点
    '\uFF9F': ('\u309C', None, None),  # 半濁点
}

half_to_full_punctuation_map = {
    '\uFF64': ('\u3001', None, None),  # 読点
    '\uFF61': ('\u3002', None, None),  # 句点
}

half_to_full_corner_bracket_map = {
    '\uFF62': ('\u300C', None, None),  # 鉤括弧始まり
    '\uFF63': ('\u300D', None, None),  # 鉤括弧終わり
}

half_to_full_conjunction_mark_map = {
    '\uFF65': ('\u30FB', None, None),  # 中黒
}

half_to_full_length_mark_map = {
    '\uFF70': ('\u30FC', None, None),  # 長音
}

full_to_half_letter_map = {
    '\u30A2': '\uFF71',  # ア
    '\u30A4': '\uFF72',  # イ
    '\u30A6': '\uFF73',  # ウ
    '\u30A8': '\uFF74',  # エ
    '\u30AA': '\uFF75',  # オ
    '\u30AB': '\uFF76',  # カ
    '\u30AD': '\uFF77',  # キ
    '\u30AF': '\uFF78',  # ク
    '\u30B1': '\uFF79',  # ケ
    '\u30B3': '\uFF7A',  # コ
    '\u30B5': '\uFF7B',  # サ
    '\u30B7': '\uFF7C',  # シ
    '\u30B9': '\uFF7D',  # ス
    '\u30BB': '\uFF7E',  # セ
    '\u30BD': '\uFF7F',  # ソ
    '\u30BF': '\uFF80',  # タ
    '\u30C1': '\uFF81',  # チ
    '\u30C4': '\uFF82',  # ツ
    '\u30C6': '\uFF83',  # テ
    '\u30C8': '\uFF84',  # ト
    '\u30CA': '\uFF85',  # ナ
    '\u30CB': '\uFF86',  # ニ
    '\u30CC': '\uFF87',  # ヌ
    '\u30CD': '\uFF88',  # ネ
    '\u30CE': '\uFF89',  # ノ
    '\u30CF': '\uFF8A',  # ハ
    '\u30D2': '\uFF8B',  # ヒ
    '\u30D5': '\uFF8C',  # フ
    '\u30D8': '\uFF8D',  # ヘ
    '\u30DB': '\uFF8E',  # ホ
    '\u30DE': '\uFF8F',  # マ
    '\u30DF': '\uFF90',  # ミ
    '\u30E0': '\uFF91',  # ム
    '\u30E1': '\uFF92',  # メ
    '\u30E2': '\uFF93',  # モ
    '\u30E4': '\uFF94',  # ヤ
    '\u30E6': '\uFF95',  # ユ
    '\u30E8': '\uFF96',  # ヨ
    '\u30E9': '\uFF97',  # ラ
    '\u30EA': '\uFF98',  # リ
    '\u30EB': '\uFF99',  # ル
    '\u30EC': '\uFF9A',  # レ
    '\u30ED': '\uFF9B',  # ロ
    '\u30EF': '\uFF9C',  # ワ
    '\u30F2': '\uFF66',  # ヲ
    '\u30F3': '\uFF9D',  # ン
    '\u30E3': '\uFF6C',  # ャ
    '\u30E5': '\uFF6D',  # ュ
    '\u30E7': '\uFF6E',  # ョ
    '\u30C3': '\uFF6F',  # ッ
    '\u30A1': '\uFF67',  # ァ
    '\u30A3': '\uFF68',  # ィ
    '\u30A5': '\uFF69',  # ゥ
    '\u30A7': '\uFF6A',  # ェ
    '\u30A9': '\uFF6B',  # ォ
    '\u30AC': '\uFF76\uFF9E',  # ガ
    '\u30AE': '\uFF77\uFF9E',  # ギ
    '\u30B0': '\uFF78\uFF9E',  # グ
    '\u30B2': '\uFF79\uFF9E',  # ゲ
    '\u30B4': '\uFF7A\uFF9E',  # ゴ
    '\u30B6': '\uFF7B\uFF9E',  # ザ
    '\u30B8': '\uFF7C\uFF9E',  # ジ
    '\u30BA': '\uFF7D\uFF9E',  # ズ
    '\u30BC': '\uFF7E\uFF9E',  # ゼ
    '\u30BE': '\uFF7F\uFF9E',  # ゾ
    '\u30C0': '\uFF80\uFF9E',  # ダ
    '\u30C2': '\uFF81\uFF9E',  # ヂ
    '\u30C5': '\uFF82\uFF9E',  # ヅ
    '\u30C7': '\uFF83\uFF9E',  # デ
    '\u30C9': '\uFF84\uFF9E',  # ド
    '\u30D0': '\uFF8A\uFF9E',  # バ
    '\u30D3': '\uFF8B\uFF9E',  # ビ
    '\u30D6': '\uFF8C\uFF9E',  # ブ
    '\u30D9': '\uFF8D\uFF9E',  # ベ
    '\u30DC': '\uFF8E\uFF9E',  # ボ
    '\u30D1': '\uFF8A\uFF9F',  # パ
    '\u30D4': '\uFF8B\uFF9F',  # ピ
    '\u30D7': '\uFF8C\uFF9F',  # プ
    '\u30DA': '\uFF8D\uFF9F',  # ペ
    '\u30DD': '\uFF8E\uFF9F',  # ポ
    '\u30F4': '\uFF73\uFF9E',  # ヴ
    '\u30F7': '\uFF9C\uFF9E',  # ヷ
    '\u30FA': '\uFF66\uFF9E',  # ヺ
}

full_to_half_voicing_mark_map = {
    '\u3099': '\uFF9E',  # 濁点 (結合文字)
    '\u309A': '\uFF9F',  # 半濁点 (結合文字)
    '\u309B': '\uFF9E',  # 濁点
    '\u309C': '\uFF9F',  # 半濁点
}

full_to_half_punctuation_map = {
    '\u3001': '\uFF64',  # 句点
    '\u3002': '\uFF61',  # 読点
}

full_to_half_corner_bracket_map = {
    '\u300C': '\uFF62',  # 鉤括弧始まり
    '\u300D': '\uFF63',  # 鉤括弧終わり
}

full_to_half_conjunction_mark_map = {
    '\u30FB': '\uFF65',  # 中黒
}

full_to_half_length_mark_map = {
    '\u30FC': '\uFF70',  # 長音
}
