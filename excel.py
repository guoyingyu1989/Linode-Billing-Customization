import pandas as pd
import os
import re
from datetime import datetime

def create_bill_details_df(items):
    bill_details = {
        'Label': [item.label for item in items],
        'From': [item.from_date for item in items],
        'To': [item.to_date for item in items],
        'Quantity': [item.quantity for item in items],
        'Unit Price': [item.unit_price for item in items],
        'Amount': [item.amount for item in items]
    }
    df = pd.DataFrame(bill_details)
    return df

def write_df_to_excel(df, filename):
    df.to_excel(filename, index=False)

def read_excel_file(filename):
    df = pd.read_excel(filename)
    return df

def update_df_with_tags(df, linode_result):
    if 'Tags' not in df.columns:
        df['Tags'] = None
    for i in range(len(df)):
        id = re.findall(r'\(\d{8}\)', df.iloc[i, 0])
        if id:
            id = int(id[0][1:-1])  # tranfer the id into interger
            for item in linode_result:
                if item[0] == id:
                    df.loc[i, 'Tags'] =  ', '.join(item[1])  # if tag is a list, change it to string.
                    break
    return df

def get_current_datetime_as_str():
    now = datetime.now()
    filename = now.strftime('%Y-%m-%d %H:%M:%S.xlsx')
    return filename

def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
