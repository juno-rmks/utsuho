# 使用方法

使用方法を説明します。

## 半角から全角への変換方法

半角から全角への変換には、[`utsuho.HalfToFullConverter`](#utsuho.HalfToFullConverter) クラスを使用します。

```python
from utsuho import HalfToFullConverter

halfwidth = 'ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2'
cnv = HalfToFullConverter()
fullwidth = cnv.convert(halfwidth)
```

上記の例では、`fullwidth` 変数に変換結果として "`キョウトシ サキョウク ギンカクジチョウ 2`" が格納されます。

## 全角から半角への変換方法

全角から半角への変換には、[`utsuho.FullToHalfConverter`](#utsuho.FullToHalfConverter) クラスを使用します。

```python
from utsuho import FullToHalfConverter

fullwidth = 'キョウトシ　サキョウク　ギンカクジチョウ　２'
cnv = FullToHalfConverter()
halfwidth = cnv.convert(fullwidth)
```

上記の例では、`halfwidth` 変数に変換結果として "`ｷｮｳﾄｼ　ｻｷｮｳｸ　ｷﾞﾝｶｸｼﾞﾁｮｳ　２`" が格納されます。

## 変換動作の設定方法

変換動作は、各 Converter クラスのコンストラクターの引数へカスタマイズした [`utsuho.ConverterConfig`](#utsuho.ConverterConfig) クラスのインスタンスを渡すことで変更できます。

```python
from utsuho import ConverterConfig, HalfToFullConverter

conf = ConverterConfig(punctuation=False)
cnv = HalfToFullConverter(conf)
```

カタカナ文字以外の変換動作は、`utsuho.ConverterConfig` クラスの次のパラメーターを設定します。

| パラメーター     | デフォルト値 | 説明                                       |
| ---------------- | ------------ | ------------------------------------------ |
| puctuation       | True         | 句読点を変換するかどうかを変更できます。   |
| corner_brucket   | True         | 鉤括弧を変換するかどうかを変更できます。   |
| conjunction_mark | True         | 中黒を変換するかどうかを変更できます。     |
| length_mark      | True         | 長音記号を変換するかどうかを変更できます。 |
