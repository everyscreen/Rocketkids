import pandas as pd 
import numpy as np
import pyodbc
import sklearn 
import joblib

from sklearn.model_selection import train_test_split #(split de data voor training en test)
from sklearn.preprocessing import StandardScaler #preprocessor voor minimal bias
from sklearn import tree #clasificatie algoritme
from sklearn.metrics import confusion_matrix #test het model voor accuracy
from sklearn.metrics import accuracy_score

server = 'tcp:marlies.database.windows.net'
database = 'rocketdb2'
username = 'rocketadmin'
password = 'Marlies123!'
driver= '{ODBC Driver 17 for SQL Server}'
conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' +
    server + ';PORT=1433;DATABASE=' + database +
    ';UID=' + username + ';PWD=' + password)

cursor = conn.cursor()

query = "SELECT * FROM [dbo].[MLkindplaats_kids_testset]"
dataset = pd.read_sql(query, conn)

print(dataset.head())

# Splits de gegevens in een trainings- en testset
X = dataset.iloc[:, 1:3]
y = dataset.iloc[:, 3]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Maak het decision tree model aan en train het op de gegevens
model = tree.DecisionTreeClassifier()
model = model.fit(X_train, y_train)

# Gebruik het model om voorspellingen te doen op de testgegevens
predictions = model.predict(X_test)

# Bekijk hoe goed het model presteert
print("accuracy", accuracy_score(y_test, predictions))

joblib.dump(model, 'decision_tree_model.pkl')

