# CLI

CLI (コマンドラインインターフェース) を説明します。

Utsuho は、コーディングレスで使用できる CLI を提供します。

## シンタックス

CLI のシンタックスは、`--help` オプションで確認できます。

```console
% utsuho --help
Usage: utsuho [OPTIONS] COMMAND [ARGS]...

  Utsuho is a Python module that facilitates bidirectional conversion between
  half-width katakana and full-width katakana in Japanese, as well as between
  hiragana and katakana.

Options:
  --version  Show version.
  --help     Show this message and exit.

Commands:
  full-to-half          Convert full-width katakana to half-width katakana.
  half-to-full          Convert half-width katakana to full-width katakana.
  hiragana-to-katakana  Convert hiragana to katakana.
  katakana-to-hiragana  Convert katakana to hiragana.
```

### `--version` オプション

Utsuho のバージョンを確認できます。

```console
% utsuho --version
Utsuho x.x.x
```

コマンドと共に指定した場合、バージョンを表示して終了します。

### コマンド

Utsuho が提供する各機能は、コマンドで実行できます。

- `full-to-half` コマンド

  全角から半角への変換機能を実行するコマンドです。

- `half-to-full` コマンド

  半角から全角への変換機能を実行するコマンドです。

- `hiragana-to-katakana` コマンド

  ひらがなからカタカナへの変換機能を実行するコマンドです。

- `katakana-to-hiragana` コマンド

  カタカナからひらがなへの変換機能を実行するコマンドです。

## `full-to-half` コマンド

`full-to-half` コマンドのシンタックスは、`--help` オプションで確認できます。

```console
% utsuho full-to-half --help
Usage: utsuho full-to-half [OPTIONS] TEXT

  Convert full-width katakana to half-width katakana.

Options:
  -f, --file  Use TEXT as file path.
  --help      Show this message and exit.
```

コマンドでは、`TEXT` に指定した文字列に含まれる全角文字を半角文字へ変換できます。
変換結果は、標準出力へ出力されます。

```console
% utsuho full-to-half "キョウトシ　サキョウク　ギンカクジチョウ　２"
ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2
```

### `--file` オプション

コマンドの引数 `TEXT` を変換対象の文字列ではなく、変換対象の文字列を含むファイルのパスとして処理します。
変換結果は、標準出力へ出力されます。

例として、全角文字列を含む `full.txt` というファイルを用意します。

full.txt:

```text
キョウトシ　サキョウク　ギンカクジチョウ　２
```

`--file` オプションとファイルパスを指定して、コマンドを実行することで、ファイルの内容を変換できます。

```console
% utsuho full-to-half --file full.txt
ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2
```

## `half-to-full` コマンド

`half-to-full` コマンドのシンタックスは、`--help` オプションで確認できます。

```console
% utsuho half-to-full --help 
Usage: utsuho half-to-full [OPTIONS] TEXT

  Convert half-width katakana to full-width katakana.

Options:
  -f, --file  Use TEXT as file path.
  --help      Show this message and exit.
```

コマンドでは、`TEXT` に指定した文字列に含まれる半角文字を全角文字へ変換できます。
変換結果は、標準出力へ出力されます。

```console
% utsuho half-to-full "ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2"
キョウトシ　サキョウク　ギンカクジチョウ　２
```

### `--file` オプション

コマンドの引数 `TEXT` を変換対象の文字列ではなく、変換対象の文字列を含むファイルのパスとして処理します。
変換結果は、標準出力へ出力されます。

例として、半角文字列を含む `half.txt` というファイルを用意します。

half.txt:

```text
ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2
```

`--file` オプションとファイルパスを指定して、コマンドを実行することで、ファイルの内容を変換できます。

```console
% utsuho half-to-full --file half.txt
キョウトシ　サキョウク　ギンカクジチョウ　２
```

## `hiragana-to-katakana` コマンド

`hiragana-to-katakana` コマンドのシンタックスは、`--help` オプションで確認できます。

```console
% utsuho hiragana-to-katakana --help
Usage: utsuho hiragana-to-katakana [OPTIONS] TEXT

  Convert hiragana to katakana.

Options:
  -f, --file  Use TEXT as file path.
  --help      Show this message and exit.
```

コマンドでは、`TEXT` に指定した文字列に含まれるひらがなをカタカナへ変換できます。
変換結果は、標準出力へ出力されます。

```console
% utsuho hiragana-to-katakana "きょうとし　さきょうく　ぎんかくじちょう　２"
キョウトシ　サキョウク　ギンカクジチョウ　２
```

### `--file` オプション

コマンドの引数 `TEXT` を変換対象の文字列ではなく、変換対象の文字列を含むファイルのパスとして処理します。
変換結果は、標準出力へ出力されます。

例として、全角文字列を含む `hiragana.txt` というファイルを用意します。

hiragana.txt:

```text
きょうとし　さきょうく　ぎんかくじちょう　２
```

`--file` オプションとファイルパスを指定して、コマンドを実行することで、ファイルの内容を変換できます。

```console
% utsuho hiragana-to-katakana --file hiragana.txt
キョウトシ　サキョウク　ギンカクジチョウ　２
```

## `katakana-to-hiragana` コマンド

`katakana-to-hiragana` コマンドのシンタックスは、`--help` オプションで確認できます。

```console
% utsuho katakana-to-hiragana --help
Usage: utsuho katakana-to-hiragana [OPTIONS] TEXT

  Convert katakana to hiragana.

Options:
  -f, --file  Use TEXT as file path.
  --help      Show this message and exit.
```

コマンドでは、`TEXT` に指定した文字列に含まれるカタカナをひらがなへ変換できます。
変換結果は、標準出力へ出力されます。

```console
% utsuho katakana-to-hiragana "キョウトシ　サキョウク　ギンカクジチョウ　２"
きょうとし　さきょうく　ぎんかくじちょう　２
```

### `--file` オプション

コマンドの引数 `TEXT` を変換対象の文字列ではなく、変換対象の文字列を含むファイルのパスとして処理します。
変換結果は、標準出力へ出力されます。

例として、全角文字列を含む `katakana.txt` というファイルを用意します。

katakana.txt:

```text
キョウトシ　サキョウク　ギンカクジチョウ　２
```

`--file` オプションとファイルパスを指定して、コマンドを実行することで、ファイルの内容を変換できます。

```console
% utsuho katakana-to-hiragana --file katakana.txt
きょうとし　さきょうく　ぎんかくじちょう　２
```
