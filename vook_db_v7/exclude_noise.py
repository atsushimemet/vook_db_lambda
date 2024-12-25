import pandas as pd

from vook_db_v7.rds_handler import get_knowledges

# product_noise_judge.csvを読み込む
df_product_noise_judge = pd.read_csv("./data/input/product_noise_judge.csv")


def product_noise_judge_brand():
    return ""


def product_noise_judge(
    df: pd.DataFrame, df_judge: pd.DataFrame = df_product_noise_judge
):
    l_df_knowledge_excluded = []
    for knowledge_id in df["knowledge_id"].unique():
        df_knowledge = df[df["knowledge_id"] == knowledge_id].copy()
        df_knowledge_tmp = df_knowledge.copy()  # 初期化
        for i, noise in enumerate(
            df_judge[df_judge["product_id"] == knowledge_id]["noise_nm"]
        ):
            df_knowledge_tmp = df_knowledge_tmp[
                ~df_knowledge_tmp["name"].str.contains(noise, regex=True, na=False)
            ].copy()
        l_df_knowledge_excluded.append(df_knowledge_tmp.copy())
    return pd.concat(l_df_knowledge_excluded)


def product_line_judge(df: pd.DataFrame, df_mst: pd.DataFrame = get_knowledges()):
    l_df_knowledge_excluded = []
    df_knowledge_mst = df_mst[["knowledge_id", "line_name"]].copy()

    for knowledge_id in df["knowledge_id"].unique():
        # 該当の knowledge_id に対応する df_knowledge を取得
        df_knowledge = df[df["knowledge_id"] == knowledge_id].copy()
        df_knowledge_tmp = df_knowledge.copy()  # 初期化

        # knowledge_id に対応する line_name を取得
        current_line_name = df_knowledge_mst[
            df_knowledge_mst["knowledge_id"] == knowledge_id
        ]["line_name"].values[0]

        # 他のすべての line_name を取得（current_line_name を除く）
        other_line_names = df_knowledge_mst[
            df_knowledge_mst["line_name"] != current_line_name
        ]["line_name"].unique()

        # name列に他のline_nameが含まれているか確認し、それを除外
        df_knowledge_tmp = df_knowledge_tmp[
            ~df_knowledge_tmp["name"].apply(
                lambda name: any(line in name for line in other_line_names)
            )
        ]

        l_df_knowledge_excluded.append(df_knowledge_tmp)

    return pd.concat(l_df_knowledge_excluded)


# 商品名に基づくフィルタリング処理を行う関数
def filter_by_name(df, filter_value):
    # 商品名からスペースを取り除いて、フィルターに一致するレコードだけを残す
    return df[df["name"].str.replace(" ", "").str.contains(filter_value)].copy()


# 全てのknowledge_idに対してフィルタリング処理を実行する関数
def filter_bulk_by_knowledge(df_bulk):
    # get_knowledges 関数を使用して知識情報を取得
    df_knowledges = get_knowledges()[
        ["knowledge_id", "knowledge_name", "line_name"]
    ].copy()

    # 結果を格納するリストを初期化
    filtered_dfs = []

    # df_bulk に含まれるすべての knowledge_id でループ
    for knowledge_id in df_bulk["knowledge_id"].unique():
        # 指定された knowledge_id に対応する line_name と knowledge_name を取得
        knowledge_info = df_knowledges[df_knowledges["knowledge_id"] == knowledge_id]
        if knowledge_info.empty:
            continue  # 該当する知識情報がない場合はスキップ

        line_name = knowledge_info["line_name"].values[0].replace(" ", "")
        knowledge_name = knowledge_info["knowledge_name"].values[0].replace(" ", "")

        # 対象のデータを一時的にコピー
        df_bulk_tmp = df_bulk[df_bulk["knowledge_id"] == knowledge_id].copy()

        print(
            f"Processing knowledge_id: {knowledge_id}, initial shape: {df_bulk_tmp.shape}"
        )

        # line_name でフィルタリング
        df_bulk_tmp = filter_by_name(df_bulk_tmp, line_name)
        print(f"After line filter, shape: {df_bulk_tmp.shape}")

        # knowledge_name でフィルタリング
        df_bulk_tmp = filter_by_name(df_bulk_tmp, knowledge_name)
        print(f"After knowledge filter, shape: {df_bulk_tmp.shape}")

        # フィルタリング結果をリストに追加
        filtered_dfs.append(df_bulk_tmp)

    # 結果を1つのデータフレームに統合
    if filtered_dfs:
        return pd.concat(filtered_dfs, ignore_index=True)
        print("Final combined shape:", df_filtered_bulk.shape)
    else:
        return pd.DataFrame()  # データがない場合の空データフレーム
        print("No matching records found")
