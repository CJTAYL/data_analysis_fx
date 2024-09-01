"""
Functions to assist with data analysis tasks related to finance and banking
""" 

import numpy as np 
import random 

def detect_outliers(number_list):
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
    iqr = q3 - q1 
    lower_fence = q1 - (1.5 * iqr)
    upper_fence = q3 + (1.5 * iqr)

    return iqr, lower_fence, upper_fence


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

