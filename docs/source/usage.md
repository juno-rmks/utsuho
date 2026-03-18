# 使用方法

Utsuho を使うと、半角・全角の正規化と、ひらがな・カタカナの相互変換を明示的に行えます。
各変換は個別の Converter クラスとして提供されています。

## 半角から全角への変換

```python
from utsuho import HalfToFullConverter

text = "ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2"
converted = HalfToFullConverter().convert(text)

print(converted)
# キョウトシ　サキョウク　ギンカクジチョウ　２
```

## 全角から半角への変換

```python
from utsuho import FullToHalfConverter

text = "キョウトシ　サキョウク　ギンカクジチョウ　２"
converted = FullToHalfConverter().convert(text)

print(converted)
# ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2
```

## ひらがなからカタカナへの変換

```python
from utsuho import HiraganaToKatakanaConverter

text = "きょうとし　さきょうく　ぎんかくじちょう　２"
converted = HiraganaToKatakanaConverter().convert(text)

print(converted)
# キョウトシ　サキョウク　ギンカクジチョウ　２
```

## カタカナからひらがなへの変換

```python
from utsuho import KatakanaToHiraganaConverter

text = "キョウトシ　サキョウク　ギンカクジチョウ　２"
converted = KatakanaToHiraganaConverter().convert(text)

print(converted)
# きょうとし　さきょうく　ぎんかくじちょう　２
```

## 半角・全角変換の設定

`WidthConverterConfig` を使うと、半角・全角変換の際に、カタカナ以外の文字をどこまで正規化するかを制御できます。

```python
from utsuho import HalfToFullConverter, WidthConverterConfig

config = WidthConverterConfig(
    ascii_symbol=False,
    ascii_digit=False,
    ascii_alphabet=False,
)

text = "ｷﾞﾝｶｸｼﾞ 2F"
converted = HalfToFullConverter(config).convert(text)

print(converted)
# ギンカクジ 2F
```

設定可能な項目は次の通りです。

| パラメーター       | デフォルト値 | 説明                                                   |
| ------------------ | ------------ | ------------------------------------------------------ |
| `punctuation`      | `True`       | 句読点を変換するかどうか。                             |
| `corner_brucket`   | `True`       | 鉤括弧を変換するかどうか。                             |
| `conjunction_mark` | `True`       | 中黒を変換するかどうか。                               |
| `length_mark`      | `True`       | 長音記号を変換するかどうか。                           |
| `space`            | `True`       | スペースを変換するかどうか。                           |
| `ascii_symbol`     | `True`       | ASCII 記号を変換するかどうか。                         |
| `ascii_digit`      | `True`       | ASCII 数字を変換するかどうか。                         |
| `ascii_alphabet`   | `True`       | ASCII アルファベットを変換するかどうか。               |
| `wave_dash`        | `False`      | 全角から半角への変換時にウェーブダッシュを変換するか。 |

:::{note}
現在の公開 API では、歴史的な理由により `corner_brucket` という名前の引数を使用しています。
:::
