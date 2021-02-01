# DB pkg
import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

# Functions
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS blogtable(author TEXT, title TEXT, article TEXT, postdate DATE)')

def add_data(author, title, article, postdate):
    c.execute('INSERT INTO blogtable(author, title, article, postdate) VALUES(?,?,?,?)', (author, title, article, postdate))
    conn.commit()

def view_all():
    c.execute('SELECT * FROM blogtable')
    data = c.fetchall()
    return data

def view_all_titles():
    c.execute('SELECT DISTINCT title FROM blogtable') 
    data = c.fetchall()
    return data       

def get_blog_by_title(title):
    c.execute('SELECT * FROM blogtable WHERE title="{}"'.format(title)) 
    data = c.fetchall()
    return data    