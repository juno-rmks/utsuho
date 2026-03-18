# CLI

Utsuho には、対話的な利用やスクリプトからの呼び出しに適したコマンドラインインターフェースが用意されています。
変換結果は標準出力に出力されるため、シェルスクリプトからも扱いやすくなっています。

## 基本構文

`--help` オプションで CLI の構文を確認できます。

```console
% utsuho --help
Usage: utsuho [OPTIONS] COMMAND [ARGS]...

  Utsuho provides deterministic normalization utilities for Japanese text,
  including width normalization and hiragana/katakana conversion.

Options:
  --version  Show the version.
  --help     Show this message and exit.

Commands:
  full-to-half          Convert from full-width to half-width characters.
  half-to-full          Convert from half-width to full-width characters.
  hiragana-to-katakana  Convert from hiragana to katakana.
  katakana-to-hiragana  Convert from katakana to hiragana.
```

`--version` オプションを指定すると、バージョンを表示して終了します。

```console
% utsuho --version
Utsuho x.x.x
```

## 使用例

```console
% utsuho full-to-half "キョウトシ　サキョウク　ギンカクジチョウ　２"
ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2

% utsuho half-to-full "ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2"
キョウトシ　サキョウク　ギンカクジチョウ　２

% utsuho hiragana-to-katakana "きょうとし　さきょうく　ぎんかくじちょう　２"
キョウトシ　サキョウク　ギンカクジチョウ　２

% utsuho katakana-to-hiragana "キョウトシ　サキョウク　ギンカクジチョウ　２"
きょうとし　さきょうく　ぎんかくじちょう　２
```

## 各コマンド

### `full-to-half`

全角文字を半角文字へ変換します。

```console
% utsuho full-to-half --help
Usage: utsuho full-to-half [OPTIONS] TEXT

  Convert from full-width to half-width characters.

Options:
  -f, --file  Whether to use TEXT as a file path.
  --help      Show this message and exit.
```

### `half-to-full`

半角文字を全角文字へ変換します。

```console
% utsuho half-to-full --help
Usage: utsuho half-to-full [OPTIONS] TEXT

  Convert from half-width to full-width characters.

Options:
  -f, --file  Whether to use TEXT as a file path.
  --help      Show this message and exit.
```

### `hiragana-to-katakana`

ひらがなをカタカナへ変換します。

```console
% utsuho hiragana-to-katakana --help
Usage: utsuho hiragana-to-katakana [OPTIONS] TEXT

  Convert from hiragana to katakana.

Options:
  -f, --file  Whether to use TEXT as a file path.
  --help      Show this message and exit.
```

### `katakana-to-hiragana`

カタカナをひらがなへ変換します。

```console
% utsuho katakana-to-hiragana --help
Usage: utsuho katakana-to-hiragana [OPTIONS] TEXT

  Convert from katakana to hiragana.

Options:
  -f, --file  Whether to use TEXT as a file path.
  --help      Show this message and exit.
```

## `--file` オプション

各コマンドは `--file` オプションと `-f` 短縮形をサポートしています。指定すると、`TEXT` は UTF-8 テキストファイルのパスとして扱われます。

```console
% utsuho full-to-half --file full.txt
ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2
```
