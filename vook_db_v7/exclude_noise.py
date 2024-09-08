import pandas as pd

from vook_db_v7.rds_handler import get_knowledges

# product_noise_judge.csvを読み込む
df_product_noise_judge = pd.read_csv("./data/input/product_noise_judge.csv")


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
                [noise not in name for name in df_knowledge_tmp["name"]]
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
