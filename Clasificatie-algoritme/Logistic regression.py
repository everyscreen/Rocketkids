import pandas as pd 
import numpy as np
import sklearn 

from sklearn.model_selection import train_test_split #(split de data voor training en test)
from sklearn.linear_model import LogisticRegression #clasificatie algoritme
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix #test
from sklearn.metrics import accuracy_score #test

dataset = pd.read_excel(r'C:\Users\mkolb\Documents\Word documents\HBO ICT\Semester 3\datasets\MLSampledataset.xlsx')
print(dataset.head())

sns.countplot('column_1', hue='WINorLOSS', data=df)
plt.show()

#split de data in training en test data
#column 1, 2 en 3 zijn data. in 4 staat het antwoord

x = df.drop('column_1', axis=1)
y = df['column_1']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=1)
logmodel = LogisticRegression()
logmodel.fit(x_train, y_train)
 
predictions = logmodel.predict(x_test)
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))
print(accuracy_score(y_test, predictions))