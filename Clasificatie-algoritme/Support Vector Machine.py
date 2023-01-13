import pandas as pd 
import numpy as np
import pyodbc
import sklearn 

from sklearn.model_selection import train_test_split #(split de data voor training en test)
from sklearn.preprocessing import StandardScaler #preprocessor voor minimal bias
from sklearn.svm import SVC #clasificatie algoritme
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

X = dataset.iloc[:, 1:3]
y = dataset.iloc[:, 3]

# Splits de gegevens op in trainings- en testgegevens
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Maak het SVC-model met specifieke hyperparameters
model = SVC(kernel='rbf', C=10, gamma=0.1)

# Train het model op de gegeven trainingsgegevens
model.fit(X_train, y_train)

# Maak voorspellingen op de testgegevens
predictions = model.predict(X_test)

# Bepaal de nauwkeurigheid van het model
accuracy = model.score(X_test, y_test)
print('Accuracy:', accuracy)

#Autheur: Marlies Kolbeek
