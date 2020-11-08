import sqlite3
import pandas as pd
#from HenHealth import *

conn = sqlite3.connect('hen_data.db')
cursor = conn.cursor()


cursor.execute(
    """ INSERT INTO main
    VALUES ('username','password','firstname','lastname','phonenumber')
    """
)

df_main = pd.read_sql_query('SELECT * FROM main', conn)
df_user = pd.read_sql_query('SELECT * FROM user', conn)




# print(df_main)