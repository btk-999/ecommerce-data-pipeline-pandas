#Merging or Joining the data sets

def merge_data(cust_df,ord_df):
    df = cust_df.merge(ord_df, on = 'customer_id', how ='inner')
    print('Merge the data sets sucessfully')
    return df