# TR5UCMN84GRFZ6KK - API key for alpha advantage

from alpha_vantage.timeseries import TimeSeries
import time
# Your key here
key = 'TR5UCMN84GRFZ6KK'
ts = TimeSeries(key)
aapl, meta = ts.get_intraday(symbol='AAPL', interval='1min',outputsize='full')
#while(1):
print aapl
#    time.sleep(5)
