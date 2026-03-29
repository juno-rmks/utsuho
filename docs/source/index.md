# Utsuho

Utsuho (うつほ) は、日本語テキストの表記揺れを決定的な変換ルールで正規化する Python ライブラリです。

半角・全角の変換や、ひらがな・カタカナの変換といった文字単位の正規化に特化しており、汎用的な Unicode 正規化で起こり得る不要な文字変換を避けられます。

すべての変換は文字単位で行われ、辞書や文脈に依存しない決定的な挙動を持ちます。この特性により、Utsuho は AI エージェントから呼び出される外部ツールとしても適しており、再現性のあるテキスト正規化処理を安定して提供できます。

- 半角カタカナと全角カタカナの双方向変換
- ひらがなとカタカナの双方向変換
- スペース、句読点、ASCII 記号、数字、アルファベットの変換可否を設定可能
- シェルやパイプライン処理で使いやすい CLI を提供
- MCP (Model Context Protocol) サーバとしても利用可能

```{figure} _static/logo_wide.png
:align: center
:width: 450px

Utsuho project logo (wide version)
```

## 背景

日本語テキストでは、半角と全角、ひらがなとカタカナなど、同じ内容を複数の表記で表せます。そのため、入力データの統一や検索前処理では、表記揺れの吸収が必要になることがよくあります。

Python 標準ライブラリの Unicode 正規化でも一部の変換は可能ですが、ASCII 記号まで変換されるなど、意図しない変換が含まれる場合があります。

このように、日本語テキストの正規化には「必要な変換だけを行いたい」という要件がありながら、既存の手段では過剰な変換が入りやすいという課題があります。

## パフォーマンス

Utsuho は pure Python 実装ですが、文字単位の正規化処理としては実用的なスループットを提供します。

プロジェクトの long-input ベンチマークでは、CPython 3.10 上で、ひらがな・カタカナ変換はおおむね毎秒 700 万から 800 万文字、半角・全角変換はおおむね毎秒 100 万から 300 万文字程度を処理できます。

これらの値は参考値であり、プラットフォーム、Python バージョン、入力の偏り、電源や熱の条件によって変動します。

## 名称の由来

Utsuho の名称は「うつほ物語」に由来します。平安時代に成立したと考えられるこの物語には、カタカナの手習いに関連する描写が含まれています。

## ユーザーガイド

- <project:usage.md>
- <project:cli.md>
- <project:mcp.md>
- <project:conversion_rules_for_half_and_full_width.md>
- <project:conversion_rules_for_hiragana_and_katakana.md>

## プロジェクト

- <project:roadmap.md>

## API リファレンス

- <project:api/utsuho.rst>

## 設計書

- <project:spec/2.3.2.md>

## 索引と表

- {ref}`genindex`
- {ref}`modindex`
- {ref}`search`

```{toctree}
:maxdepth: 4
:caption: ユーザーガイド
:hidden:

usage
cli
mcp
conversion_rules_for_half_and_full_width
conversion_rules_for_hiragana_and_katakana
```

```{toctree}
:maxdepth: 4
:caption: プロジェクト
:hidden:

roadmap
```

```{toctree}
:maxdepth: 4
:caption: API リファレンス
:hidden:

api/utsuho
```

```{toctree}
:maxdepth: 4
:caption: 設計書
:hidden:

spec/2.3.2.md
```
