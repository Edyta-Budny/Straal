from db_data_process import df_db
from utils import (SUBSET, df_concat, df_process, drop_duplicates, fake_id,
                   get_id_chargebacks, read_excel)

# read excel
visa_chargebacks = read_excel('Visa')
mastercard_chargebacks = read_excel('Mastercard')

# process data
df_process(visa_chargebacks)
df_process(mastercard_chargebacks)

# concat all chargebacks data
all_chargebacks = df_concat(visa_chargebacks, mastercard_chargebacks)

# create fake id to concat all chcargebacks with db data
fake_id(all_chargebacks)

# concat chargebacks data with db data
all_data = df_concat(all_chargebacks, df_db)

# remove duplicates and receive transactions without chargebacks (because
# keep=False in drop_duplicates function)
non_chargebacks_transactions = drop_duplicates(all_data, False)

# chargeback transactions
duplicates = all_data[all_data.duplicated(subset=SUBSET, keep=False)]
chargebacks_transactions = drop_duplicates(duplicates, 'last')


# id from lists allows to retrieve data from the database because it's unique
# I checked it out before zip data by using .unique() pandas function
# example of getting data by id in example.py

# only id of chargeback transactions
id_chargeback_transactions = get_id_chargebacks(
    df_db['id'], list(non_chargebacks_transactions['id']))

# only id of non chargeback transactions
id_non_chargebacks_transactions = get_id_chargebacks(
    df_db['id'], id_chargeback_transactions)
