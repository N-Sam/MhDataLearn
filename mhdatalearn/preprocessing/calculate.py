# -*- coding: utf-8 -*-
"""
This module contains functions which calculate new
variables from variables included in raw data from a
Mental Health Services Data Set (MHSDS)
"""


def calc_age_admit(df):
    """
    caluculates age at admission
    adds age_admit to dataset

    Parameters
    ----------
    df : main dataset
    Returns
    -------
    df : main dataset

    """
    df['age_admit'] = ((df['StartDateHospProvSpell'] - df['PersonBirthDate']) //
                        timedelta(days=365.2425))
    return df


def check_emergency(df):
    """
    checks if 'AdmMethCodeHospProvSpell' is coded as an emergency admission
    adds flag to emergency admissions ('Emergency' == 1)

    Parameters
    ----------
    df : main dataset

    Returns
    -------
    df : main dataset


    """
    df['Emergency'] = np.where((df['AdmMethCodeHospProvSpell'] == "21") \
                        | (df['AdmMethCodeHospProvSpell'] == "22") \
                        | (df['AdmMethCodeHospProvSpell'] == "23") \
                        | (df['AdmMethCodeHospProvSpell'] == "24") \
                        | (df['AdmMethCodeHospProvSpell'] == "25") \
                        | (df['AdmMethCodeHospProvSpell'] == "2A") \
                        | (df['AdmMethCodeHospProvSpell'] == "2B") \
                        | (df['AdmMethCodeHospProvSpell'] == "2D") \
                                    ,1,0)
    return df


def calc_readmit(df):
    """
    calculates if admission is a readmission
    calculates days until next admission
    adds flag for a readmission
    adds number of days until admission

    Parameters
    ----------
    df : main dataset
        
    Returns
    -------
    df : main dataset

    """

    df = df.sort_values(["LocalPatientId",
                         "StartDateHospProvSpell"],
                        ascending=(True, True))
    df['ad_num'] = df.groupby(['LocalPatientId']).cumcount()+1
    df_read = df.copy()
    #df_read = df.loc[(df['ad_num'] > 1)]
    df_read['next_ad_num'] = df_read['ad_num']+1
    df_read = pd.merge(df_read,
                       df[['LocalPatientId',
                           'ad_num',
                           'StartDateHospProvSpell']],
                       how='left',
                       left_on=['LocalPatientId',
                                'next_ad_num'],
                       right_on=['LocalPatientId',
                                 'ad_num'])
    df = pd.merge(df,
                  df_read[['LocalPatientId',
                           'ad_num_x',
                           'StartDateHospProvSpell_y']],
                  how='left',
                  left_on=['LocalPatientId',
                           'ad_num'],
                  right_on=['LocalPatientId',
                            'ad_num_x'])
    df['days_since_admit'] = df['StartDateHospProvSpell_y'] - \
        df['DischDateHospProvSpell']
    df['days_since_admit'] =   df['days_since_admit'].dt.days    
    return df


def emergency_readmit(df):
    """
    Checks if readmission is within 30 days and adds flag ('Readmit30)
    Checks if episode is an emergency readmission within 30 days
    Adds flag ('EmergencyReadmit')

    Parameters
    ----------
    df : main dataset

    Returns
    -------
    df : main dataset


    """
    df['Readmit30'] = np.where((df['days_since_admit'] <= 30), 1, 0)
    df['EmergencyReadmit'] = np.where((df['Readmit30'] == 1) \
                                & (df['Emergency'] == 1),1,0)
    return df



def los_train(df):
    """
    Calculates length of stay (admission to discharge)
    for the training dataset
    Adds len_stay to dataset

    Parameters
    ----------
    df : main dataset
    
    Returns
    -------
    df : main dataset

    """
    df['len_stay'] = (df['DischDateHospProvSpell'] - df['StartDateHospProvSpell']) 
    return df


def los_current(df):
    """
    Calculates length of stay (admission to current date)
    for current inpatients
    Adds len_stay to dataset

    Parameters
    ----------
    df : main dataset
    Returns
    -------
    df : main dataset

    """
    df['len_stay'] = (datetime.now() - df['StartDateHospProvSpell']) 
    return df

