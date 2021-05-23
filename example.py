import sqlite3

from excel_data_process import id_chargeback_transactions

# example of getting data by id
con = sqlite3.connect('db.sqlite')

cur = con.cursor()

args1 = id_chargeback_transactions

query1 = 'SELECT transactions.created_at, currency, amount, brand, bin, ' \
         'last_4, bin_country, cards.created_at, customers.created_at, ' \
         'ip_addr FROM transactions JOIN cards ON transactions.card_id = ' \
         'cards.id  JOIN customers ON cards.id = customers.card_id WHERE ' \
         'cards.brand = "visa" AND transactions.id in ' \
         '({seq})'.format(seq=','.join(['?'] * len(args1)))

cur.execute(query1, args1)
cur.fetchall()
con.close()
