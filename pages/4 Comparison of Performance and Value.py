# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 11:42:34 2023

@author: edwar
"""

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="2022 Performance and Draft Value",
    page_icon="🏈",
    layout="wide"
)

st.write("# Analysis of 2022 Performance and Draft Value")
st.text('Use this chart to compare performance against draft value of 2022 players.')
st.text('Size of the bubble represents games played.')
st.text('Hover/click on a point to see player name, position, total points, draft value, and games played.')
st.text('Click on the positions on the legend to filter by position.')



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
                 title="2022 Performance and Draft Value of NFL Players",
                 width= 1200,
                 height=1000)
st.plotly_chart(scatter)