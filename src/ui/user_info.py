import pandas as pd


def user_details():
    df = pd.read_csv('../../data/users.csv')
    user_dict = df.set_index('name').T.to_dict('list')
    return user_dict
