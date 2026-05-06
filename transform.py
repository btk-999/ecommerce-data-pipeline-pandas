#Transforming the data according to business logic
from config import usd_to_inr_rate

def tran_data(df,rate):
    df['subtotal_inr'] = df['subtotal_usd']*rate
    df['discount_amount_inr'] = df['discount_amount_usd']*rate
    df['shipping_fee_inr'] = df['shipping_fee_usd']*rate
    df['tax_amount_inr'] = df['tax_amount_usd']*rate
    df['total_amount_inr'] = df['total_amount_usd']*rate
    print('USD to INR currency conversion columns are inserted')
    df['Ele_id'] = 'E' + df['year'].astype(str)
    return df