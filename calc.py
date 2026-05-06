#Aggregations & grouping

def cal_data(df):
    df['total_per_customer'] = df.groupby('customer_id')['total_amount_inr'].transform('sum')
    df = df.sort_values(by='country',ascending=True) 
    print("Calculated part is sucessfully completed")
    return df