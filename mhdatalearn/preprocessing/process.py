# -*- coding: utf-8 -*-
"""
This module contains the function toexecute all 
preprocessing functions (from clean.py and calculate.py)
on a dataset (which can be specified as training or a
new unseen dataset) in preparation for ml model
training and selection.
"""


from MhDataLearn.clean import (data_types, age_check, gender_replace,
                               marital_replace, accom_replace,
                               employ_replace
                               )
from MhDataLearn.calculate import (calc_age_admit, check_emergency,
                                   calc_readmit, calc_readmit,
                                   check_emergency, los_train, los_current
                                   )


def wrangle_data(df_temp, test= "training"):
    """
    Parameters
    ----------
    df_temp : main dataset
        
    test : True means wrangle data on historical dataset
           False means wrangle data on current dataset
                 and caluclaue LOS to today

    Returns
    -------
    df : main dataset
        all varibles encoded ready for modelling and appropriate
        flags added

    """
    df = df_temp.copy()
    df = data_types(df)
    df = age_check(df)
    df = gender_replace(df)
    df = marital_replace(df)
    df = accom_replace(df)
    df = employ_replace(df)
    df = calc_age_admit(df)
    df = check_emergency(df)
    if test == "training":
        df = calc_readmit(df)
        df = emergency_readmit(df)
        df = los_train(df)
        print('Training data has been cleansed')
    else:
        df = los_current(df)
        print('Current data has been cleansed')
    return df