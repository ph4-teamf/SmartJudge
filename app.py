
#ライブラリの読み込み
import os
import time
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import Judge
import ML


def main():
    with st.sidebar:
        page = st.selectbox('', ('Judge', 'ML'), )

    if page == 'Judge':
        Judge.render()
    elif page == 'ML':
        ML.render()


if __name__ == '__main__':
    main()
