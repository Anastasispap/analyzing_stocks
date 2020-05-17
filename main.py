import datetime
from analyzing_stocks import analyze_stock
from ticker_symbols import get_symbols
import os
start_date = datetime.datetime(2020, 5, 1)
end_date = datetime.datetime(2020, 5, 10)


symbols, names = get_symbols()
if 'results.csv' in os.listdir:
    os.remove('results.csv')
for s in range(len(symbols)):
    analyze_stock(symbols[s], names[s], start_date, end_date)