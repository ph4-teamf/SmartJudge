import pandas as pd
import os

csv_path = os.path.join(os.path.dirname(__file__),
                        '40_Fukuoka Prefecture_20211_20223.csv')
df = pd.read_csv(csv_path)

# 出力するファイル
output_data = "output_data.csv"
# データの行数とカラム数の確認
# df.shape

# 「種類」フィールドの値が「宅地(土地と建物)」のデータのみ使用
df = df[df['種類'] == "宅地(土地と建物)"]

# 「地域」フィールドの値が「住宅地」データのみ使用
df = df[df['地域'] == "住宅地"]

# 「用途」フィールドの値が「住宅」を含むデータのみ使用
df = df[df['用途'].str.contains("住宅") == True]

# 欠損値除去
df = df.dropna(subset=["最寄駅：距離（分）", "面積（㎡）", "建築年",
               "地区名", "延床面積（㎡）", "取引価格（総額）"])
# df = df.dropna(subset=["建築年"])
# 連番付与
serial_num = pd.RangeIndex(start=1, stop=len(df.index) + 1, step=1)
df["ID"] = serial_num

# 不要なフィールドを削除
df = df[["最寄駅：距離（分）", "面積（㎡）", "延床面積（㎡）", "建築年", "地区名", "取引価格（総額）", "市区町村コード"]]

# 最寄駅：距離（分）の不正な値を置換
df = df.replace({'最寄駅：距離（分）': {"1H?1H30": 60}})
df = df.replace({'最寄駅：距離（分）': {"1H30?2H": 90}})
df = df.replace({'最寄駅：距離（分）': {"2H?": 120}})
df = df.replace({'最寄駅：距離（分）': {"30分?60分": 30}})

# 建築年の不正な値を置換
df = df.replace({'建築年': {"戦前": "昭和15年"}})

# 建築年の元号表記を築年数に変換
df['年号'] = df['建築年'].str[:2]
df['和暦_年'] = df['建築年'].str[2:].str.replace('年', '').astype(int)
df.loc[df['年号'] == '昭和', '築年数'] = 2023 - (df['和暦_年'] + 1925)
df.loc[df['年号'] == '平成', '築年数'] = 2023 - (df['和暦_年'] + 1988)
df.loc[df['年号'] == '令和', '築年数'] = 2023 - (df['和暦_年'] + 2019)

# 外れ値の除去（取引価格（総額）が1億50000万円より大きいレコードは削除）
df = df[df['取引価格（総額）'] <= 150000000]

# 面積が2000㎡以上のものを除去する
df = df[df['面積（㎡）'] != '2000㎡以上']
df = df[df['延床面積（㎡）'] != '2000㎡以上']

# データの加工結果を出力
df.to_csv(os.path.join(os.path.dirname(__file__), output_data))
# print(df.head(10))
