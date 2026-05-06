#Main pipeline 

from ingest import load_data
from merge import merge_data
from filtering import fltr_data
from clean import clean_data
from transform import tran_data
from calc import cal_data
from savefile import output
from config import category, year, usd_to_inr_rate

def pipeline():
    cust_df,ord_df =load_data()
    merging_data = merge_data(cust_df,ord_df)
    filter_data = fltr_data(merging_data,category,year)
    cleaned_data = clean_data(filter_data)
    conv_data = tran_data(cleaned_data,usd_to_inr_rate)
    cal_part = cal_data(conv_data)
    saving_data = output(cal_part)
    print('Pipeline excuted sucessfully')


#Entry point
if __name__ =='__main__':
    pipeline()