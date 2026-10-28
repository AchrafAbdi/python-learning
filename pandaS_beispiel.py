import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_excel(r"C:/Users/Administrator/Desktop/Python kurs/Kursmaterialien/18 - DataScience - Stack/daten.xlsx")
df.head()
print(df.head())
year= df["Jahr"]
sales=df["Umsatz"]

plt.plot(year, sales)
plt.show()