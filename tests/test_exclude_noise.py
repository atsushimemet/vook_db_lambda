from tests.test_utils_10_1 import (
    generate_mock_data_actual as generate_mock_data_actual_1,
)
from tests.test_utils_10_1 import (
    generate_mock_data_expected as generate_mock_data_expected_1,
)
from tests.test_utils_10_2 import (
    generate_mock_data_actual as generate_mock_data_actual_2,
)
from tests.test_utils_10_2 import (
    generate_mock_data_expected as generate_mock_data_expected_2,
)
from vook_db_v7.exclude_noise import (
    product_noise_judge_brand,
)  # 実際のモジュール名に置き換え


def test_product_noise_judge_brand():
    """ブランドレベルのノイズが除外されていることをdf_bulkのname列を使用して確認"""
    # テスト用データ
    df_bulk_actual = generate_mock_data_actual_1()

    # 関数を実行
    df_cleaned = product_noise_judge_brand(df_bulk_actual)

    # 期待される出力
    df_bulk_expected = generate_mock_data_expected_1()

    # name列をセットとして比較
    actual_names = set(df_cleaned["name"])
    expected_names = set(df_bulk_expected["name"])

    # 集合が一致しているかを確認
    assert (
        actual_names == expected_names
    ), f"Actual names: {actual_names}, Expected names: {expected_names}"


def test_product_noise_judge_knowledge():
    """知識レベルのノイズが除外されていることをdf_bulkのname列を使用して確認"""
    # テスト用データ
    df_bulk_actual = generate_mock_data_actual_2()

    # 関数を実行
    df_cleaned = product_noise_judge_brand(df_bulk_actual)

    # 期待される出力
    df_bulk_expected = generate_mock_data_expected_2()

    # name列をセットとして比較
    actual_names = set(df_cleaned["name"])
    expected_names = set(df_bulk_expected["name"])

    # 集合が一致しているかを確認
    assert (
        actual_names == expected_names
    ), f"Actual names: {actual_names}, Expected names: {expected_names}"
