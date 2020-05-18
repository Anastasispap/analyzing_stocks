from write_csv import write_to_csv
import pandas_datareader.data as web

max_var = -1


def analyze_stock(ticker_symbol, name, start_date, end_date):
    try:
        stock = web.DataReader(ticker_symbol, 'yahoo', start_date, end_date)
        high = [x for x in stock['High']]
        low = [x for x in stock['Low']]
        max_stock = max(high)
        low = min(low)
        variable = max_stock/low
        write_to_csv(name, variable)
    except:
        print("Can't find ticker symbol")
