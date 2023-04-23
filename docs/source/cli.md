# CLI

CLI (コマンドラインインターフェース) を説明します。

Utsuho は、コーディングレスで使用できる CLI を提供します。

## シンタックス

CLI のシンタックスは、`--help` オプションで確認できます。

```console
% utsuho --help
Usage: utsuho [OPTIONS] COMMAND [ARGS]...

  Utsuho is an interconverter between Japanese half-width katakana and full-
  width katakana.

Options:
  --version  Show version.
  --help     Show this message and exit.

Commands:
  full-to-half  Convert full-width katakana to half-width katakana.
  half-to-full  Convert half-width katakana to full-width katakana.
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
