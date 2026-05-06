#Filtering the data before transformation
from config import category,year

def fltr_data(df,category,year):
    fltrd_data = df[(df['category'].isin(category)) & (df['year'].isin(year))].copy()
    print(f"The data is filter sucessfully under {category} categories for {year} years")
    return fltrd_data