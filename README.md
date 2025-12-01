# Yahoo Auction Scraper

## 概要
このプロジェクトは、ヤフオクの購入履歴情報を自動で抽出し、CSV に保存するサンプルスクリプトです。  
ポートフォリオ用に作成したもので、実際のログイン情報は使用せず、サンプル HTML ファイルからテーブルデータを読み込みます。

## 機能
- サンプル HTML ファイルから購入商品情報を読み込み
- CSV に出力
- Pandas と BeautifulSoup を使用した HTML テーブル解析

## 使用方法
1. 仮想環境を作成してアクティブ化
```bash
python3 -m venv venv
source venv/bin/activate


必要なライブラリをインストール

pip install pandas beautifulsoup4 lxml html5lib openpyxl


スクリプト実行

python src/main.py


data/sample_purchase_output.csv に結果が保存されます

注意

実際のヤフオクのアカウントや購入情報は含まれていません

ポートフォリオ用サンプルとして動作確認用の HTML データを使用

ディレクトリ構成
yahoo-auction-scraper/
├─ data/
│  ├─ sample_purchase.html
│  └─ sample_purchase_output.csv
├─ src/
│  └─ main.py
├─ .gitignore
└─ README.md