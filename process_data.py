
'''
BSTOCK take-home assignment
This script processes sales data from a CSV file and product data from a JSON file.
It merges the two datasets, aggregates the sales data by product category,
and generates a report with total sales, number of transactions, average transaction value, and total quantity sold for each category.
'''
import sys
import pandas as pd
import datetime as dt
import modules.data_ingestion as di
import modules.data_processing as dp

csv_file = 'sales_data.csv'
json_file = 'product_data.json'
export_file = 'aggregated_report.csv'

SUCCESS = True

check_csv_columns = ['sale_amount', 'quantity', 'transaction_id', 'product_id', 'date']
check_json_columns = ['product_id', 'category', 'product_name', 'price', 'availability']

##########################################
########### data ingestion ###############
##########################################

try:
    # read the csv file 
    df = di.read_csv_file(csv_file)
    # read the json file
    df_json = di.read_json_file(json_file)
except Exception as e:
    print("Error in data ingestion. Missing file or invalid format.")
    SUCCESS = False
    sys.exit()
    
# check if the required columns are present in the dataframe
for col in check_csv_columns:
    if col not in df.columns:
        print(f"Column '{col}' is missing")
        sys.exit()
# check if the required columns are present in the json dataframe
for col in check_json_columns:
    if col not in df_json.columns:
        print(f"Column '{col}' is missing")
        sys.exit()
        
# check if columns are missing in the csv file
nan_check = df[check_csv_columns[:1]].isna().any().any()
if nan_check:
    print("Check the csv file for missing values")
    sys.exit()
    
##########################################
############ data parsing ################
##########################################

try:
    # date parsing
    df = dp.date_format(df)
    # normalize the date column to remove time information
    df['date'] = pd.to_datetime(df['date']).dt.normalize()
    # merge the two dataframes on the 'product_id' column
    df_merged = pd.merge(df, df_json, on='product_id', how='inner')
except Exception as e:
    print("Error in data parsing")
    SUCCESS = False
    sys.exit()

##########################################
########## aggregated report #############
##########################################
# output the merged dataframe to a new csv file
try:
    df_output = dp.output_format(df_merged)
except Exception as e:
    print("Error in output formatting")
    SUCCESS = False
    sys.exit()
    

print(df_output)
if SUCCESS:
    # save the output to a csv file
    export_file = 'aggregated_report.csv'
    df_output.to_csv(export_file, float_format='%.2f', index=True)
    print(f"Data processing complete. Output saved to {export_file}.")
else:
    print("Exporting failed.")