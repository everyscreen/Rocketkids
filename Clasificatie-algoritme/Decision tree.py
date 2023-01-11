import pandas as pd 
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

#nieuw model trainen
model = joblib.load('decision_tree_model.pkl')

# Laad de nieuwe gegevens in en bereid deze voor
server = 'tcp:marlies.database.windows.net'
database = 'rocketdb2'
username = 'rocketadmin'
password = 'Marlies123!'
driver= '{ODBC Driver 17 for SQL Server}'
conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' +
    server + ';PORT=1433;DATABASE=' + database +
    ';UID=' + username + ';PWD=' + password)

cursor = conn.cursor()

query = "SELECT * FROM [dbo].[MLkindplaats_kids_officieel]"
new_data = pd.read_sql(query, conn)

#eerste kolom leest hij niet omdat het een string is, deze weghalen.
new_data = new_data.iloc[:, 1:3]

# Voorspel de waarden op basis van de nieuwe gegevens
predictions = model.predict(new_data)
print(predictions)

# Bewaar de voorspellingen voor toekomstig gebruik
# makkelijkste manier via een function zodat beide datasets gecombineerd worden 

def save_data(data, data_path):
    # Sla de gegevens op in het opgegeven bestand of database      
    data.to_csv(data_path)
    
def save_predictions(predictions, data, data_path):
    # Voeg de voorspellingen toe aan de dataset
    data['predictions'] = predictions

    # Sla de gewijzigde dataset op in een nieuw bestand
    save_data(data, data_path)

# voor nu opgeslagen op mijn eigen device, connectie naar server en daar uploaden kostte teveel tijd om uit te zoeken hoe dit moest, kwam in tijdnood.
save_predictions(predictions, new_data, r"C:\Users\mkolb\Documents\Word documents\HBO ICT\Semester 3\datasets\voorspelling2.csv")

#connectie met database opslaan en sluiten
cursor.close()
conn.commit()
conn.close()