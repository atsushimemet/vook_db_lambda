# 実行環境
## Lambdaのレイヤー作成方法
### 公式イメージの取得
```
docker pull amazon/aws-sam-cli-build-image-python3.9
# https://hub.docker.com/r/amazon/aws-sam-cli-build-image-python3.9
```
### コンテナに入る
```
docker run -it -v $(pwd):/var/task amazon/aws-sam-cli-build-image-python3.9:latest
```
### 必要なライブラリをインストール
pip install pandas -t ./python
pip install sshtunnel -t ./python
pip install pymysql -t ./python
pip install boto3 -t ./python
pip install requests -t ./python

### zip化
```
zip -r lambda-layer.zip ./python
```
### マネコンで作業
1. s3アップロード
2. httpsのURL取得
3. zipファイルをアップロードしてレイヤー作成
4. 関数側でレイヤーを指定
### 参考
https://pomblue.hatenablog.com/entry/2021/06/08/230146

# 設計
## 楽天 - rakuten_api_call_bulk_from_table
1. 知識情報の取得
2. 対象のワードリスト作成（ngワードを消す ex. BIG E）
3. 修正版のテーブルを作成（知識情報の修正）
4. df_bulkの作成
   1. repeat_dataframe_makerを実行
   2. DataFrame_makerの実行
      1. 設定
         1. cnt:情報取得対象のページ番号
         2. df:WANT_LISTでカラムを指定してデータフレームを作成
         3. req_params["page"]:リクエストパラメータ内のページ番号
         4. req_params["keyword"]:リクエストパラメータ内のキーワード
      2. ループ
      3. 整形
5. IDの設定
6. df_bulkをs3に保存
7. df_bulkをRDSに保存
8. RDSに保存したデータを確認
## Yahoo - yahoo_api_call_bulk_from_table
1. 設定値の作成
2. DataFrame_makerの実行
   1. 設定
      1. start_num:取得対象の商品番号
      2. step:繰り返し処理の間隔
      3. max_products:商品数の最大値
      4. l_df:作成したDataFrameを格納するリスト
   2. ループ
3. ファイル出力
## yahoo_api_call_bulk_from_tableの修正方針
1. DataFrame_makerを楽天と同じ形式に修正
2. repeat_dataframe_makerを作成
3. 楽天の2~8を実装
4. 設定値の共通処理作成
5. その他共通処理作成
## 共通処理検討
1. 設計
   1. 共通のrepeat_dataframe_makerを利用する。
      1. 楽天
      2. Yahoo
   2. 知識情報の取得処理を共通処理にする。
   3. ID設定を共通処理にする。
# 他
vook_db_lambda_rakuten-84eea0cd-a965-452a-8b56-a3d5f965e7f3.zipは2024/04/10に本番環境から移行する際に生成したzipファイル。
本番環境のコードが入っている。
