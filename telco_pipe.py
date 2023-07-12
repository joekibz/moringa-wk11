
##<----------------------------------------
#Telco billing pipeline unittesting
##----------------------------------------->

import pandas as pd
import unittest


def data_extraction(file_path):

    """
        Function takes as input path to csv file on disk and returns pandas df
    """
    
    data = pd.read_csv(file_path)
    return data

def data_transformation(data):

    """
        Function takes df as input. Transformations done: 1-Drop duplicate entries, 2-Remove '$' currency sign in 'billing_amount' column,
        3-Add column 'total_charges' using summation of 'billing_amount' and 'tax_amount'
        Returns transformed data df
    """
    
    data = data.drop_duplicates()
    data['billing_amount'] = data['billing_amount'].str.replace('$', '').astype(float)
    data['total_charges'] = data['billing_amount'] + data['tax_amount']
    return data

def data_loading(data, output_file):

    """
        Function takes df as input and writes it out to csv file 'output_file'
    """
    
    data.to_csv(output_file, index=False)