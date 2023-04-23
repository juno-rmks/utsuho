Utsuho
======

.. note::

   This project currently only provides Japanese documentation.

Utsuho (うつほ) は、日本語の半角カタカナと全角カタカナの相互変換を提供する Python モジュールです。

Utsuho という名称は、カタカナに関する記述がある平安時代中期に成立したとされる長編物語 \"うつほ物語\" に由来します。

Python 標準ライブラリでも Unicode 文字列の正規化として半角カタカナを全角カタカナへ変換できますが、合成文字を分解したり、全角英数字記号を半角へ変換したり、と不必要な変換も伴います。又、全角カタカナから半角カタカナへの変換はできません。Utsuho は、日本語の文脈を考慮し、半角カタカナと全角カタカナの相互変換のみを提供します。

.. toctree::
   :maxdepth: 4
   :caption: ユーザーガイド:

   usages
   mappings
   cli

.. toctree::
   :maxdepth: 4
   :caption: API リファレンス:

   utsuho

索引と表
========

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
