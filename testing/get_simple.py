import requests
import json

#r = requests.get('https://api.kraken.com/0/public/OHLC?pair=XXBTZUSD&since=0')
r = requests.get('https://api.kraken.com/0/public/Trades?pair=XXBTZUSD&since=0')
data = json.loads(r.content)

print '\nprint last :\n'
#print data['result']['last']

#print '\nprint result :\n'

#print data['result']['XXBTZUSD']
for key, value in data['result'].iteritems() :
    # result & last
    print key

print '\nprint resulst XXBTZUSD :\n'
for key2, value2 in data['result'].iteritems() :
    print key2
    print value2
#print data['result']['XXBTZUSD']

#print 'Now what we are looking for:'

