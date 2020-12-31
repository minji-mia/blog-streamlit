from collections import UserString
import streamlit as st

PAGE_CONFIG = {'page_title':'Blog World', 'page_icon':':smiley:', 'layout':'contered'}

st.beta_set_page_config(**PAGE_CONFIG)

#EDA Pkgs
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from wordcloud import WordCloud,STOPWORDS, ImageColorGenerator
 
if __name__ == '__main__':
    main()