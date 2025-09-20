import streamlit as st

st.set_page_config(page_title="ETL Pipeline Visualization", layout="wide")

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=900, scrolling=True)

