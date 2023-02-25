
#ライブラリの読み込み
import os
import time
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder


#タイトル
st.title("機械学習アプリ")
st.write("streamlitで実装")

# 以下をサイドバーに表示
st.sidebar.markdown("### 機械学習に用いるcsvファイルを入力してください")
#ファイルアップロード
uploaded_files = st.sidebar.file_uploader("Choose a CSV file", accept_multiple_files= False)

#ファイルがアップロードされたら以下が実行される
if uploaded_files:
    df = pd.read_csv(uploaded_files)
    df_columns = df.columns
    
# 「種類」フィールドの値が「宅地(土地と建物)」のデータのみ使用
df = df[df['種類'] == "宅地(土地と建物)"]

# 「地域」フィールドの値が「住宅地」データのみ使用
df = df[df['地域'] == "住宅地"]

# 「用途」フィールドの値が「住宅」を含むデータのみ使用
df = df[df['用途'].str.contains("住宅") == True]

# 欠損値除去
df = df.dropna(subset=["最寄駅：距離（分）", "延床面積（㎡）", "建築年", "建物の構造", '地域', '用途'])

# 連番付与
serial_num = pd.RangeIndex(start=1, stop=len(df.index) + 1, step=1)
df["ID"] = serial_num

# 不要なフィールドを削除
df = df[["地域", "市区町村コード", "都道府県", "地区名", "坪単価", "面積（㎡）", "土地の形状",
         "間口", "用途", "今後の利用目的", "前面道路：方位", "前面道路：種類", "延床面積（㎡）", 
         "建物の構造", "取引価格（㎡単価）", "前面道路：幅員（ｍ）", "都市計画",
         "建ぺい率（％）", "容積率（％）", "取引時点", "改装", "取引の事情等"]]

# 最寄駅：距離（分）の不正な値を置換
df = df.replace({'最寄駅：距離（分）': {"1H?1H30": 60}})
df = df.replace({'最寄駅：距離（分）': {"1H30?2H": 90}})
df = df.replace({'最寄駅：距離（分）': {"2H?": 120}})
df = df.replace({'最寄駅：距離（分）': {"30分?60分": 30}})

# 建築年の不正な値を置換
df = df.replace({'建築年': {"戦前": "昭和15年"}})

# 建築年の元号表記を築年数に変換
df['年号'] = df['建築年'].str[:2]
df['和暦_年'] = df['建築年'].str[2:].str.replace('年','').astype(int)
df.loc[df['年号']=='昭和','築年数'] = 2021 - (df['和暦_年'] + 1925)
df.loc[df['年号']=='平成','築年数'] = 2021 - (df['和暦_年'] + 1988)
df.loc[df['年号']=='令和','築年数'] = 2021 - (df['和暦_年'] + 2019)

# 外れ値の除去（取引価格（総額）が1億50000万円より大きいレコードは削除）
df = df[df['取引価格（総額）'] <= 150000000]

# データの加工結果を出力
df.to_csv("output_data.csv")
