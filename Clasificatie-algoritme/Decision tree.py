import pandas as pd 
import numpy as np
import pyodbc
import sklearn 

from sklearn.model_selection import train_test_split #(split de data voor training en test)
from sklearn.preprocessing import StandardScaler #preprocessor voor minimal bias
from sklearn import tree #clasificatie algoritme
from sklearn.metrics import confusion_matrix #test het model voor accuracy
from sklearn.metrics import accuracy_score

dataset = pd.read_excel(r'C:\Users\mkolb\Documents\Word documents\HBO ICT\Semester 3\datasets\MLkindplaats_kids_testset.xlsx')
print(dataset.head())

# Splits de gegevens in een trainings- en testset
X = dataset.iloc[:, 1:3]
y = dataset.iloc[:, 3]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Maak het decision tree model aan en train het op de gegevens
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

# Gebruik het model om voorspellingen te doen op de testgegevens
predictions = clf.predict(X_test)

# Bekijk hoe goed het model presteert
print(accuracy_score(y_test, predictions))