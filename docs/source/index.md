# Utsuho

Utsuho (うつほ) は、日本語の半角カタカナと全角カタカナの双方向変換をサポートする Python モジュールです。更に、ひらがなとカタカナの双方向変換も提供しています。

<div style="text-align: center;">
  <picture>
    <img src="_static/logo_500x500.png" alt="photo" width="200" height="200" />
  </picture>
</div>

:::{note}
バージョン 2.0.0 以降、ひらがなとカタカナの双方向変換が可能になりました。
:::

## 背景と目的

日本語の文字セットには、半角文字と全角文字があります。日本語では、同じデータを半角文字と全角文字のいずれでも表現することができます。しかしながら、半角文字と全角文字のいずれでデータを表現するかには標準がありません。日本語のデータを使用する時、半角文字と全角文字の不統一にしばしば遭遇します。

Python 標準ライブラリでは、Unicode 文字列の正規化により半角カタカナを全角カタカナへ変換できます。ただし、この変換には、合成文字の分解や全角の英数字を半角に変換するといった不要な変換が含まれることがあります。さらに、全角カタカナから半角カタカナへの逆方向の変換はサポートされていません。

Utsuho は、不要な変換を含まない日本語の半角カタカナと全角カタカナの双方向変換をサポートします。また、Utsuho は、日本語の多様な表記を統一する手段を提供することで、日本語のデータの有用性を高めることを目指します。

## 名称の由来

Utsuho の名称は "うつほ物語" に由来しており、この物語は平安時代に作成されたと考えられています。この物語にはカタカナの手習に関連する描写が含まれています。

## ユーザーガイド

- <project:usage.md>
- <project:conversion_rules_for_half_and_full_width.md>
- <project:conversion_rules_for_hiragana_and_katakana.md>
- <project:cli.md>

## API リファレンス

- <project:utsuho.rst>

## 索引と表

- {ref}`genindex`
- {ref}`modindex`
- {ref}`search`

```{toctree}
:maxdepth: 4
:caption: ユーザーガイド
:hidden:

usage
conversion_rules_for_half_and_full_width
conversion_rules_for_hiragana_and_katakana
cli
```

```{toctree}
:maxdepth: 4
:caption: API リファレンス
:hidden:

utsuho
```
