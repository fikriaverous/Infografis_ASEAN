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
SELECT co.Name as Negara_ASEAN, co.Population as Populasi_Negara, co.GNP, ci.Name as Ibukota, ci.Population as Populasi_Ibukota
FROM country co
JOIN city ci
ON ci.ID=co.Capital
WHERE co.Name in ('Brunei', 'Cambodia', 'East Timor', 'Indonesia', 'Laos', 'Malaysia', 'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Vietnam')
ORDER BY Negara_ASEAN ASC;
"""

df = pd.read_sql(q, con=conn)

# ===PLOT

x = list(df['Negara_ASEAN'])
y = list(df['Populasi_Negara'])

plt.bar(x,y, color=['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'grey', 'gold', 'lightblue', 'blue'], zorder=2)

for a,b in zip(x,y):
    plt.text(a, b, str(b), fontsize=7, horizontalalignment='center')

plt.title('Populasi Negara ASEAN')
plt.xlabel('Negara')
plt.ylabel('Populasi (x100jt Jiwa)')
plt.xticks(rotation=45, size=8)
plt.grid(True, zorder=1)
plt.show()