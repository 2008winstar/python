import csv
import time
import os

field_order = ['date', 'last_trade', 'change', 'ah_price', 'ah_change']
fields = {
    'date': 'Date',
    'last_trade': 'Last Trade',
    'change': 'Change',
    'ah_price': 'After Hours Price',
    'ah_change': 'After Hours Change'
}


def write_row(ticker_name, stock_values):
    file_name = 'stocktracker-' + ticker_name + '.csv'
    if os.access(file_name, os.F_OK):
        file_mode = 'ab'
    else:
        file_mode = 'wb'
    csv_writer = csv.DictWriter(open(file_name, file_mode), fieldnames=field_order, extrasaction='ignore')
    if file_mode == 'wb':
        csv_writer.writerow(fields)
    csv_writer.writerow(stock_values)
if __name__ == '__main__':
    stock = {'last_trade': 1, 'change': 2, 'ah_price': 3, 'ah_change': 4}
    stock['date'] = time.strftime('%Y-%m-%d %H:%M')
    write_row('GOOG', stock)
    print stock






















