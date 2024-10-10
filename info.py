# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 15:08:06 2024

@author: 유국현
"""

import pandas as pd
import streamlit as st

root = "./information.csv"


st.title("Search Prone")

tab1, tab2 = st.tabs(["Info", "Project"])


with tab1:
    name = st.text_input("이름을 입력하세요!")
   
    data = pd.read_csv(root,encoding="euc-kr")

    unit = data[data["성명"]==name]
    
    if st.button("Search"):
        with st.spinner('Wait for it...'):
            df = pd.DataFrame(list(unit.iloc[0]),index=unit.columns,columns=["Info"])
            st.table(df)
        









