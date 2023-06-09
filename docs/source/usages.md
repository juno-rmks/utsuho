# 使用方法

使用方法を説明します。

## 半角から全角への変換方法

半角から全角への変換には、[`utsuho.converters.HalfToFullConverter`](#utsuho.converters.HalfToFullConverter) クラスを使用します。

```python
from utsuho import HalfToFullConverter

halfwidth = 'ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2'
cnv = HalfToFullConverter()
fullwidth = cnv.convert(halfwidth)
```

上記の例では、`fullwidth` 変数に変換結果として "`キョウトシ　サキョウク　ギンカクジチョウ　２`" が格納されます。

## 全角から半角への変換方法

全角から半角への変換には、[`utsuho.converters.FullToHalfConverter`](#utsuho.converters.FullToHalfConverter) クラスを使用します。

```python
from utsuho import FullToHalfConverter

fullwidth = 'キョウトシ　サキョウク　ギンカクジチョウ　２'
cnv = FullToHalfConverter()
halfwidth = cnv.convert(fullwidth)
```

上記の例では、`halfwidth` 変数に変換結果として "`ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2`" が格納されます。

## 変換動作の設定方法

変換動作は、各 Converter クラスのコンストラクターの引数へカスタマイズした [`utsuho.converters.ConverterConfig`](#utsuho.converters.ConverterConfig) クラスのインスタンスを渡すことで変更できます。

```python
from utsuho import ConverterConfig, HalfToFullConverter

conf = ConverterConfig(punctuation=False)
cnv = HalfToFullConverter(conf)
```

カタカナ文字以外の変換動作は、`utsuho.ConverterConfig` クラスの次のパラメーターを設定します。

| パラメーター     | デフォルト値 | 説明                                                   |
| ---------------- | ------------ | ------------------------------------------------------ |
| puctuation       | True         | 句読点を変換するかどうかを切り替えできます。           |
| corner_brucket   | True         | 鉤括弧を変換するかどうかを切り替えできます。           |
| conjunction_mark | True         | 中黒を変換するかどうかを切り替えできます。             |
| length_mark      | True         | 長音記号を変換するかどうかを切り替えできます。         |
| space            | True         | スペースを変換するかどうかを切り替えできます。         |
| ascii_symbol     | True         | 記号を変換するかどうかを切り替えできます。             |
| ascii_digit      | True         | 数字を変換するかどうかを切り替えできます。             |
| ascii_alphabet   | True         | アルファベットを変換するかどうかを切り替えできます。   |
| wave_dash        | True         | ウェーブダッシュを変換するかどうかを切り替えできます。 |
