import csv


def write_to_csv(name, variable):
    with open('results.csv', 'a') as file:
        stock_w = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        stock_w.writerow([name, variable])