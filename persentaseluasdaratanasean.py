import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# ===MySQL Properties with mysqlconnector

conn = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '',
    database = 'world'
)

# ===Read MySQL

q = """
SELECT Name as Negara_ASEAN, surfacearea as Luas_Daratan
FROM country
WHERE Name in ('Brunei', 'Cambodia', 'East Timor', 'Indonesia', 'Laos', 'Malaysia', 'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Vietnam')
ORDER BY Negara_ASEAN ASC;
"""

df = pd.read_sql(q, con=conn)

# ===PLOT

x = list(df['Negara_ASEAN'])
y = list(df['Luas_Daratan'])

warna = ['red', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'grey', 'gold', 'lightblue', 'blue']

_,_,autotexts = plt.pie(y, labels=x, colors=warna,
    autopct = '%1.1f%%',
    textprops={'color':'black'}
)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_size(6)

plt.title('Persentase Luas Daratan ASEAN')

plt.show()