import sqlite3

import pandas as pd

conn = sqlite3.connect('db.sqlite')

query = '''SELECT transactions.id, transactions.created_at, currency, amount, 
brand, bin, last_4 FROM transactions JOIN cards ON 
transactions.card_id = cards.id '''

df_db = pd.read_sql_query(query, conn)
