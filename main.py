import datetime
from analyzing_stocks import analyze_stock
from ticker_symbols import get_symbols
import os
from send_mail import send_email


def main():
    today = str(datetime.date.today())
    year, month, day = [int(x) for x in today.split("-")]
    month_2 = abs(month-6)%12 + 1
    start_date = datetime.datetime(year if month-6>0 else year-1, month_2, 1)
    end_date = datetime.datetime(year, month, 15)
    receiver_email = 'anastasis.papapanagiotou@gmail.com'

    symbols, names = get_symbols()
    if 'results.csv' in os.listdir():
        os.remove('results.csv')
    for s in range(len(symbols)):
        analyze_stock(symbols[s], names[s], start_date, end_date)
    send_email(receiver_email)

main()
