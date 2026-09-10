#Bestimmung der Anzahl unterschiedlicher Vornamen aus einer CSV-Datei mithilfe eines Sets

import csv  # Imports the csv module so we can read CSV files

# Creates an empty set.
# A set stores only unique values, so duplicate names are automatically removed.
names = set()

# Opens the CSV file.
# newline='' is recommended when working with CSV files.
with open("C:/Users/Administrator/Desktop/Python kurs/Kursmaterialien/data/names.csv", newline='') as csvfile:

    # Creates a CSV reader.
    # delimiter="," means the columns are separated by commas.
    # quotechar='"' means text can be surrounded by quotation marks.
    namereader = csv.reader(csvfile, delimiter=",", quotechar='"')

    # Counter to keep track of the current row
    counter = 0

    # Goes through the CSV file row by row
    for row in namereader:

        # Skip the first row because it contains the column headings
        if counter != 0:

            # Add the value from the second column (index 1) to the set
            # Duplicate names will not be added twice
            names.add(row[1])

        # Increase the counter after every row
        counter = counter + 1

# Print the number of unique names found in the second column
print("Bestimmung der Anzahl unterschiedlicher Vornamen aus einer CSV-Datei mithilfe eines Sets")
print(len(names))