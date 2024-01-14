# CLI (Command Line Interface)

Utsuho は Python ライブラリとしてだけでなく、対話的に利用することができる直感的なコマンドラインインターフェースも提供しています。

## シンタックス

`--help` オプションを使用して、CLI の構文を表示できます。

```console
% utsuho --help
Usage: utsuho [OPTIONS] COMMAND [ARGS]...

  Utsuho is a Python module that facilitates bidirectional conversion between
  half-width katakana and full-width katakana in Japanese. Furthermore, it
  offers bidirectional conversion between hiragana and katakana.

Options:
  --version  Show the version.
  --help     Show this message and exit.

Commands:
  full-to-half          Convert from full-width to half-width characters.
  half-to-full          Convert from half-width to full-width characters.
  hiragana-to-katakana  Convert from hiragana to katakana.
  katakana-to-hiragana  Convert from katakana to hiragana.
```

### `--version` オプション

`--version` オプションを使用して、Utsuho のバージョンを表示できます。バージョンを表示した後、Utsuho は終了します。

他のオプションやコマンドと一緒に指定された場合、Utsuho はバージョンを表示して終了します。

```console
% utsuho --version
Utsuho x.x.x
```

### コマンド

Utsuho は以下のコマンドを提供しています。

- `full-to-half` コマンド

  このコマンドは、全角文字から半角文字への変換を実行します。

- `half-to-full` コマンド

  このコマンドは、半角文字から全角文字への変換を実行します。

- `hiragana-to-katakana` コマンド

  このコマンドは、ひらがなからカタカナへの変換を実行します。

- `katakana-to-hiragana` コマンド

  このコマンドは、カタカナからひらがなへの変換を実行します。

## `full-to-half` コマンド

このコマンドは、全角文字から半角文字への変換を実行します。

`--help` オプションを使用して、コマンドの構文を表示できます。

```console
% utsuho full-to-half --help
Usage: utsuho full-to-half [OPTIONS] TEXT

  Convert from full-width to half-width characters.

Options:
  -f, --file  Whether to use TEXT as a file path.
  --help      Show this message and exit.
```

`TEXT` に含まれる全角文字を半角文字に変換できます。変換結果は標準出力に出力されます。

```console
% utsuho full-to-half "キョウトシ　サキョウク　ギンカクジチョウ　２"
ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2
```

### `--file` オプション

`TEXT` パラメーターを変換対象の文字列を含むファイルのパスと見做します。

ファイル内の全角文字を半角文字に変換できます。変換結果は標準出力に出力されます。

全角文字を含むファイル "full.txt" を作成します。

full.txt:

```text
キョウトシ　サキョウク　ギンカクジチョウ　２
```

`--file` オプションとファイルのパス "full.txt" を指定して、コマンドを実行します。

```console
% utsuho full-to-half --file full.txt
ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2
```

## `half-to-full` コマンド

このコマンドは、半角文字から全角文字への変換を実行します。

`--help` オプションを使用して、コマンドの構文を表示できます。

```console
% utsuho half-to-full --help
Usage: utsuho half-to-full [OPTIONS] TEXT

  Convert from half-width to full-width characters.

Options:
  -f, --file  Whether to use TEXT as a file path.
  --help      Show this message and exit.
```

`TEXT` に含まれる半角文字を全角文字に変換できます。変換結果は標準出力に出力されます。

```console
% utsuho half-to-full "ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2"
キョウトシ　サキョウク　ギンカクジチョウ　２
```

### `--file` オプション

`TEXT` パラメーターを変換対象の文字列を含むファイルのパスと見做します。

ファイル内の半角文字を全角文字に変換できます。変換結果は標準出力に出力されます。

全角文字を含むファイル "half.txt" を作成します。

half.txt:

```text
ｷｮｳﾄｼ ｻｷｮｳｸ ｷﾞﾝｶｸｼﾞﾁｮｳ 2
```

`--file` オプションとファイルのパス "half.txt" を指定して、コマンドを実行します。

```console
% utsuho half-to-full --file half.txt
キョウトシ　サキョウク　ギンカクジチョウ　２
```

## `hiragana-to-katakana` コマンド

このコマンドは、ひらがなからカタカナへの変換を実行します。

`--help` オプションを使用して、コマンドの構文を表示できます。

```console
% utsuho hiragana-to-katakana --help
Usage: utsuho hiragana-to-katakana [OPTIONS] TEXT

  Convert from hiragana to katakana.

Options:
  -f, --file  Whether to use TEXT as a file path.
  --help      Show this message and exit.
```

`TEXT` に含まれるひらがなをカタカナに変換できます。変換結果は標準出力に出力されます。

```console
% utsuho hiragana-to-katakana "きょうとし　さきょうく　ぎんかくじちょう　２"
キョウトシ　サキョウク　ギンカクジチョウ　２
```

### `--file` オプション

`TEXT` パラメーターを変換対象の文字列を含むファイルのパスと見做します。

ファイル内のひらがなをカタカナに変換できます。変換結果は標準出力に出力されます。

ひらがなを含むファイル "hiragana.txt" を作成します。

hiragana.txt:

```text
きょうとし　さきょうく　ぎんかくじちょう　２
```

`--file` オプションとファイルのパス "hiragana.txt" を指定して、コマンドを実行します。

```console
% utsuho hiragana-to-katakana --file hiragana.txt
キョウトシ　サキョウク　ギンカクジチョウ　２
```

## `katakana-to-hiragana` コマンド

このコマンドは、カタカナからひらがなへの変換を実行します。

`--help` オプションを使用して、コマンドの構文を表示できます。

```console
% utsuho katakana-to-hiragana --help
Usage: utsuho katakana-to-hiragana [OPTIONS] TEXT

  Convert from katakana to hiragana.

Options:
  -f, --file  Whether to use TEXT as a file path.
  --help      Show this message and exit.
```

`TEXT` に含まれるカタカナをひらがなに変換できます。変換結果は標準出力に出力されます。

```console
% utsuho katakana-to-hiragana "キョウトシ　サキョウク　ギンカクジチョウ　２"
きょうとし　さきょうく　ぎんかくじちょう　２
```

### `--file` オプション

`TEXT` パラメーターを変換対象の文字列を含むファイルのパスと見做します。

ファイル内のカタカナをひらがなに変換できます。変換結果は標準出力に出力されます。

カタカナを含むファイル "katakana.txt" を作成します。

katakana.txt:

```text
キョウトシ　サキョウク　ギンカクジチョウ　２
```

`--file` オプションとファイルのパス "katakana.txt" を指定して、コマンドを実行します。

```console
% utsuho katakana-to-hiragana --file katakana.txt
きょうとし　さきょうく　ぎんかくじちょう　２
```
