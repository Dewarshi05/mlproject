import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer ## This is to set up a particular pipeline for the operations such 
## as StandardScaler, OneHotEncoder, Handelling missing values,etc
from sklearn.impute import SimpleImputer ## For missing value imputation purpose
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging

