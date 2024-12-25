aws lambda get-function \
    --function-name vook_db_lambda_rakuten \
    --query 'Code.Location' \
    --output text
