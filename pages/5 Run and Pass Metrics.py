# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 15:14:39 2023

@author: edwar
"""

import streamlit as st
import pandas as pd

#Read in data from Github
url = 'https://raw.githubusercontent.com/hankshackleford/KorbelFantasyApp/main/run_pass.csv'
df = pd.read_csv(url)
print(df)


st.set_page_config(
    page_title="Run/Pass Metrics",
    page_icon="🏈",
    layout="wide"
)
st.header("Run/Pass Metrics for NFL Teams, 2022")


#Data Editor
st.data_editor(
    df,
    column_config={
        "Run %": st.column_config.ProgressColumn(
            "Run %",
            format="%6.2f"),     
        "Pass %": st.column_config.ProgressColumn(
            "Pass %",
            format="%6.2f"),       
        },
    hide_index=True,
    width=1500,
    height=1500
)