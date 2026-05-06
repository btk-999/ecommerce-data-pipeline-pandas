#Loadind the data
import pandas as pd
import os
from config import data_path
def load_data():
    try:
        cust_df = pd.read_csv(os.path.join(data_path,'customers.csv'))
        ord_df = pd.read_csv(os.path.join(data_path,'orders.csv'))
        print("Data is loaded sucessfully")
        return cust_df,ord_df
    except Exception as e:
        print(f"Error while loading data{e}")
        raise