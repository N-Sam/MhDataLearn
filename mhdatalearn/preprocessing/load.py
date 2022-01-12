# -*- coding: utf-8 -*-
"""
This module contains the function to load a user
specified file or the dummy data provided with
the package
"""


def load_data(filepath="/dummy_data.csv"):
    """
    Loads local data file as dataframe from specified filepath
    If no filepath specified, loads dummy dataset from web

    Parameters
    ----------
    filepath : user specified filepath
    
    Returns
    -------
    df : DataFrame

    """
    df = pd.read_csv(filepath)
    return df