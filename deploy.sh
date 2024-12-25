# ZIPファイル名を変数に設定
ZIP_FILE="vook_db_lambda_20241225_2.zip"

# ZIPファイルを作成
zip -r $ZIP_FILE . -x ".env/*" -x ".git/*" -x ".mypy_cache/*" -x "vook_db_v7/__pycache__/*" -x "*.zip" -x "notebook/*" -x "data/.DS_Store" -x "*/.ipynb_checkpoints/*"

# 関数コードの取得（オプション）
aws lambda get-function \
    --function-name vook_db_lambda_rakuten \
    --query 'Code.Location' \
    --output text

# Lambda 関数コードの更新
aws lambda update-function-code \
    --function-name vook_db_lambda_rakuten \
    --zip-file fileb://$ZIP_FILE
