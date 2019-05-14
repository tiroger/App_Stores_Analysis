import csv
with open('AppleStore.csv', 'r') as inp, open('AppleStore_clean.csv', 'w') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
        if row[1] != "NA":
            writer.writerow(row)

