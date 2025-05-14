import pandas as pd
import datetime as dt
import modules.data_enrichment as de

def date_format(df):
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
    return df

def output_format(df_merged):
    df_output = df_merged.groupby(['category']).agg({'sale_amount': 'sum'})
    df_output['sale_amount'] = df_output['sale_amount'].apply(lambda x: '{:,.2f}'.format(x))
    # find the total transactions for each category
    tot_transactions_obj = df_merged.groupby(['category'])['transaction_id']
    for i in tot_transactions_obj:
        category, id = i
        df_output.loc[category, 'total_transactions'] = int(len(id))
    # find the average transaction value for each category
    avg_transaction_obj = df_merged.groupby(['category'])['sale_amount']
    for i in avg_transaction_obj:
        category, amount = i
        avg = de.get_avg(amount)
        df_output.loc[category, 'average_transaction_value'] = avg
    # find the total quantity for each category
    tot_quantity_obj = df_merged.groupby(['category'])['quantity']
    for i in tot_quantity_obj:
        category, quantity = i
        df_output.loc[category, 'total_quantity'] = int(de.get_sum(quantity))
    # sort the categories in alphabetical order
    df_output = df_output.sort_values(by='category')
    
    return df_output