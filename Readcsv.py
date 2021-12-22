import configparser
import csv
config = configparser.RawConfigParser()
config.read('ConfigFile.properties')

filename = config.get('Filename', 'filepath')


fields = []
rows = []
try:
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)

        for row in csvreader:
            rows.append(row)

except Exception as error:
    print("Error in exception:", error)
for row in rows[:len(rows)]:
    # parsing each column of a row
    print(row)

