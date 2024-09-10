import altair as alt
import numpy as np
import pandas as pd 
import streamlit as st 


st.set_page_config(
    page_title="Streamlit Trials in Docker", 
    page_icon="🦍")

st.markdown(
    """
    <style> 
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden}
        .stAppDeployButton {visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('Streamlit Trials in Docker')

st.write(
    """
    ## Welcome to StreamLit Trials in Docker.

    ### [More info](https://docs.streamlit.io)

    ### Other pages 
    > - [Hello World] (./hello)


    
    This is a demo of Streamlit running in a Docker container. 
    """
)