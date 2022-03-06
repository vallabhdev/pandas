import pandas as pd

def basic_details():
    return pd.read_csv('../../data/Animal.csv')


def affecting_factors():
    return pd.read_csv('../../data/Effecting_Factor.csv').drop(columns=['Country'])


def endangered_status():
    return pd.read_csv('../../data/Endangered_Species.csv').drop(columns=['Year', 'Extinction_Rate', 'Continent'])


def remediation():
    return pd.read_csv('../../data/Remediation_measures.csv').drop(columns=['Country', 'Effect_of_Measures'])

