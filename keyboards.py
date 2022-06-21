import json
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
# import requests
# from urllib.parse import unquote
# from bs4 import BeautifulSoup
# url=unquote("https://www.google.com/search?q=%D1%86%D1%96%D0%BD%D0%B0+%D1%80%D1%83%D0%B1%D0%BB%D1%8F+%D0%B4%D0%BE+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D1%96&oq=%D1%86%D1%96%D0%BD%D0%B0&aqs=chrome.1.69i57j35i39l2j46i131i433i512j0i433i512j0i131i433i512j0i512j0i433i512j0i512l2.6000j1j15&sourceid=chrome&ie=UTF-8").split("&aqs")[0]

# headers ={
#     "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
#     "accept" : "*/*"
# }
# all_currencies = {}
# print(url)
# req = requests.get(url,headers=headers)
# soup = BeautifulSoup(req.text,"lxml")
# for currency in enumerate(soup.find("select",class_="l84FKc").find_all("option")):
#     all_currencies[currency[1].text]=str(currency[0])
# with open("Telegram_bot_currency_dealer/currencies.json","w",encoding="utf-8") as file:
#     json.dump(all_currencies,file,indent=4,ensure_ascii=False)

with open("Telegram_bot_currency_dealer\currencies.json",encoding="utf-8") as file:
    data=json.load(file)
markup_1 = InlineKeyboardMarkup(row_width=2)
markup_2 = InlineKeyboardMarkup(row_width=2)
markup_3 = InlineKeyboardMarkup(row_width=2)
markup_4 = InlineKeyboardMarkup(row_width=2)
markup_5 = InlineKeyboardMarkup(row_width=2)

to_markup_1 = InlineKeyboardMarkup(row_width=2)
to_markup_2 = InlineKeyboardMarkup(row_width=2)
to_markup_3 = InlineKeyboardMarkup(row_width=2)
to_markup_4 = InlineKeyboardMarkup(row_width=2)
to_markup_5 = InlineKeyboardMarkup(row_width=2)

page_markup = InlineKeyboardMarkup(row_width=3)
page_markup.insert(InlineKeyboardButton("1️⃣",callback_data="page_1"))
page_markup.insert(InlineKeyboardButton("2️⃣",callback_data="page_2"))
page_markup.insert(InlineKeyboardButton("3️⃣",callback_data="page_3"))
page_markup.insert(InlineKeyboardButton("4️⃣",callback_data="page_4"))
page_markup.insert(InlineKeyboardButton("5️⃣",callback_data="page_5"))
markup_1_list_amount = 0
markup_2_list_amount = 0
markup_3_list_amount = 0
markup_4_list_amount = 0
for name,value in data.items():
    if markup_1_list_amount != 30:
        markup_1.insert(InlineKeyboardButton(f"1 {name}",callback_data=value))
        markup_1_list_amount += 1
    else:
        if markup_2_list_amount!=30:
            markup_2.insert(InlineKeyboardButton(f"1 {name}",callback_data=value))
            markup_2_list_amount +=1
        else:
            if markup_3_list_amount !=30:
                markup_3.insert(InlineKeyboardButton(f"1 {name}",callback_data=value))
                markup_3_list_amount +=1
            else:
                if markup_4_list_amount!=30:
                    markup_4.insert(InlineKeyboardButton(f"1 {name}",callback_data=value))
                    markup_4_list_amount +=1
                else:
                    markup_5.insert(InlineKeyboardButton(f"1 {name}",callback_data=value))    

to_markup_1_list_amount = 0
to_markup_2_list_amount = 0
to_markup_3_list_amount = 0
to_markup_4_list_amount = 0
for name,value in data.items():
    if to_markup_1_list_amount != 30:
        to_markup_1.insert(InlineKeyboardButton(f"До {name}",callback_data=f"to_{value}"))
        to_markup_1_list_amount += 1
    else:
        if to_markup_2_list_amount!=30:
            to_markup_2.insert(InlineKeyboardButton(f"До {name}",callback_data=f"to_{value}"))
            to_markup_2_list_amount +=1
        else:
            if to_markup_3_list_amount !=30:
                to_markup_3.insert(InlineKeyboardButton(f"До {name}",callback_data=f"to_{value}"))
                to_markup_3_list_amount +=1
            else:
                if to_markup_4_list_amount!=30:
                    to_markup_4.insert(InlineKeyboardButton(f"До {name}",callback_data=f"to_{value}"))
                    to_markup_4_list_amount +=1
                else:
                    to_markup_5.insert(InlineKeyboardButton(f"До {name}",callback_data=f"to_{value}")) 