# README
自作した便利ツールやスクリプトを配置しています。

## 01_getURL_IE
内容物
* getURL_IE.vbs
言語
* VBScript

### 機能、使い方、環境
`getURL_IE.vbs`をダウンロードします。  
Internet ExplorerをWebサイトをいくつか開いた状態で、`getURL_IE.vbs`をダブルクリックなどで実行すれば、  
開いているWebサイトのタイトル/URLを取得し、クリップボードで貼り付け可能な状態にしてくれます。  
Windows7、IE11で動作確認しています。  

### 背景
Internet Explorer以外のブラウザを利用できない状況や端末で  
たくさんのサイトを開き、そのURLを連携したいときに、煩雑な作業を避けて、自動化したいがために作成しました。  
そのようなシーンは、何度もあったので、重宝しました。  

### コメント
Google Chromeであれば、  
「GetTabInfo」という強力な拡張機能を利用できるのに...  
参考：https://chrome.google.com/webstore/detail/gettabinfo/iadhcoaabobddcebhmheikmbcjcigjhc  
大人の事情でIEを利用せざるを得ないときにどうぞ！  

## 02_downloadSecuritiesReport
内容物
* downloadProgram.py（実行プログラム）
* TokyoStockExchange1stSection_LocalCode.csv（証券コードのリスト）
言語
* Python

### 機能、使い方、環境
Pythonの開発環境を用意し、`downloadProgram.py`を実行する。  
Anaconda + Jupyter Notebookが手軽で便利でした。  
参考：https://qiita.com/KI1208/items/a7765e6fdc95c3e03609  
`os.getcwd()のパス/json/`と`os.getcwd()のパス/xbrl/`というフォルダは事前に用意しておく。  


### 背景
案件の都合で、有価証券報告書（売上高、営業利益など）のデータについて、上場企業数分を必要になったが、金融庁のEDINET（https://www.fsa.go.jp/search/20130917.html）から手作業でダウンロードするわけにもいかないため、自動取得プログラムを作成しました。

### コメント
さらに踏み込めば、売上高、営業利益など数値データも同時に抽出することも可能。  
以下、参考サイト。  
EDINETのXBRL用のPythonライブラリを作った - Parser編 - Qiita  
https://qiita.com/shoe116/items/dd362ad880f2b6baa96f  
UFOキャッチャーからXBRLをダウンロード&パースするクラスを作った - Qiita  
https://qiita.com/sawadybomb/items/67059635545cf0a11c8e  
