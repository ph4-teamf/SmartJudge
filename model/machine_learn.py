import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from datashaping import df
import os
import pickle

output_data = "output_data2.csv"
# 出力変数
t = df["取引価格（総額）"]

# 学習に必要なカラムを抽出
x = df.iloc[:, [0, 1, 2, 6, 9]]
# print(x.head())

# object 型のカラムをダミー変数化
# x = pd.get_dummies(x)
# print(x.head())
# 訓練データと検証データに分ける
x_train, x_val, t_train, t_val = train_test_split(
    x, t, test_size=0.3, random_state=0)

# x_train.to_csv(os.path.join(os.path.dirname(__file__), output_data))

# 線形回帰モデル
model = LinearRegression()

model.fit(x_train, t_train)

# print(model.score(x_val, t_val))

# モデルを保存する
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))

# 保存したモデルをロードする
# loaded_model = pickle.load(open(filename, 'rb'))
# result = loaded_model.score(x_val, t_val)
# print(result)
