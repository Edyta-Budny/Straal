from excel_data_process import all_chargebacks, chargebacks_transactions
from utils import list_element, zip_data

# zip data from columns created_at and amount for comparison
data_report = zip_data(all_chargebacks)
data_db = zip_data(chargebacks_transactions)

# sort data by transaction creation date, because it is unique - I checked
# it out before zip data by using .unique() pandas function
data_report.sort()
data_db.sort()

# create a list with only transaction amount
amounts_report = list_element(data_report)
amounts_db = list_element(data_db)

# zip list to compare transaction amount from database and report
all_amounts = zip(amounts_report, amounts_db)

# percent of difference in transaction amounts
percent_amount_difference = [
    round(amounts_report / amounts_db * 100) for
    amounts_db, amounts_report in all_amounts
]


# Check if the percent of difference amount is the same for each chargeback
# transaction. I did not include the brand of the card because there was no
# distinction here, but I have checked this before.
def get_amount_differences():
    if len(set(percent_amount_difference)) == len(percent_amount_difference):

        print('There are various differences in the amounts compared to the '
              'report data')
    else:
        print(f'All transaction amounts with chargebacks in database are '
              f'{percent_amount_difference[0]} % greater compared to the '
              f'report data.')


get_amount_differences()
