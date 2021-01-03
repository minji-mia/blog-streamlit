from collections import UserString
import streamlit as st

PAGE_CONFIG = {'page_title':'Blog World', 'page_icon':':smiley:', 'layout':'centered'}

st.set_page_config(**PAGE_CONFIG)

#EDA Pkgs
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from wordcloud import WordCloud,STOPWORDS, ImageColorGenerator
        
# Layout templates
title_temp = """
    <div style="background-color:#f1d4d4;padding:10px;border-radius:10px;margin:10px">
    <h4 style="color:#000000;text-align:center;">{}</h4>
    <img src="https://cdn4.iconfinder.com/data/icons/essential-part-3/32/215-User-256.png" alt="User" style="vertical-align: middle;float:left;width: 50px;height: 50px;">
    <h6 style="color:#000000">Author: {}</h6>
    <br/>
    <br/>	
    <p style="text-align:justify">{}</p>
    <h6 style="color:#000000;text-align:right;">Post Date: {}</h6>
    </div> 
"""

def main():
    """A Simple CRUD Blog"""
    st.title("Blog World")
    menu = ["Home", "Login", "Sign Up", "View Posts", "Search"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        result = view_all()
        for i in result:
            b_author = i[0]
            b_title = i[1]
            b_article = str(i[2])[0:50]
            b_post_date = i[3]
            st.markdown(title_temp.format(b_title, b_author, b_article, b_post_date), unsafe_allow_html=True)

if __name__ == '__main__':
    main()