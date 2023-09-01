# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 15:19:37 2023

@author: edwar
"""

import streamlit as st


st.set_page_config(
    page_title="Korbel Fantasy League",
    page_icon="🏈",
    layout="wide"
)

st.write("# Welcome to the Official App of the Korbel Fantasy League.")
st.subheader('Select a page from the sidebar to get started.')
st.text('Player Data: analyze data on players for 2023 (including projections) and 2022 (including draft recap)')
st.text('Past Seasons: recap each season, including full season stats')
st.text('Team Owners: assess total historic performance of all team owners')
st.text('Comparison of Performance and Value: use this interactive chart to explore draft value and player performance')
st.text('2022 Team Run Pass: run/pass stats for NFL teams in 2022')


st.subheader('Version History')
st.text('V1.1, 9/1/2023: Added run/pass stats for NFL teams in 2022')
st.text('V1.05, 8/30/2023: Updated 2023 player projections, added rookies from 2023 draft class')
st.text('V1.00, 8/28/2023: App release')




st.sidebar.success("Select a page above.")
