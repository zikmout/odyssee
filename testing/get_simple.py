import requests

print(requests.get('https://api.kraken.com/0/public/AssetPairs').json())
