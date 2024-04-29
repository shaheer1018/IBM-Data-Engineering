# Extracting and processing information on world's largest banks

# Problem Statement
A multi-national firm has hired you as a data engineer. Your job is to access and process data as per requirements.

Your boss asked you to compile the list of the top 10 largest banks in the world ranked by market capitalization in billion USD. Further, you need to transform the data and store it in USD, GBP, EUR, and INR per the exchange rate information made available to you as a CSV file. You should save the processed information table locally in a CSV format and as a database table. Managers from different countries will query the database table to extract the list and note the market capitalization value in their own currency.

The objectives of this project are:
1. Extract Real-World data from a public website using Beautiful Soup and Requests API in Python.
2. Transform the data as per the problem statement
3. Load the data in the required file format as well as a SQLite database
4. Query the database to retrieve filtered information from the table


Particulars of the code to be made have been shared below.

| Parameter                               | Value                                                                                           |
| --------------------------------------- | ------------------------------------------------------------------------------------------------|
| Code name                               | `banks_project.py`                                                                              |
| Data URL                                | `https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks`|
| Exchange rate CSV path                  | `https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv` |
| Table Attributes (upon Extraction only) | `Name`, `Market_Cap_USD_Billion`                                                                        |
| Table Attributes (final)                | `Name`, `Market_Cap_USD_Billion`, `Market_Cap_GBP_Billion`, `Market_Cap_EUR_Billion`, `Market_Cap_INR_Billion`                  |
| Output CSV Path                         | `./Largest_banks_data.csv`                                                                      |
| Database name                           | `Banks.db`                                                                                      |
| Table name                              | `Largest_banks`                                                                                 |
| Log file                                | `code_log.txt`                                                                                  |


# Tasks
1. Write a function to extract the tabular information from the given URL under the heading By Market Capitalization, and save it to a data frame.
2. Write a function to transform the data frame by adding columns for Market Capitalization in GBP, EUR, and INR, rounded to 2 decimal places, based on the exchange rate information shared as a CSV file.
3. Write a function to load the transformed data frame to an output CSV file.
4. Write a function to load the transformed data frame to an SQL database server as a table.
5. Write a function to run queries on the database table.
6. Run the following queries on the database table:
   - Extract the information for the London office, that is Name and Market_Cap_GBP_Billion
   - Extract the information for the Berlin office, that is Name and Market_Cap_EUR_Billion
   - Extract the information for New Delhi office, that is Name and Market_Cap_INR_Billion
7. Write a function to log the progress of the code.

## Usage

Install the required libraries using the provided `requirements.txt` file. The command syntax is:

```bash
python -m pip install -r requirements.txt
```

Download the required exchange rate file using the terminal command:

```bash
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv
```
If you are using windows you can directly download the csv file by opening the given link and then save it to the project folder.

Execute the code using the command:

```bash
python banks_project.py
```

