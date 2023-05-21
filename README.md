# blog to microCMS

- ブログから microCMS に移行するサンプル

## scripts

- スクリプト類。想定実行順で記載

### 1. mtToCsv.py

- ブログの export 機能でよく利用される『MT 形式』から microCMS の import に利用できる『CSV 形式』に変換するスクリプト
- はてなブログからの export データ実装。他ブログからの export データに関しては未検証。
- 入力は`contents.txt`、出力は`contents.csv`と`category.csv`

### 2. categoryMapping.py

- `contents.csv`のカテゴリを microCMS のカテゴリ ID に置換するスクリプト
- 上記の`category.csv`をインポート後、microCMS から GET したカテゴリ一覧が`category.json`ファイルとして同階層に配置されていることを前提とする
- 入力は`category.json`、出力は`mappedContents.csv`

### 3. request.py

- `mappedContents.csv`から microCMS にデータを POST するスクリプト
- ファイル名の`API_KEY`, `API_DOMAIN`を設定の上で利用
- 1POST ごとに 5 秒間隔を開けている
- `mappedContents.csv`に含まれる日付が JST である前提になっているので、UTC の場合は要修正
- 進捗＆エラー監視のためにレスポンスを`print`している。コンソールでなくファイルに残したい場合は下記が手軽
  - `python request.py > log.txt`

## app

- 上記の script を利用してブログから microCMS を利用したブログのサンプル
- 下記のように importData を優先する実装がされている
  - `importData.publishDate`がある場合は`importData.publishDate`を優先。ない場合は`publishedAt`を利用
  - `importData.content`がある場合は`importData.content`を優先。ない場合は`content`を利用
- importData が不要になった場合は、編集画面上で新データへ人力で移行を行う想定
