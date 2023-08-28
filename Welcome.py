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
st.text('Select a page from the sidebar to get started.')
st.text('Player Data: analyze data on players for 2023 (including projections) and 2022 (including draft recap')
st.text('Past Seasons: recap each season, including full season stats')
st.text('Team Owners: assess total historic performance of all team owners')
st.text('Comparison of Performance and Value: use this interactive chart to explore draft value and player performance')


st.sidebar.success("Select a page above.")
