# Utsuho

Utsuho (うつほ) は、日本語の半角文字と全角文字、及びひらがなとカタカナの相互変換を提供する Python モジュールです。

## コンセプト

日本語のコンピューティング環境では、半角文字と全角文字があります。
日本語のデータは、データ提供元の判断により、半角文字と全角文字のいずれかで提供されています。
複数のデータセットを組み合わせて使用する場合、日本語のデータは半角文字と全角文字を統一する必要があります。

また、日本語の仮名表記には、ひらがなとカタカナがあります。
ひらがなとカタカナにも半角文字と全角文字と同じ課題があります。

Utsuho は、日本語の多様な表記を統一する手段を提供することで、日本語のデータの有用性を高めることを目指します。

## 名称の由来

Utsuho という名称は、平安時代中期に成立したとされる長編物語 "うつほ物語" に由来します。
"うつほ物語" には仮名手習に関する記述があることから、モジュールの名称に採用しました。

## ユーザーガイド

- <project:usages.md>
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

usages
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
