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

# Security
# passlib, hashlib, bcrypt, scrypt
import hashlib
def make_hashes(pw):
    return hashlib.sha256(str.encode(pw)).hexdigest()

def check_hashes(pw, hashed_text):
    if make_hashes(pw) == hashed_text:
        return hashed_text
    return False
         
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

    elif choice == "Login":
        st.subheader("Logged In")
        user_name = st.sidebar.text_input("User name")
        pw = st.sidebar.text_input("Password", type='password')
        if st.sidebar.button("Login"):
            create_user_table()
            hashed_pw = make_hashes(pw)

            result = login(user_name, check_hashes(hashed_pw))
            if result:
                st.success("Logged in as {}".format(user_name))
                work = st.selectbox("Work", ["Add Post", "Manage Blog", "Profile Setting"])

                if work == "Add Post":
                    st.subheader("Add Articles")
                    create_table()
                    author = st.text_input("Enther Author Name", max_chars=50)
                    title = st.text_input("Enther Post Title")
                    article = st.text_area("Post Article", height=200)
                    post_date = st.date_input("Date")
                    if st.button("Add"):
                        add_data(author, title, article, post_date)
                        st.success("Post:{} saved".format(title))

                elif work == "Manage Blog":
                    st.subheader("Manage Articles")

                    result = view_all()    
                    clean_db = pd.DataFrame(result, columns=["Author", "Title", "Articles", "Post date"])
                    st.dataframe(clean_db)

                    title_list = [i[0] for i in view_all_titles()]
                    delete_by_title = st.selectbox("Unique Title", title_list)

                    if st.button("Delete"):
                        delete_data(delete_by_title)
                        st.warning("Deleted: {}".format(delete_by_title))

                    if st.checkbox("Metircs"):
                        new_df = clean_db
                        new_df['Length'] = new_df['Articles'].str.len()
                        st.dataframe(new_df)

                        st.set_option('deprecation.showPyplotGlobalUse', False)

                        st.subheader("Author Stats")
                        new_df['Author'].value_counts().plot(kind='bar')
                        st.pyplot()

                        st.subheader("Author Stats")
                        new_df['Author'].value_counts().plot.pie()
                        st.pyplot()
                        
                    if st.checkbox("Word Cloud"):        
                        st.subheader("Generate Word Cloud")
                        text = ','.join(new_df['Articles'])
                        wordcloud = WordCloud().generate(text)
                        plt.imshow(wordcloud, interpolation='bilinear')
                        plt.axis('off')
                        st.pyplot()
                        
    elif choice == "Sign Up":
        st.subheader("Create a new account")
        new_user = st.text_input("User name")
        new_pw = st.text_input("Password", type='password')

        if st.button("Sign up"):
            create_user_table()
            add_userdata(new_user, make_hashes(new_pw))
            st.success("You have successfully create an account")     


if __name__ == '__main__':
    main()