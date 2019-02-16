import os
import requests
import json

with open('config.json') as config_file:
    config = json.load(config_file)

def get_environmental_var(name):
    '''Returns environmental variables for keys/secrets
    Args:
        name (str): Name of environmental variable to get
    Returns:
        (str) Corresponding variable
    Raises:
        ValueError: if variable with name not found
    '''
    variable = os.environ.get(name)
    if not variable:
        raise ValueError('Environmental variable not found')
    else:
        return variable

def get_transactions(from_date=None, to_date=None):
    '''Gets all transactions spent for a given timeframe
    Args:
        from_date (str): YYYY-MM-DD
        to_date (str): YYYY-MM-DD
    Returns:
        (str) JSON of transactions
    '''
    endpoint = config['api_base_url'] + config['transactions_url']
    token = get_environmental_var('StarlingPersonalAccessToken')
    headers = {'Authorization': f'Bearer {token}'}
    query_string = f'?from={from_date}&to={to_date}' if from_date or to_date else ''
    response = requests.get(endpoint + query_string, headers=headers).json()
    transactions = response['_embedded']['transactions']
    return transactions
