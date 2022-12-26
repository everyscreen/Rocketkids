import pandas as pd 
import numpy as np
import pyodbc
import sklearn 

from sklearn.model_selection import train_test_split #(split de data voor training en test)
from sklearn.preprocessing import StandardScaler #preprocessor voor minimal bias
from sklearn.neighbors import KNeighborsClassifier #de KNN clasificatie algoritme
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

# Extract the features and labels
# the features of a dataset are the characteristics or attributes of the data, 
# while the label is the target variable that we are trying to predict.

x = dataset.iloc[:, 1:3]
y = dataset.iloc[:, 3]

#split de data. 0.5 staat voor 50% van de data wat apart wordt gezet
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 1, test_size = 0.50)

print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.fit_transform(x_test)

# Create a KNN classifier 5 is normal. Euclidean metric is het meest gangbaar
knn = KNeighborsClassifier(n_neighbors=2, metric='euclidean')

# Train the classifier using the training data
knn.fit(x_train, y_train)

# Predict the labels for the test data
y_pred = knn.predict(x_test)
print(y_pred)

print(x_train.shape)
print(y_pred.shape)

if y_train.shape == y_pred.shape:
    print("The input arrays have the same number of samples.")
else:
    print("The input arrays have different numbers of samples.")

# Calculate the accuracy score of the KNN model
accuracy = accuracy_score(y_train, y_pred)

# Print the accuracy score
print("Accuracy: {:.2f}".format(accuracy))