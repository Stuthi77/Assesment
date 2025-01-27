# -*- coding: utf-8 -*-
"""lvadsusr80_stuthi_lab1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wYRK7mKHk2CU0hN6t9978BEbb5ENfCAL
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df=pd.read_csv("/content/winequality-red.csv")
df

"""#handling missing values"""

df.info()

df=df.dropna()
X=df[['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol']]
Y=df['quality']
x_train,x_test,y_train,y_test=train_test_split(X,Y,random_state=42)

"""#Data Tranformation"""

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train[:, 1] = scaler.fit_transform(x_train[:, 1])
x_test[:, 1] = scaler.transform(x_test[:, 1])

"""#Encoding And Balancing Data"""

from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
df['fixed acidity']=encoder.fit_transform(df['fixed acidity'])
df['alcohol']=encoder.fit_transform(df['alcohol'])
df['chlorides']=encoder.fit_transorm(df['chlorides'])

"""#featuring Selection And Data Cleaning"""

X=df[['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol']]
Y=df['quality']

"""#Data Splitting"""

x_train,x_test,y_train,y_test=train_test_split(X,Y,random_state=42,test_size=0.2)

"""#Model Development"""

Model=RandomForestClassifier(n_estimators=100,random_state=42)
Model.fit(x_test, y_test)
y_pred=Model.predict(x_test)

"""#Model Evaluation"""

from sklearn.metrics import accuracy_score,precision_score,recall_score
a=accuracy_score(y_test,y_pred)
b=precision_score(y_test,y_pred)
c=recall_score(y_test,y_pred)
print("Accuracy Score:",a)
print("Precision:",b)
print("recall:",c)

from matplotlib import pyplot as plt
df.plot(kind='scatter', x=x_test['volatile acidity'], y=y_test, s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)