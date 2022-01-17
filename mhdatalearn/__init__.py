# -*- coding: utf-8 -*-
"""
This package contains tools to: preprocess raw Mental Health
Services Data Set (MHSDS) data in preparation for analysis,
train classification machine learning models and select the
best performing model, and apply the selected model to
new, preprocessed MHSDS data to identify people at high
risk of readmission.
"""

__version__ = "1.0.0"
__author__ = "Samuel, Simon, Yan, Kris"

from MHDataLearn import (preprocessing, modelselector, predict)
