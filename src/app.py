# ライブラリの読み込み
import os
import time
import datetime
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def main():

    select_municipalities = st.selectbox("市区町村", ("北九州市戸畑区", "北九州市若松区", "北九州市小倉南区",
                                                  "北九州市小倉北区", "北九州市八幡西区", "北九州市八幡東区", "北九州市門司区",
                                                  "福岡市城南区", "福岡市西区", "福岡市早良区", "福岡市中央区", "福岡市東区", "福岡市南区", "福岡市博多区"))
    st.write("You selected:", select_municipalities)
    st.markdown("---")

    Area = st.slider("面積(㎡)", 0, 1999, 1000)
    st.write("You selected:", Area)
    st.markdown("---")

    Age = st.slider("築年数", 0, 100, 50)
    st.write("You selected:", Age)
    st.markdown("---")

    # select_Age = st.selectbox("築年数", ("1946年", "1946年", "1947年", "1950年", "1951年", "1952年", "1953年",
    #                                   "1954年", "1955年", "1956年", "1957年", "1958年", "1959年", "1960年",
    #                                   "1961年", "1962年", "1963年", "1964年", "1965年", "1966年", "1967年"
    #                                   , "1968年", "1969年", "1970年", "1971年", "1972年", "1973年", "1974年"
    #                                   , "1975年", "1976年", "1977年", "1978年", "1979年", "1980年", "1981年"
    #                                   , "1982年", "1983年", "1984年", "1985年", "1986年", "1987年", "1988年"
    #                                   , "1989年", "1990年", "1991年", "1992年", "1993年", "1994年", "1995年"
    #                                   , "1996年", "1997年", "1998年", "1999年", "2000年", "2001年", "2002年"
    #                                   , "2003年", "2004年", "2005年", "2006年", "2007年", "2008年", "2009年"
    #                                   , "2010年", "2011年", "2012年", "2013年", "2014年", "2015年", "2016年"
    #                                   , "2017年", "2018年", "2019年", "2020年", "2021年", "2022年"))
    # st.write("You selected:", select_Age)
    # st.markdown("---")

    NearestStation = st.slider("最寄り駅までの距離(分)", 1, 120, 60)
    st.write("You selected:", NearestStation)
    st.markdown("---")

    # TransactionPrice = st.slider("取引価格", 50000, 149999999, 70000000)
    # st.write("You selected:", TransactionPrice)
    # st.markdown("---")

    TransactionPrice = st.number_input(label="取引価格",
                                       value=42,
                                       )
    st.write("You selected:", TransactionPrice)
    st.markdown("---")

    TotalFloorArea = st.slider("延床面積(㎡)", 1, 1600, 800)
    st.write("You selected:", TotalFloorArea)
    st.markdown("---")


if __name__ == '__main__':
    main()
