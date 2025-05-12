
'''
BSTOCK take-home assignment
This script processes sales data from a CSV file and product data from a JSON file.
It merges the two datasets, aggregates the sales data by product category,
and generates a report with total sales, number of transactions, average transaction value, and total quantity sold for each category.
'''
import pandas as pd
import datetime as dt

csv_file = 'sales_data.csv'
json_file = 'product_data.json'
export_file = 'aggregated_report.csv'

##########################################
########### data ingestion ###############
##########################################

# read the csv file 
df = pd.read_csv(csv_file)

# read the json file
df_json = pd.read_json(json_file)

##########################################
############ data parsing ################
##########################################

# date parsing
for i in range(0, len(df['date'])):
    try:
        # convert the date string to a datetime object
        df.loc[i, "date"] = pd.to_datetime(df['date'][i], format='%Y-%m-%d')
    except Exception as e:
        # print("Error parsing date:", e)
        format_str = df['date'][i]
        date_obj = dt.datetime.strptime(format_str, '%m/%d/%y')
        df.loc[i, "date"] = date_obj
        # continue to the next iteration
        continue
    
# normalize the date column to remove time information
df['date'] = pd.to_datetime(df['date']).dt.normalize()
# merge the two dataframes on the 'product_id' column
df_merged = pd.merge(df, df_json, on='product_id', how='inner')


##########################################
########## aggregated report #############
##########################################
# output the merged dataframe to a new csv file

df_output = df_merged.groupby(['category']).agg({'sale_amount': 'sum'})
df_output['sale_amount'] = df_output['sale_amount'].apply(lambda x: '{:,.2f}'.format(x))
df_output['total_transactions'] = df_merged.groupby(['category'])['transaction_id'].nunique()
df_output['average_transaction_value'] = df_merged.groupby(['category'])['sale_amount'].mean().apply(lambda x: '{:,.2f}'.format(x))
df_output['total_quantity'] = df_merged.groupby(['category'])['quantity'].sum()
print("this is df_output")
print(df_output)

df_output.to_csv(export_file, float_format='%.2f', index=True)
print(f"Data processing complete. Output saved to {export_file}.")