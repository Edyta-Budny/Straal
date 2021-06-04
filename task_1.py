from excel_data_process import (chargebacks_transactions,
                                non_chargebacks_transactions)


def show_transactions():
    print(f'Chargeback transactions:\n{chargebacks_transactions}\n'
          f'Non chargeback transactions:\n{non_chargebacks_transactions}')
