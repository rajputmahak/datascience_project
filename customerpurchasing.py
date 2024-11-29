# -*- coding: utf-8 -*-
"""customer.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wpeAikhfyaFkSrF8yNM1cbEfuV0dUOBy
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path='//content/customerpurchasing.csv'
df=pd.read_csv(path)
print(df)

X = df['annual_income'].values
Y = df['purchase_amount'].values
print(X,Y)

plt.scatter(X,Y,color='red')
plt.plot(X,Y,color='blue')
plt.title('simple linear regression')
plt.xlabel('annual_income')
plt.ylabel('purchase_amount')
plt.show()