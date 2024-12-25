import numpy as np
import pandas as pd


def generate_mock_data_actual(num_rows=30):
    """
    テストデータを生成する関数。

    この関数は、指定された行数のモックデータを生成し、データフレームとして返します。
    主に、`df_bulk`というデータが作成された後の実装修正時に使用されます。
    本関数に反映されているデータは仮のデータです。
    ・参考までに2024/12/24 16:32時点でcheck_df_bulk_interface.ipynbを実行して作成されました。

    Args:
        num_rows (int): 生成する行数。デフォルトは30行。実装修正の規模に合わせて行数を調整できます。

    Returns:
        pd.DataFrame:

    使用例:
      - 修正点に応じたテストデータを簡単に作成するために利用します。
      - 修正点が発生した場合はテスト要件、ケースを言語化し、そのケースを確認できるようなdf_bulkをこの関数内部の実装を修正することで作成します。
      - 作成方法はtest_utils.pyの末尾に__<issue_no>_<test_case_no>を付与しファイル自体をコピーした後、内部の実装を修正してください。
    """
    data = {
        "id": [np.nan for _ in range(num_rows)],
        "name": [
            "【中古】リーバイス Levi's 70s 501 66前期 BIG EビッグE デニムパンツ 青 デニム 無地 ブルー 103MB-103",
            "【中古】Lee｜リー デニム ジャケット 101-J 50年代後期 ヴィンテージ ブルー サイズ：42 / アメカジ【f93】",
            "【中古】Levi’s◆70s/ベルボトム/ボタン裏39/ブーツカットパンツ/IDG/646-0217/ダメージ有【メンズウェア】",
            "古着 00'S パタゴニア Patagonia ORGANIC COTTON オーガニックコットン 11339F7 ダック地ショーツ ショートパンツ メンズw36相当 /eaa485969 【中古】 【240903】",
            "【中古】Levi’s◆60s/4th/トラッカージャケット/BIGE/ボタン裏52/Gジャン/コットン/IDG/70505//【メンズウェア】",
            "【中古】コンバース CONVERSE CANVAS ALL STAR HI キャンバスオールスターハイ スニーカー US8 26.5cm 紫 パープル /KH メンズ 【ベクトル 古着】 241106",
            "古着 90'S チャンピオン Champion REVERSE WEAVE リバースウィーブ 刺繍タグ ロゴスウェット トレーナー USA製 メンズM ヴィンテージ /eaa380932 【中古】 【231201】 ss2412_30",
            "【中古】Levi’s◆70s/501/66BigE/足長/ボタン裏6/シングル/赤耳/デニムパンツ/デニム/インディゴ【メンズウェア】",
            "【中古】Levi’s◆501/66後期/チェーンステッチ/IDG///【メンズウェア】",
            "【中古】Levi’s◆550/カットオフ/ボトム/34/ブラックデニム【メンズウェア】",
            "90s USA製 ヴィンテージ リーバイス Levi's スタプレ 517 スラックス フレアパンツ 古着 ★ メンズ Lサイズ相当 ダークブラウン",
            "【中古】未使用品 リー LEE 44J カバーオール ロコジャケット LM5412-924 オフホワイト M メンズ 【ベクトル 古着】 241124",
            "Levi's リーバイス 70s 501 66前期 BigE 両面BigE 刻印6 フライボタン通常R 裾チェーンステッチ オリジナルレングス【中古】",
            "【中古】リーバイス Levis 501 ORIGINAL SELVEDGE DENIM メンズ W29/L32",
            "【中古】Levi’s◆ストレートパンツ/--/デニム/BLU/40505-0209【メンズウェア】",
            "【中古】Levi’s◆70s/42TALON/ボタン裏563/オレンジタブ/フレア/ブーツカットパンツ/34/6460217【メンズウェア】",
            "【送料無料】WACKO MARIA × CONVERSE ALL STAR ワコマリア コンバース オールスター【中古】【004】",
            "Levi's(リーバイス) サイズ:W32 40s VINTAGE 501XX 47モデル 革パッチ 片面タブ デニムパンツ インディゴ【中古】【程度C】【カラーブルー】【取扱店舗AWESOME原宿店】",
            "Levi's リーバイス デニム、ジーンズ パンツ Pants, Trousers Denim Pants, Jeans 35585-0019 551Z STRAIGHT ストレート ジーンズ デニムパンツ タグ付き【USED】【古着】【中古】10104658",
            "【中古】Levi’s◆ボトム/31/デニム/IDG/無地/リメイク【メンズウェア】",
            "古着 90'S リーバイス Levi's 70598-4891 特大パッチ デニムジャケット Gジャン カナダ製 メンズL ヴィンテージ /eaa453517 【中古】 【240609】",
            "【中古】Levi’s◆80s/501/66後期/赤耳/バレンシア工場/28/コットン/IDG/汚れ有/リペア有【メンズウェア】",
            "【12/23 大感謝祭 ポイント5倍!!】 16年製 パタゴニア バギーズ ショーツ メンズ M / 古着 PATAGONIA アウトドア ナイロン ショートパンツ スイムショーツ 短パン 水陸両用 青| 中古 バギーズショーツ ナイロンショーツ ナイロンパンツ サーフパンツ ハーフパンツ 半パン ワ",
            "LEVI'Sリーバイス PREMIUM 501 BIGE デニムパンツ w40 L32★SDP2924 ジーンズ ストレート ビッグE オーバーサイズ ビッグサイズ",
            "【中古】Levi’s◆ストレートパンツ/30/デニム/IDG/60s～70s/501/BIG E/後期/並行ステッチ/不均【メンズウェア】",
            "古着 90'S リーバイス Levi's 550 RELAXED FIT ブラックデニム テーパードデニムパンツ メンズw31相当 ヴィンテージ /eaa403447 【中古】 【241027】",
            "古着 90'S リーバイス Levi's 560 LOOSE FIT TAPERED LEG テーパードデニムパンツ USA製 メンズw35相当 ヴィンテージ /eaa503800 【中古】 【241121】",
            "未使用 Levi’s リーバイス 04511-2301 W27 米国製 MADE IN USA スリムフィット BIGEタブ デニムパンツ M12615",
            "【中古】Levi’s◆70s/646/リペア跡有/ブーツカットパンツ/32/デニム/IDG【メンズウェア】",
            "BIG E LVC",
        ],
        "url": [
            "https://hb.afl.rakuten.co.jp/hgc/g00tpkue.brn1qeb9.g00tpkue.brn1r3b3/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fkaitori-gekijo%2Frc_iti2vmepfolk_ralt%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fkaitori-gekijo%2Fi%2F10013668%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00qxgae.brn1qd0c.g00qxgae.brn1rd0a/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fotaichi%2F20166700476205%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fotaichi%2Fi%2F10531907%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00r3cee.brn1qd11.g00r3cee.brn1r0ee/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjumblestore%2F2320332329241%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjumblestore%2Fi%2F31004574%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00qhzfe.brn1q668.g00qhzfe.brn1rb64/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjam-ing%2Feaa485969%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjam-ing%2Fi%2F11385570%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00r3cee.brn1qd11.g00r3cee.brn1r0ee/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjumblestore%2F2329041972731%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjumblestore%2Fi%2F32831699%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00rsgoe.brn1q7ed.g00rsgoe.brn1r898/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fvectorpremium%2F081-102410250137%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fvectorpremium%2Fi%2F18215332%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00qhzfe.brn1q668.g00qhzfe.brn1rb64/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjam-ing%2Feaa380932%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjam-ing%2Fi%2F11309384%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00r3cee.brn1qd11.g00r3cee.brn1r0ee/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjumblestore%2F2319972409338%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjumblestore%2Fi%2F30440514%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00r3cee.brn1qd11.g00r3cee.brn1r0ee/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjumblestore%2F2325602208073%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjumblestore%2Fi%2F33912948%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00r3cee.brn1qd11.g00r3cee.brn1r0ee/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjumblestore%2F2337951825641%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjumblestore%2Fi%2F33936117%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00rgike.brn1q775.g00rgike.brn1re1d/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fkazzin%2F100023721%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fkazzin%2Fi%2F10394914%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00rsgoe.brn1q7ed.g00rsgoe.brn1r898/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fvectorpremium%2F051-202411240199%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fvectorpremium%2Fi%2F18233509%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://store.shopping.yahoo.co.jp/brand-life/3a04627nm0410xa10.html",
            "https://hb.afl.rakuten.co.jp/hgc/g00rbope.brn1q62a.g00rbope.brn1r58a/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fbazzstore%2F1134205184537%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fbazzstore%2Fi%2F11869573%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00r3cee.brn1qd11.g00r3cee.brn1r0ee/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjumblestore%2F2329005180196%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjumblestore%2Fi%2F33722881%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00r3cee.brn1qd11.g00r3cee.brn1r0ee/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjumblestore%2F2342131270067%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjumblestore%2Fi%2F32139196%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00r88je.brn1qf78.g00r88je.brn1r0d3/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fotaculture%2F7992-004%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fotaculture%2Fi%2F10075165%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00s6rie.brn1q032.g00s6rie.brn1rea7/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fbring-sg%2F2124k260006%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fbring-sg%2Fi%2F10746925%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00u1a6e.brn1qbd9.g00u1a6e.brn1r5ac/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fistitch-store%2F10104658%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fistitch-store%2Fi%2F10125514%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00r3cee.brn1qd11.g00r3cee.brn1r0ee/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjumblestore%2F2335341568413%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjumblestore%2Fi%2F34032795%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00qhzfe.brn1q668.g00qhzfe.brn1rb64/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjam-ing%2Feaa453517%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjam-ing%2Fi%2F11360403%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00r3cee.brn1qd11.g00r3cee.brn1r0ee/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjumblestore%2F2326824056596%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjumblestore%2Fi%2F33209732%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00r9nge.brn1qdbe.g00r9nge.brn1rcd2/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fauc-grab%2Fs-jyd01y24n12%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fauc-grab%2Fi%2F10136987%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://store.shopping.yahoo.co.jp/sixpacjoe/240709-5.html",
            "https://hb.afl.rakuten.co.jp/hgc/g00r3cee.brn1qd11.g00r3cee.brn1r0ee/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjumblestore%2F2319571864170%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjumblestore%2Fi%2F31148678%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00qhzfe.brn1q668.g00qhzfe.brn1rb64/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjam-ing%2Feaa403447%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjam-ing%2Fi%2F11402097%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00qhzfe.brn1q668.g00qhzfe.brn1rb64/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjam-ing%2Feaa503800%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjam-ing%2Fi%2F11407662%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://store.shopping.yahoo.co.jp/reuseshoplantern/m12615.html",
            "https://hb.afl.rakuten.co.jp/hgc/g00r3cee.brn1qd11.g00r3cee.brn1r0ee/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjumblestore%2F2340780519858%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjumblestore%2Fi%2F33923539%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://google.com",
        ],
        "price": [
            67980,
            98000,
            18260,
            8360,
            31460,
            10800,
            18920,
            55660,
            39160,
            8360,
            8800,
            9700,
            159280,
            8239,
            7260,
            22660,
            13000,
            132000,
            7920,
            7260,
            19690,
            14960,
            6100,
            6900,
            99660,
            14960,
            12760,
            3300,
            14960,
            999999,
        ],
        "knowledge_id": [
            5,
            107,
            134,
            31,
            38,
            131,
            50,
            10,
            28,
            102,
            148,
            149,
            10,
            102,
            102,
            134,
            131,
            11,
            99,
            135,
            101,
            37,
            31,
            10,
            10,
            43,
            28,
            10,
            134,
            5,
        ],
        "platform_id": [
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            2,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            2,
            1,
            1,
            1,
            2,
            1,
            1,
        ],
        "size_id": [999 for _ in range(num_rows)],
        "created_at": [
            "2024-12-24 15:41:38.556295",
            "2024-12-24 15:46:38.781377",
            "2024-12-24 15:47:55.986734",
            "2024-12-24 15:42:42.617846",
            "2024-12-24 15:43:20.847997",
            "2024-12-24 15:47:38.583199",
            "2024-12-24 15:43:51.166849",
            "2024-12-24 15:41:52.554069",
            "2024-12-24 15:42:26.195244",
            "2024-12-24 15:45:56.554437",
            "2024-12-24 15:49:07.619465",
            "2024-12-24 15:49:09.957529",
            "2024-12-24 15:50:05.327065",
            "2024-12-24 15:45:56.554437",
            "2024-12-24 15:45:56.554437",
            "2024-12-24 15:47:55.986734",
            "2024-12-24 15:47:38.583199",
            "2024-12-24 15:41:54.836419",
            "2024-12-24 15:45:30.840984",
            "2024-12-24 15:48:06.410209",
            "2024-12-24 15:45:44.834494",
            "2024-12-24 15:43:15.069716",
            "2024-12-24 15:42:42.617846",
            "2024-12-24 15:50:05.756203",
            "2024-12-24 15:41:52.554069",
            "2024-12-24 15:43:37.054258",
            "2024-12-24 15:42:26.195244",
            "2024-12-24 15:50:06.047126",
            "2024-12-24 15:47:55.986734",
            "2024-12-24 15:45:56.554437",
        ],
        "updated_at": [
            "2024-12-24 15:41:38.556295",
            "2024-12-24 15:46:38.781377",
            "2024-12-24 15:47:55.986734",
            "2024-12-24 15:42:42.617846",
            "2024-12-24 15:43:20.847997",
            "2024-12-24 15:47:38.583199",
            "2024-12-24 15:43:51.166849",
            "2024-12-24 15:41:52.554069",
            "2024-12-24 15:42:26.195244",
            "2024-12-24 15:45:56.554437",
            "2024-12-24 15:49:07.619465",
            "2024-12-24 15:49:09.957529",
            "2024-12-24 15:50:05.327073",
            "2024-12-24 15:45:56.554437",
            "2024-12-24 15:45:56.554437",
            "2024-12-24 15:47:55.986734",
            "2024-12-24 15:47:38.583199",
            "2024-12-24 15:41:54.836419",
            "2024-12-24 15:45:30.840984",
            "2024-12-24 15:48:06.410209",
            "2024-12-24 15:45:44.834494",
            "2024-12-24 15:43:15.069716",
            "2024-12-24 15:42:42.617846",
            "2024-12-24 15:50:05.756212",
            "2024-12-24 15:41:52.554069",
            "2024-12-24 15:43:37.054258",
            "2024-12-24 15:42:26.195244",
            "2024-12-24 15:50:06.047129",
            "2024-12-24 15:47:55.986734",
            "2024-12-24 15:45:56.554437",
        ],
    }

    # ランダムなモックデータの生成
    df = pd.DataFrame(data)

    return df


def generate_mock_data_expected(num_rows=30):
    """
    テストデータを生成する関数。

    この関数は、指定された行数のモックデータを生成し、データフレームとして返します。
    主に、`df_bulk`というデータが作成された後の実装修正時に使用されます。
    本関数に反映されているデータは仮のデータです。
    ・参考までに2024/12/24 16:32時点でcheck_df_bulk_interface.ipynbを実行して作成されました。

    Args:
        num_rows (int): 生成する行数。デフォルトは30行。実装修正の規模に合わせて行数を調整できます。

    Returns:
        pd.DataFrame:

    使用例:
      - 修正点に応じたテストデータを簡単に作成するために利用します。
      - 修正点が発生した場合はテスト要件、ケースを言語化し、そのケースを確認できるようなdf_bulkをこの関数内部の実装を修正することで作成します。
      - 作成方法はtest_utils.pyの末尾に__<issue_no>_<test_case_no>を付与しファイル自体をコピーした後、内部の実装を修正してください。
    """
    data = {
        "id": [np.nan for _ in range(num_rows - 4)],
        "name": [
            "【中古】リーバイス Levi's 70s 501 66前期 BIG EビッグE デニムパンツ 青 デニム 無地 ブルー 103MB-103",
            "【中古】Lee｜リー デニム ジャケット 101-J 50年代後期 ヴィンテージ ブルー サイズ：42 / アメカジ【f93】",
            "【中古】Levi’s◆70s/ベルボトム/ボタン裏39/ブーツカットパンツ/IDG/646-0217/ダメージ有【メンズウェア】",
            "古着 00'S パタゴニア Patagonia ORGANIC COTTON オーガニックコットン 11339F7 ダック地ショーツ ショートパンツ メンズw36相当 /eaa485969 【中古】 【240903】",
            "【中古】Levi’s◆60s/4th/トラッカージャケット/BIGE/ボタン裏52/Gジャン/コットン/IDG/70505//【メンズウェア】",
            "【中古】コンバース CONVERSE CANVAS ALL STAR HI キャンバスオールスターハイ スニーカー US8 26.5cm 紫 パープル /KH メンズ 【ベクトル 古着】 241106",
            "古着 90'S チャンピオン Champion REVERSE WEAVE リバースウィーブ 刺繍タグ ロゴスウェット トレーナー USA製 メンズM ヴィンテージ /eaa380932 【中古】 【231201】 ss2412_30",
            "【中古】Levi’s◆70s/501/66BigE/足長/ボタン裏6/シングル/赤耳/デニムパンツ/デニム/インディゴ【メンズウェア】",
            "【中古】Levi’s◆501/66後期/チェーンステッチ/IDG///【メンズウェア】",
            "90s USA製 ヴィンテージ リーバイス Levi's スタプレ 517 スラックス フレアパンツ 古着 ★ メンズ Lサイズ相当 ダークブラウン",
            "【中古】未使用品 リー LEE 44J カバーオール ロコジャケット LM5412-924 オフホワイト M メンズ 【ベクトル 古着】 241124",
            "Levi's リーバイス 70s 501 66前期 BigE 両面BigE 刻印6 フライボタン通常R 裾チェーンステッチ オリジナルレングス【中古】",
            "【中古】リーバイス Levis 501 ORIGINAL SELVEDGE DENIM メンズ W29/L32",
            "【中古】Levi’s◆ストレートパンツ/--/デニム/BLU/40505-0209【メンズウェア】",
            "【中古】Levi’s◆70s/42TALON/ボタン裏563/オレンジタブ/フレア/ブーツカットパンツ/34/6460217【メンズウェア】",
            "【送料無料】WACKO MARIA × CONVERSE ALL STAR ワコマリア コンバース オールスター【中古】【004】",
            "Levi's(リーバイス) サイズ:W32 40s VINTAGE 501XX 47モデル 革パッチ 片面タブ デニムパンツ インディゴ【中古】【程度C】【カラーブルー】【取扱店舗AWESOME原宿店】",
            "Levi's リーバイス デニム、ジーンズ パンツ Pants, Trousers Denim Pants, Jeans 35585-0019 551Z STRAIGHT ストレート ジーンズ デニムパンツ タグ付き【USED】【古着】【中古】10104658",
            "【中古】Levi’s◆ボトム/31/デニム/IDG/無地/リメイク【メンズウェア】",
            "古着 90'S リーバイス Levi's 70598-4891 特大パッチ デニムジャケット Gジャン カナダ製 メンズL ヴィンテージ /eaa453517 【中古】 【240609】",
            "【12/23 大感謝祭 ポイント5倍!!】 16年製 パタゴニア バギーズ ショーツ メンズ M / 古着 PATAGONIA アウトドア ナイロン ショートパンツ スイムショーツ 短パン 水陸両用 青| 中古 バギーズショーツ ナイロンショーツ ナイロンパンツ サーフパンツ ハーフパンツ 半パン ワ",
            "【中古】Levi’s◆ストレートパンツ/30/デニム/IDG/60s～70s/501/BIG E/後期/並行ステッチ/不均【メンズウェア】",
            "古着 90'S リーバイス Levi's 550 RELAXED FIT ブラックデニム テーパードデニムパンツ メンズw31相当 ヴィンテージ /eaa403447 【中古】 【241027】",
            "古着 90'S リーバイス Levi's 560 LOOSE FIT TAPERED LEG テーパードデニムパンツ USA製 メンズw35相当 ヴィンテージ /eaa503800 【中古】 【241121】",
            "未使用 Levi’s リーバイス 04511-2301 W27 米国製 MADE IN USA スリムフィット BIGEタブ デニムパンツ M12615",
            "【中古】Levi’s◆70s/646/リペア跡有/ブーツカットパンツ/32/デニム/IDG【メンズウェア】",
        ],
        "url": [
            "https://hb.afl.rakuten.co.jp/hgc/g00tpkue.brn1qeb9.g00tpkue.brn1r3b3/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fkaitori-gekijo%2Frc_iti2vmepfolk_ralt%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fkaitori-gekijo%2Fi%2F10013668%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00qxgae.brn1qd0c.g00qxgae.brn1rd0a/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fotaichi%2F20166700476205%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fotaichi%2Fi%2F10531907%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00r3cee.brn1qd11.g00r3cee.brn1r0ee/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjumblestore%2F2320332329241%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjumblestore%2Fi%2F31004574%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00qhzfe.brn1q668.g00qhzfe.brn1rb64/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjam-ing%2Feaa485969%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjam-ing%2Fi%2F11385570%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00r3cee.brn1qd11.g00r3cee.brn1r0ee/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjumblestore%2F2329041972731%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjumblestore%2Fi%2F32831699%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00rsgoe.brn1q7ed.g00rsgoe.brn1r898/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fvectorpremium%2F081-102410250137%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fvectorpremium%2Fi%2F18215332%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00qhzfe.brn1q668.g00qhzfe.brn1rb64/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjam-ing%2Feaa380932%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjam-ing%2Fi%2F11309384%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00r3cee.brn1qd11.g00r3cee.brn1r0ee/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjumblestore%2F2319972409338%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjumblestore%2Fi%2F30440514%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00r3cee.brn1qd11.g00r3cee.brn1r0ee/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjumblestore%2F2325602208073%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjumblestore%2Fi%2F33912948%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00rgike.brn1q775.g00rgike.brn1re1d/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fkazzin%2F100023721%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fkazzin%2Fi%2F10394914%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00rsgoe.brn1q7ed.g00rsgoe.brn1r898/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fvectorpremium%2F051-202411240199%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fvectorpremium%2Fi%2F18233509%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://store.shopping.yahoo.co.jp/brand-life/3a04627nm0410xa10.html",
            "https://hb.afl.rakuten.co.jp/hgc/g00rbope.brn1q62a.g00rbope.brn1r58a/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fbazzstore%2F1134205184537%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fbazzstore%2Fi%2F11869573%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00r3cee.brn1qd11.g00r3cee.brn1r0ee/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjumblestore%2F2329005180196%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjumblestore%2Fi%2F33722881%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00r3cee.brn1qd11.g00r3cee.brn1r0ee/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjumblestore%2F2342131270067%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjumblestore%2Fi%2F32139196%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00r88je.brn1qf78.g00r88je.brn1r0d3/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fotaculture%2F7992-004%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fotaculture%2Fi%2F10075165%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00s6rie.brn1q032.g00s6rie.brn1rea7/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fbring-sg%2F2124k260006%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fbring-sg%2Fi%2F10746925%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00u1a6e.brn1qbd9.g00u1a6e.brn1r5ac/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fistitch-store%2F10104658%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fistitch-store%2Fi%2F10125514%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00r3cee.brn1qd11.g00r3cee.brn1r0ee/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjumblestore%2F2335341568413%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjumblestore%2Fi%2F34032795%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00qhzfe.brn1q668.g00qhzfe.brn1rb64/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjam-ing%2Feaa453517%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjam-ing%2Fi%2F11360403%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00r9nge.brn1qdbe.g00r9nge.brn1rcd2/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fauc-grab%2Fs-jyd01y24n12%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fauc-grab%2Fi%2F10136987%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00r3cee.brn1qd11.g00r3cee.brn1r0ee/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjumblestore%2F2319571864170%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjumblestore%2Fi%2F31148678%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00qhzfe.brn1q668.g00qhzfe.brn1rb64/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjam-ing%2Feaa403447%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjam-ing%2Fi%2F11402097%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://hb.afl.rakuten.co.jp/hgc/g00qhzfe.brn1q668.g00qhzfe.brn1rb64/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjam-ing%2Feaa503800%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjam-ing%2Fi%2F11407662%2F&rafcid=wsc_i_is_1040242227042771333",
            "https://store.shopping.yahoo.co.jp/reuseshoplantern/m12615.html",
            "https://hb.afl.rakuten.co.jp/hgc/g00r3cee.brn1qd11.g00r3cee.brn1r0ee/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjumblestore%2F2340780519858%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Fjumblestore%2Fi%2F33923539%2F&rafcid=wsc_i_is_1040242227042771333",
        ],
        "price": [
            67980,
            98000,
            18260,
            8360,
            31460,
            10800,
            18920,
            55660,
            39160,
            8800,
            9700,
            159280,
            8239,
            7260,
            22660,
            13000,
            132000,
            7920,
            7260,
            19690,
            6100,
            99660,
            14960,
            12760,
            3300,
            14960,
        ],
        "knowledge_id": [
            5,
            107,
            134,
            31,
            38,
            131,
            50,
            10,
            28,
            148,
            149,
            10,
            102,
            102,
            134,
            131,
            11,
            99,
            135,
            101,
            31,
            10,
            43,
            28,
            10,
            134,
        ],
        "platform_id": [
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            2,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            2,
            1,
        ],
        "size_id": [999 for _ in range(num_rows - 4)],
        "created_at": [
            "2024-12-24 15:41:38.556295",
            "2024-12-24 15:46:38.781377",
            "2024-12-24 15:47:55.986734",
            "2024-12-24 15:42:42.617846",
            "2024-12-24 15:43:20.847997",
            "2024-12-24 15:47:38.583199",
            "2024-12-24 15:43:51.166849",
            "2024-12-24 15:41:52.554069",
            "2024-12-24 15:42:26.195244",
            "2024-12-24 15:49:07.619465",
            "2024-12-24 15:49:09.957529",
            "2024-12-24 15:50:05.327065",
            "2024-12-24 15:45:56.554437",
            "2024-12-24 15:45:56.554437",
            "2024-12-24 15:47:55.986734",
            "2024-12-24 15:47:38.583199",
            "2024-12-24 15:41:54.836419",
            "2024-12-24 15:45:30.840984",
            "2024-12-24 15:48:06.410209",
            "2024-12-24 15:45:44.834494",
            "2024-12-24 15:42:42.617846",
            "2024-12-24 15:41:52.554069",
            "2024-12-24 15:43:37.054258",
            "2024-12-24 15:42:26.195244",
            "2024-12-24 15:50:06.047126",
            "2024-12-24 15:47:55.986734",
        ],
        "updated_at": [
            "2024-12-24 15:41:38.556295",
            "2024-12-24 15:46:38.781377",
            "2024-12-24 15:47:55.986734",
            "2024-12-24 15:42:42.617846",
            "2024-12-24 15:43:20.847997",
            "2024-12-24 15:47:38.583199",
            "2024-12-24 15:43:51.166849",
            "2024-12-24 15:41:52.554069",
            "2024-12-24 15:42:26.195244",
            "2024-12-24 15:49:07.619465",
            "2024-12-24 15:49:09.957529",
            "2024-12-24 15:50:05.327073",
            "2024-12-24 15:45:56.554437",
            "2024-12-24 15:45:56.554437",
            "2024-12-24 15:47:55.986734",
            "2024-12-24 15:47:38.583199",
            "2024-12-24 15:41:54.836419",
            "2024-12-24 15:45:30.840984",
            "2024-12-24 15:48:06.410209",
            "2024-12-24 15:45:44.834494",
            "2024-12-24 15:42:42.617846",
            "2024-12-24 15:41:52.554069",
            "2024-12-24 15:43:37.054258",
            "2024-12-24 15:42:26.195244",
            "2024-12-24 15:50:06.047129",
            "2024-12-24 15:47:55.986734",
        ],
    }

    # ランダムなモックデータの生成
    df = pd.DataFrame(data)

    return df
