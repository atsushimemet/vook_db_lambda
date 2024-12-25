import pandas as pd

from tests.test_utils_10_1 import generate_mock_data_actual, generate_mock_data_expected
from vook_db_v7.exclude_noise import (
    product_noise_judge_brand,
)  # 実際のモジュール名に置き換え


def test_product_noise_judge_brand():
    # テスト用データ
    df_bulk_actual = generate_mock_data_actual()

    # 関数を実行
    df_cleaned = product_noise_judge_brand(df_bulk_actual)

    # 期待される出力
    df_bulk_expected = generate_mock_data_expected()

    # 結果を比較
    pd.testing.assert_frame_equal(df_cleaned.reset_index(drop=True), df_bulk_expected)
