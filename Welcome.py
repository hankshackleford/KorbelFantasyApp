# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 15:19:37 2023

@author: edwar
"""

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Korbel Fantasy League",
    page_icon="🏈",
)

st.write("# Welcome to the Official App of the Korbel Fantasy League.")
st.text('Select a page from the sidebar to get started.')


st.sidebar.success("Select a page above.")

#Read in data from Github
url = 'https://raw.githubusercontent.com/hankshackleford/KorbelFantasyApp/main/FF23_for_github.csv'
df = pd.read_csv(url)
print(df)

df['GP'] = df['GP'].fillna(0)
df['GP'] = df['GP'].astype('int')

#setting palette
colors=['#1A8A41','#521052']



scatter = px.scatter(df.query("Year==2022"), x="Total Points", y="Draft Value",
	         size="GP", 
             color="POS",
                 hover_name="PLAYER", size_max=17,
                 width= 1200,
                 height=1000)
st.plotly_chart(scatter)