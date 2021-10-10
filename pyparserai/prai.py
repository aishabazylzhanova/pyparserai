import requests
from bs4 import BeautifulSoup
class Prai:
    def GetInfo(self, coin):
        self.coin = coin;
        r = requests.get('https://coinmarketcap.com/currencies/'+self.coin)
        htmlParser = BeautifulSoup(r.text, 'html.parser')
        for i in htmlParser.find_all('p'):
            print(i.get_text())
