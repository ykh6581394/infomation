# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 15:08:06 2024

@author: 유국현
"""

import pandas as pd
import streamlit as st

root = "./information.csv"
prj_root = "./prj.csv"

st.title("Search Prone")

tab1, tab2 = st.tabs(["Info", "Project"])


with tab1:
    name = st.text_input("이름을 입력하세요!")
   
    data = pd.read_csv(root,encoding="euc-kr")

    unit = data[data["성명"]==name]
    
    if st.button("Search"):
        with st.spinner('Wait for it...'):
            try:
                df = pd.DataFrame(list(unit.iloc[0]),index=unit.columns,columns=["Info"])
                st.table(df)
        
            except:
                st.text("No Entry, Enter Again")



with tab2:
    name = st.text_input("이름 또는 프로젝트 키워드를 입력하세요!")

    dt = pd.read_csv(prj_root,encoding="euc-kr")
    name_list = list(dt["성명"])
    prj_list  = dt["프로젝트명"]
    
    
    if st.button("Search Project"):
        try:
            if name in name_list:
                dt_new = dt[dt["성명"]==name]
                dt_final = dt_new[["프로젝트명","고객사", "역할","사업기간","상태"]].sort_values(by="사업기간")
            
            else:
                keyword = name
                
                key_in = []
                for i in range(len(dt)):
                    unit = dt.iloc[i]
                    if keyword in unit["프로젝트명"]:
                        key_in.append(True)
                    else:
                        key_in.append(False)
                        
                dt["tag"] = key_in
                
                dt_key = dt[dt["tag"]==True]
                dt_final = dt_key[["성명","프로젝트명","고객사", "역할","사업기간","상태"]].sort_values(by="프로젝트명")
            
            st.table(dt_final.reset_index(drop=True))
        except:
            st.text("No Entry, Enter Again")
    
    





