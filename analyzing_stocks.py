from write_csv import write_to_csv
import pandas_datareader.data as web


def analyze_stock(ticker_symbol, name, start_date, end_date):
    try:
        stock = web.DataReader(ticker_symbol, 'yahoo', start_date, end_date)

        max_close = max(stock['Adj Close'])
        min_close = min(stock['Adj Close'])
        variable = max_close/min_close
        if variable > 2:
            write_to_csv(name, str(variable)[:4])
    except:
        print("Can't find ticker symbol")
