#Cleaning the filered data set (removing duplicates & handling missing vaules)

def clean_data(df):
    df = df.drop_duplicates()
    df.fillna({
        'discount_amount_usd': 0,
        'shipping_fee_usd': 0,
        'tax_amount_usd': 0},inplace=True)
    print('Data clean the sucessfully')
    return df