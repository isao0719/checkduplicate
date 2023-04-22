import streamlit as st
import pandas as pd
import glob

st.title("CSV Uploader")  # タイトル
uploaded_files = st.file_uploader(
    "Choose CSV files", type="csv", accept_multiple_files=True
)  # 場所を作る
if st.button("push"):  # ボタン
    if len(uploaded_files) >= 1:
        list1 = [pd.read_csv(f) for f in uploaded_files]

        result = pd.concat(list1)
        duplicated_phama = result[result.duplicated("医薬品名", keep=False)]
        name = duplicated_phama["医薬品名"].unique()
        for i in name:
            p = duplicated_phama[duplicated_phama["医薬品名"] == i]
            st.write(p)  # printの代わり
