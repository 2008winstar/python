import datetime
import numpy as np


def datestr2num(s):
    s = str(s, encoding='utf-8')
    return datetime.datetime.strptime(s, '%d-%m-%Y').date().weekday()


dates, close = np.loadtxt('data.csv', delimiter=',', usecols=(1, 6), converters={1: datestr2num}, unpack=True)
averages = np.zeros(5)

for i in range(5):
    indices = np.where(dates == i)
    prices = np.take(close, indices)
    avg = np.mean(prices)
    print('Day', i, 'prices', prices, 'average', avg)
    averages[i] = avg
