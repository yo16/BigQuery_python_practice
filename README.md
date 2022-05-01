# BigQuery_python_practice
PythonでBigQueryの操作をするサンプル

# 準備

## (1)Python環境
```
pip install pandas-gbq google.cloud google-auth
```

## (2)GCP環境
- ①カスタムロールを定義
  - 付与した権限
    - bigquery.datasets.get
    - bigquery.jobs.create
    - bigquery.tables.create
      - いらないかも。あとで消して試してみる
    - bigquery.tables.delete
      - いらないかも。あとで消して試してみる
    - bigquery.tables.export
      - いらないかも。あとで消して試してみる
    - bigquery.tables.get
      - いらないかも。あとで消して試してみる
    - bigquery.tables.getData
    - bigquery.tables.list
      - いらないかも。あとで消して試してみる
    - bigquery.tables.update
    - bigquery.tables.updateData
- ②サービスアカウントを作成
- ③IAMにサービスアカウントをプリンシパルとして追加
  - ②を追加し、ロールとして①で作ったロールを付与。
- ④サービスアカウントの鍵を作成
  - JSONファイルを入手
- ⑤"credentials"フォルダを作成し、"credentials/"を`.gitignore`へ追記し、フォルダ内に鍵のjsonファイルを置き、`git status`に含まれないことを確認
  - めちゃ重要。この一連の内容は必ず一気にやる。
  - フォルダを作るだけだと`git status`に出ないので注意。
  - これが外部(publicなgithubとか)に出ると、勝手にアクセスできてしまう。
    - privateすら危ないのでアップしない方がよい。githubのソースを使った能力検定みたいなサービスにうっかり登録し、そこから漏洩する可能性まである。そうなると個人でガードできない。


# 参考
- [Google BigQuery](https://cloud.google.com/bigquery?hl=ja) > [ドキュメント](https://cloud.google.com/docs?hl=ja) > [ガイド](https://cloud.google.com/bigquery/docs/introduction?hl=ja) > 開発 > BigQuery API の基本 > 認証 > [はじめに](https://cloud.google.com/bigquery/docs/authentication?hl=ja)
- [Google BigQuery](https://cloud.google.com/bigquery?hl=ja) > [ドキュメント](https://cloud.google.com/docs?hl=ja) > [ガイド](https://cloud.google.com/bigquery/docs/introduction?hl=ja) > 開発 > Pythonライブラリの使用 > [pandas-gbq との比較](https://cloud.google.com/bigquery/docs/pandas-gbq-migration?hl=ja)
- pandas > API reference > Input/output  > [pandas.read_gbq](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_gbq.html)
  - BigQueryからDataFrameへselect。
- pandas > API reference > DataFrame  > [pandas.DataFrame.to_gbq](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_gbq.html)
  - DataFrameからBigQueryへinsert。
