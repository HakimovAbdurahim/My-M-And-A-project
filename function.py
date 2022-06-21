from sqlite3 import connect


def sort_gender(x):
    if x == 'M' or x == '0':
        x = 'Male'
    elif x == 'F' or x == '1':
        x = 'Female'
    return x


def replace_str(x):
    return str(x).replace('"', '').replace('\\', '').title()


def replace_str2(x):
    return x.replace('-', ' ').replace('_', ' ').title()


def cut_gender(x):
    if x == 'string_Male' or x == 'boolean_0' or x == 'character_M':
        x = 'Male'
    elif x == 'string_Female' or x == 'boolean_1':
        x = 'Female'
    return x


def cut_age(x):
    return x.replace('years', '').replace('year', '').replace('yo', '')


def cut_str(x):
    return x.replace('string_', '').title()


def csv_to_sql(df):
    sql_data = connect('Database.db')
    cursor = sql_data.cursor()
    return df.to_sql(name='data_usa', con=sql_data, if_exists='replace')
