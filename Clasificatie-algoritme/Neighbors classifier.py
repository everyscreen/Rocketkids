import pandas as pd
import numpy as np
import sklearn

from sklearn.model_selection import train_test_split #(split de data voor training en test)
from sklearn.preprocessing import StandardScaler #preprocessor voor minimal bias
from sklearn.neighbors import KNeighborsClassifier #de KNN clasificatie algoritme
from sklearn.metrics import confusion_matrix #test het model voor accuracy
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

dataset = pd.read_excel(r'C:\Users\mkolb\Documents\Word documents\HBO ICT\Semester 3\datasets\MLSampledataset2.xlsx')
print(dataset.head())

#split de data in training en test data
#column 1, 2 en 3 zijn data. in 4 staat het antwoord
#pakt geen string dus data onder column 1
x = dataset.iloc[:, 1:3]
y = dataset.iloc[:, 3]

#split de data. 0.2 staat voor 20% van de data wat apart wordt gezet
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 0, test_size = 0.2)

#standard scaler
#uitzoeken wat dit nu doet
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.fit_transform(x_test)

# getal van de neighbors afstand berekenen:
import math
a = math.sqrt(len(y_test))
print('math neigbors classifier =',(a))

#define the model KNN, metric = 'euclidian' kan niet. nu standaard gehouden checken wat dat doet
classifier = KNeighborsClassifier(n_neighbors=3, p=1)

#fit model
classifier.fit(x_train, y_train)

#predict test results
y_pred = classifier.predict(x_train)
print('y_pred =',(y_pred))

#evaluate model confusion matrix ff nader onderzoeken
cm = confusion_matrix(y_test, y_pred)
print('confusion matrix =', (cm))

#f1 score
print('f1 score =',(f1_score(y_test, y_pred)))
#accuracy score
print('accuracy score =',(accuracy_score(y_test, y_pred)))

#hoe kan ik de overgebleven data classificeren?