import pandas as pd

REQUIRE_COLUMNS = [0, 1, 2, 3, 4]
COLUMNS_NAMES = ['created_at', 'currency', 'amount', 'masked CCN', 'brand']
SUBSET = ['created_at', 'currency', 'brand', 'bin', 'last_4']


def read_excel(sheet_name):
    return pd.read_excel('processing-report.xlsx', engine='openpyxl',
                         sheet_name=sheet_name, names=COLUMNS_NAMES,
                         header=None, usecols=REQUIRE_COLUMNS)


def get_bin(df):
    df['bin'] = df['masked CCN'].apply(lambda x: x[:6])
    return df['bin']


def get_last_4(df):
    df['last_4'] = df['masked CCN'].apply(lambda x: x[-4:])
    return df['last_4']


def drop_unnecessary(df):
    df.drop(0, inplace=True)
    df.drop(['masked CCN'], axis=1, inplace=True)
    return df


def fake_id(df):
    return df.insert(0, 'id', 'x')


def df_process(df_name):
    get_bin(df_name)
    get_last_4(df_name)
    drop_unnecessary(df_name)
    return df_name


def df_concat(df1, df2):
    return pd.concat([df1, df2])


def drop_duplicates(df, keep):
    return df.drop_duplicates(
        subset=SUBSET, keep=keep
    )


def get_id_chargebacks(column1, column2):
    return list(set(list(column1)) - set(column2))


def zip_data(df):
    return list(zip(df['created_at'], df['amount']))


def list_element(tuple_list):
    return [element2 for element1, element2 in tuple_list]
