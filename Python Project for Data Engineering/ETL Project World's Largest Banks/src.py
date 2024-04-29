from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


def log_progress(message, filepath):
    ''' This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing'''

    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(filepath, 'a') as f:
        f.write(timestamp + ' : ' + message + '\n')

def extract(url, table_attribs):
    '''This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''

    df = pd.DataFrame(columns = table_attribs)
    # get the contents of the webpage in text format and store in a variable called data
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')
    # find all html tables on the webpage
    tables = soup.find_all('tbody')
    print(len(tables))
    rows = tables[0].find_all('tr')

    for row in rows:
        col = row.find_all('td')
        if len(col) != 0:
            rank = int(col[0].text)
            bank = col[1].text
            market_cap = float(col[2].text)

            data_dict = {'Rank': rank, 'Bank_Name': bank, 'Market_Cap_USD_Billion': market_cap}

            df1 = pd.DataFrame(data_dict, index = [0])
            df = pd.concat([df, df1], ignore_index = True)
    return df

def transform(df, csv_path):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''

    # read the exchange rate csv file
    exchange_rate = pd.read_csv(csv_path)

    # Convert to a dictionary with "Currency" as keys and "Rate" as values
    exchange_rate = exchange_rate.set_index("Currency").to_dict()["Rate"]

    df['Market_Cap_GBP_Billion'] = [np.round(x * exchange_rate['GBP'], 2) for x in df['Market_Cap_USD_Billion']]
    df['Market_Cap_EUR_Billion'] = [np.round(x * exchange_rate['EUR'], 2) for x in df['Market_Cap_USD_Billion']]
    df['Market_Cap_INR_Billion'] = [np.round(x * exchange_rate['INR'], 2) for x in df['Market_Cap_USD_Billion']]

    return df

def load_to_csv(df, output_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''
    df.to_csv(output_path)
    
def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''
    df.to_sql(table_name, sql_connection, if_exists = 'replace', index = False)

def run_query(query_statement, sql_connection):
    ''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)