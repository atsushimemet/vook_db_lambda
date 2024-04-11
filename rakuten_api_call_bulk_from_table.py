#!/usr/bin/env python
# coding: utf-8

import pandas as pd

# from vook_db_v7.config import platform_id
from vook_db_v7.rds_handler import get_products, put_products
from vook_db_v7.tests import run_all_if_checker
from vook_db_v7.utils import (
    DataFrame_maker_rakuten,
    DataFrame_maker_yahoo,
    create_api_input,
    repeat_dataframe_maker,
    set_id,
    upload_s3,
)


def main(event, context):
    # APIのインプットデータ作成
    df_api_input = create_api_input()
    # df_bulkの作成
    l_df_bulk = []
    for platform_id, func in zip(
        [1, 2], [DataFrame_maker_rakuten, DataFrame_maker_yahoo]
    ):
        df_bulk = repeat_dataframe_maker(df_api_input, platform_id, func)
        l_df_bulk.append(df_bulk)
    df_bulk = pd.concat(l_df_bulk, axis=0, ignore_index=True)
    # s3_file_name_products_raw_prev = "lambda_output/products_raw_prev.csv"
    s3_file_name_products_raw_prev = "vook-db/products_raw_prev.csv"
    df_bulk = set_id(df_bulk, s3_file_name_products_raw_prev)
    run_all_if_checker(df_bulk)
    # df_bulkをs３に保存
    upload_s3(df_bulk, s3_file_name_products_raw_prev)
    # # df_bulkをRDSに保存
    put_products(df_bulk)
    # # RDSに保存したデータを確認
    df_from_db = get_products()
    print("shape:", df_from_db.shape)
    print("id min:", df_from_db["id"].min())
    print("id max:", df_from_db["id"].max())


if __name__ == "__main__":
    main(1, 1)
