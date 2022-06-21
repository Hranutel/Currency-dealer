import json
from locale import currency
import requests
from bs4 import BeautifulSoup
import datetime
from keyboards import data
# with open("Telegram_bot_currency_dealer\currencies.json",encoding="utf-8") as file:
#     currencies_data = json.load(file)
# currencies = {}
# currencies["date"]=datetime.datetime.now().strftime("%d_%m")
# for currency in currencies_data:
#     currencies[currency]={}
# with open("Telegram_bot_currency_dealer\Currencies_data.json","w",encoding="utf-8") as file:
#     json.dump(currencies,file,indent=4,ensure_ascii=False)
async def get_data(url,currency,to_currency,mode):
    headers ={
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
    "accept" : "*/*"
    }
    req =  requests.get(url,headers=headers)
    soup = BeautifulSoup(req.text,"lxml")
    Cost = soup.find("div",class_="dDoNo").find_next().text.strip()
    if mode == 1:
        currencies={}
        currencies["date"] = datetime.datetime.now().strftime("%d_%m")
        for currency in data:
            currencies[currency]={}
        currencies[currency][to_currency]=Cost
    else:
        with open("Telegram_bot_currency_dealer/Currencies_data.json",encoding="utf-8")as file:
            currencies = json.load(file)
        currencies[currency][to_currency]=Cost
    with open("Telegram_bot_currency_dealer/Currencies_data.json","w",encoding="utf-8") as file:
        json.dump(currencies,file,indent=4,ensure_ascii=False)


