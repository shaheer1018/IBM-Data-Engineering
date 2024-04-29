from src import log_progress, extract, transform, load_to_csv, load_to_db, run_query
import requests
import bs4
import pandas
import sqlite3
import numpy
import datetime



def main():

    log_file_path = './etl_project_log.txt'
    url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
    table_attribs = ['Rank', 'Bank_Name', 'Market_Cap_USD_Billion']
    csv_path = './exchange_rate.csv'
    output_path = './banks_ranking.csv'
    db_name = 'Banks.db'
    table_name = 'Largest_Banks'
    
    log_progress('Preliminaries complete. Initiating ETL process', log_file_path)
    df = extract(url, table_attribs)
    
    log_progress('Data extraction complete. Initiating Transformation process', log_file_path)
    df = transform(df, csv_path)

    log_progress('Data transformation complete. Initiating Loading process', log_file_path)
    load_to_csv(df, output_path)
    log_progress('Data saved to CSV file', log_file_path)

    # establish a connection to the database
    sql_connection = sqlite3.connect(db_name)
    log_progress('SQL Connection initiated', log_file_path)
    load_to_db(df, sql_connection, table_name)

    log_progress('Data loaded to Database as a table, Executing queries', log_file_path)

    # print the contents of the entire table
    query_statement_1 = 'SELECT * FROM Largest_banks'
    run_query(query_statement_1, sql_connection)

    # print the average market capitalization of all the banks in Billion USD
    query_statement_2 = 'SELECT AVG(Market_Cap_GBP_Billion) FROM Largest_Banks'
    run_query(query_statement_2, sql_connection)

    # print only the names of the top 5 banks
    query_statement_3 = 'SELECT Bank_Name from Largest_Banks LIMIT 5'
    run_query(query_statement_3, sql_connection)

    log_progress('Process Complete', log_file_path)

    # close SQLite3 connection
    sql_connection.close()
    log_progress('Server Connection closed', log_file_path)


    # verify log entries
    with open(log_file_path, 'r') as log:
        LogContent = log.read()
        print(LogContent)





if __name__ == '__main__':
    main()