import requests
from bs4 import BeautifulSoup

class Line:
    def __init__(self):
        self.line_notify_token = ''
        self.line_notify_api = 'https://notify-api.line.me/api/notify'

    def sender(self, message):
        payload = {'message': message}
        headers = {'Authorization': 'Bearer ' + self.line_notify_token}
        line_notify = requests.post(self.line_notify_api, data=payload, headers=headers)

def get_stockPrice(code):
    base_url = "https://stocks.finance.yahoo.co.jp/stocks/detail/"
    query = {}
    query["code"] = code + ".T"
    ret = requests.get(base_url, params = query)
    soup =  BeautifulSoup(ret.content, "lxml")
    # print (soup)
    stocktable = soup.find('table', {'class':'stocksTable'})
    symbol = stocktable.findAll('th', {'class':'symbol'})[0].text
    stockPrice = stocktable.findAll('td', {'class': 'stoksPrice'})[1].text
    startPrice = stocktable.findAll('td', {'class':'change'})[0].text
    return symbol, stockPrice, startPrice

if __name__ == "__main__":
    symbol , stockPrice , startPrice= get_stockPrice("4689")
    # print (symbol, stockPrice, startPrice)
    Line().sender(symbol+stockPrice+startPrice)
