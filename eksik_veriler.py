# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 16:40:44 2023

@author: oruc2
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

eksikveriler = pd.read_csv('C:/Users/oruc2/OneDrive/Masaüstü/BTK/Python ile Makine Öğrenmesi/Veri Setleri/eksikveriler.csv')


print(eksikveriler)


# eksik verileri ortalamaya tamamlama 

eksikveriler.yas.fillna(method="bfill")

print(eksikveriler)
