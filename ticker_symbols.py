import csv


def get_symbols():
    symbols = []
    names = []
    with open('companylist.csv') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for i, row in enumerate(csv_reader):
            if i != 0:
                symbols.append(row[0])
                names.append(row[1])

    return symbols, names