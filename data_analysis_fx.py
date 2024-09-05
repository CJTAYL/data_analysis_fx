"""
Functions to assist with data analysis tasks related to finance and banking
""" 

import numpy as np 
import pandas as pd
import random 

def calculate_IQR(number_list):
    """
    Calculate the inter-quartile range (IQR), lower fence, and upper fence of a list of numbers to help identify outliers

    Parameters:
    - number_list = list of numbers 
    
    Returns:
    - iqr = inter-quartile range
    - lower_fence = lower limit for outliers (Q1 - 1.5 * IQR)
    - upper_fence = upper limit for outliers (Q3 + 1.5 * IQR)
    """
    q1 = np.percentile(number_list, 25) 
    q3 = np.percentile(number_list, 75)
    iqr = float(q3 - q1)
    lower_fence = float(q1 - (1.5 * iqr))
    upper_fence = float(q3 + (1.5 * iqr))

    return iqr, lower_fence, upper_fence


def column_stack(path_to_orig_csv, path_to_new_csv):
    """ 
    Convert the columns of an exported SQL table into the first row of a Pandas dataframe

    Parameters
    - path_to_orig_csv = file path to downloaded table
    - path_to_new_csv = file path for new csv + name

    Returns 
    - New CSV file with column names of original CSV as first column
    """ 
    df1 = pd.read_csv(path_to_orig_csv)
    df2 = pd.DataFrame()

    new_column_data = df1.columns
    df2['columns'] = new_column_data 

    df2.to_csv(path_to_new_csv, index=False)

    print('CSV updated successfully')


def five_number_summary(number_list):
    """ 
    Calculate the five number summary for a list of numbers

    Parameters:
    - number_list = list of numbers

    Returns: 
    - minimum = smallest value in the list
    - q1 = first quartile 
    - q2 = second quartile (i.e., median)
    - q3 = third quartile 
    -maximum = largest value in the list 
    """

    minimum = float(min(number_list))
    q1 = float(np.percentile(number_list, 25))
    q2 = float(np.percentile(number_list, 50))
    q3 = float(np.percentile(number_list, 75))
    maximum = float(max(number_list))

    return minimum, q1, q2, q3, maximum 


def generate_random_cc_numbers(n):
    """
    Generate a list of numbers to represent the digits of a credit card

    Parameters:
    - n = the number of 16 digits that will be returned

    Returns:
    - list_of_numbers = List of n random 16-digit strings.
    """
    list_of_numbers = []

    for i in range(n + 1):
        number = ''.join([str(random.randint(0,9)) for _ in range(16)])
        list_of_numbers.append(number)
        
    return list_of_numbers


def mask_cc_digits(number):
    """ 
    Function to replace each of the first 12 digits of a credit card number with an X. 

    Parameters:
    - number = Number that will be masked

    Returns: 
    - masked_number = Entered number where the first 12 digits are replaced with an 'X'
    """
    if len(number) == 16:
        masked_number = 'X' * 12 + number[12:]
        return masked_number
    elif len(number) < 16:
        return('Credit card number has less than digits')
    else: 
        return('Credit card number has more than 16 digits')

