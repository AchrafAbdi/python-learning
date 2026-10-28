# Importiert pandas zur Verarbeitung von Tabellen unter dem Kurznamen pd.
import pandas as pd

# Importiert pyplot zum Erstellen von Diagrammen unter dem Kurznamen plt.
import matplotlib.pyplot as plt

# Legt den gesuchten Vornamen fest.
name = "Anna"

# Legt das gesuchte Geschlecht fest: F steht hier für weiblich.
gender = "F"

# Legt den gesuchten US-Bundesstaat fest: CA steht für Kalifornien.
state = "CA"

# Liest die CSV-Datei ein und speichert die Tabelle im DataFrame df.
df = pd.read_csv(
    "C:/Users/Administrator/Desktop/Python kurs/Kursmaterialien/data/names.csv"
)

# Prüft für jede Zeile, ob in der Spalte "Name" der Wert "Anna" steht.
# Behält nur passende Zeilen und speichert sie in df1.
df1 = df[df["Name"] == name]

# Filtert df1 weiter: Behält nur Zeilen mit "F" in der Spalte "Gender".
df2 = df1[df1["Gender"] == gender]

# Filtert df2 weiter: Behält nur Zeilen mit "CA" in der Spalte "State".
df3 = df2[df2["State"] == state]

# Gibt die gefilterte Tabelle in der Konsole aus.
print(df3)

# Sortiert die gefilterte Tabelle nach "Year" aufsteigend:
# vom ältesten zum neuesten Jahr. Speichert das Ergebnis in df4.
df4 = df3.sort_values("Year")

# Zeichnet ein Liniendiagramm:
# x-Achse = Jahr ("Year"), y-Achse = Anzahl ("Count").
plt.plot(df4["Year"], df4["Count"])

# Zeigt das Diagramm an.
plt.show()