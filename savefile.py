#saving the transformed data 
import os
from config import output_path

def output(df):
    os.makedirs(output_path,exist_ok=True)
    df.to_csv(os.path.join(output_path,'clean_data.csv'),index = False)
    print('Data saved the sucessfully')