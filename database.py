import sqlite3
import pandas as pd
import numpy as np

conn = sqlite3.connect(r'C:\Users\chris\OneDrive\Documents\Hackathon2020\hen_data.db')
cursor = conn.cursor()

cursor.execute(
    """ INSERT INTO main
    VALUES ('username','password','firstname','lastname','phonenumber')
    """
)

df_main = pd.read_sql_query('SELECT * FROM main', conn)
df_user = pd.read_sql_query('SELECT * FROM user', conn)

"""
def update_main(username, password, firstname, lastname, phonenumber):
    sql = "INSERT INTO main VALUES ({},{},{},{},{})".format(username, password, firstname, lastname, phonenumber)
    cursor.execute(sql)
    conn.commit()
"""
