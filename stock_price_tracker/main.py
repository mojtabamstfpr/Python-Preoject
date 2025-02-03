import requests
symbol = "AAPL"
url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token=your_api_key"
response = requests.get(url).json()
print(f"Current price of {symbol}: {response['c']}")