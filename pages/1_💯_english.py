import pandas as pd
import streamlit as st

st.set_page_config(page_title='子页面1', page_icon='💯', layout='wide')

st.header('This is a subpage')

file = st.file_uploader('上传文件', 'xlsx')

if file is not None:
    df = pd.read_excel(file)
    st.dataframe(df)