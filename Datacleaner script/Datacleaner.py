import pyodbc
import pandas as pd
from pandas import Series, DataFrame

server = 'tcp:rockettheunsinkable.database.windows.net'
database = 'Rocketv3'
username = 'rocketadmin'
password = 'Marlies123!'
driver= '{ODBC Driver 17 for SQL Server}'
conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' +
    server + ';PORT=1433;DATABASE=' + database +
    ';UID=' + username + ';PWD=' + password)

cursor = conn.cursor()

query = "SELECT * FROM dbo.[CBS-geboorteprog];"
df = pd.read_sql(query, conn)
df_new = df.replace(to_replace = '^\.$', value = '' , regex = True) 
print("changes", df.count().sum() - (df == df_new).astype(int).sum().sum())
print(df_new.head(26))
conn.close()
