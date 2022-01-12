# -*- coding: utf-8 -*-
"""
This module contains functions to clean raw data from a
Mental Health Services Data Set (MHSDS), check validity and
impute missing values
"""


def data_types(df):
    """
    Use this function to change variable formats prior to analysis
    
    converts DOB to date format
    converts admission_date to date format
    converts discharge_date to date format

    Parameters
    ----------
    df : main dataset
    Returns
    -------
    df : main dataset

    """
    df['PersonBirthDate'] = pd.to_datetime(df['PersonBirthDate'])
    df['StartDateHospProvSpell'] = pd.to_datetime(df['StartDateHospProvSpell'])
    df['DischDateHospProvSpell'] = pd.to_datetime(df['DischDateHospProvSpell'])
    return df


def age_check(df):
    """
    Checks age is within permitted bounds
    If age is missing or outside bounds,
    replaces age with median age

    Parameters
    ----------
    df : main dataset

    Returns
    -------
    df : main dataset
        adds age_admit column

    """
    df.loc[df['age_admit'] > 110, 'age_admit'] = None
    df.loc[df['age_admit'] < 16, 'age_admit'] = None
    med_age = df['age_admit'].median()
    df['age_admit'] = df['age_admit'].fillna(med_age)
    return df


def gender_replace(df):
    """
    Replaces values of the variable "Gender" from input dataset 
    to the format used for analysis and visualisation.
    Missing values or unknowns changed to NaN
    
    Parameters
    ----------
    df : main datatset
        
    Returns
    -------
    df : main dataset after replacement
    """
    gender_replaced_values = {"1": "1", "2": "2", "9": "3","X": np.nan}
    df.Gender = [gender_replaced_values[item] for item in df.Gender]
    return df


def marital_replace(df):
    """
    replaces values of the variable "MaritalStatus" from input dataset 
    to the format used for analysis and visualisation
    Grouped in to 'married' and 'not married'
    
    Parameters
    ----------
    df : main datatset
        
    Returns
    -------
    df : main dataset after replacement
    """
    marital_replaced_values = {"S": "0", "M": "1", "D": "0", "W": "0", "P": "0", "N": np.nan, "8": "0", "9": np.nan}
    df.MaritalStatus = [marital_replaced_values[item] for item in df.MaritalStatus]
    return df


def accom_replace(df):
    """
    replaces values of the variable "SettledAccommodationInd" from input dataset 
    to the format used for analysis and visualisation
    Grouped in to 'in accommodation' or 'not in accommodation'
    
    Parameters
    ----------
    df : main datatset
        
    Returns
    -------
    df : main dataset after replacement
    """
    accom_replaced_values = {"Y": "1", "N": "0", "Z": np.nan,"9": np.nan}
    df.SettledAccommodationInd = [accom_replaced_values[item] for item in df.SettledAccommodationInd]
    return df


def employ_replace(df):
    """
    replaces values of the variable "EmployStatus" from input dataset 
    to the format used for analysis and visualisation
    Grouped in to 'employed' or 'unemployed'
    
    Parameters
    ----------
    df : main datatset
        
    Returns
    -------
    df : main dataset after replacement
    """
    employment_replaced_values = {"1": "1", "2": "0", "3": "1", "4": "0", "5": "0", "6": "0", "7": "0", "8": "0", "ZZ": np.nan}
    df.EmployStatus = [employment_replaced_values[item] for item in df.EmployStatus]
    return df