import datetime
from config import TOKEN,CHAT_ID
import logging
from aiogram import Bot,Dispatcher,executor,types
from keyboards import *
from get_data import get_data

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
Dp = Dispatcher(bot)
Active_currency =[]
To_active_currency = []
@Dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Вас вітає бот валютник, я буду вам показувати актуальний курс валют.\nВиберіть валюту\nСторінка перша",reply_markup=markup_1)
    await message.answer("Сторінки:",reply_markup=page_markup)
    Active_currency.clear()
@Dp.callback_query_handler(lambda c: c.data.find("page") > -1)
async def change_page(c:types.CallbackQuery):
    page_number = int(c.data.split("_")[1])
    pages = [markup_1,markup_2,markup_3,markup_4,markup_5]
    pages_2 = [to_markup_1,to_markup_2,to_markup_3,to_markup_4,to_markup_5]
    if len(Active_currency)!=0:
        await c.message.answer(f"1 {Active_currency[0]} до\nСторінка {page_number}:\n(щоб відмінити вибір напиши /start або знайди старі кнопки з вибором або вийди і зайди в телеграм)",reply_markup=pages_2[page_number-1])
    else:
        await c.message.answer(f"Сторінка {page_number}:",reply_markup=pages[page_number-1])
    await c.message.answer("Сторінки:",reply_markup=page_markup)
    await c.answer()
@Dp.callback_query_handler(lambda c: c.data.find("to")==-1)
async def choice_of_first_currency(c:types.CallbackQuery):
    for currency ,value in data.items():
        if value== c.data:
            Active_currency.clear()
            await c.message.answer(f"1 {currency} до\nСторінка 1:\n(щоб відмінити вибір напиши /start або знайди старі кнопки з вибором або вийди і зайди в телеграм)",reply_markup=to_markup_1)
            await c.message.answer("Сторінки:",reply_markup=page_markup)
            await c.answer()
            Active_currency.append(currency)
@Dp.callback_query_handler(lambda c: c.data.find("to") >-1)
async def choice_of_second_currency_and_show_ratio(c: types.CallbackQuery):
    if len(Active_currency)==0:
        await c.message.answer("Виберіть перше валюту до якої будете прирівнювати")
    else:
        for currency,value in data.items():
            if "to_"+value == c.data:
                To_active_currency.append(currency)
                if To_active_currency[0] == Active_currency[0]:
                    await c.message.answer("Валюти мають бути різними")
                else:
                    with open("Telegram_bot_currency_dealer/Currencies_data.json",encoding="utf-8") as file:
                        currencies = json.load(file)
                    url = f"https://www.google.com/search?q=ціна+{Active_currency[0]}+в+{To_active_currency[0]}&oq=цін"
                    if currencies["date"] != datetime.datetime.now().strftime("%d_%m"):
                        await get_data(url,Active_currency[0],To_active_currency[0],mode=1)
                        with open("Telegram_bot_currency_dealer/Currencies_data.json",encoding="utf-8") as file:
                            currencies = json.load(file)
                        await c.message.answer(f"1 {Active_currency[0]} дорівнює {currencies[Active_currency[0]][To_active_currency[0]]} {To_active_currency[0]}\n(щоб вибрати знову провишіть /start)")
                    else:
                        if To_active_currency[0] in currencies[Active_currency[0]]:
                            await c.message.answer(f"1 {Active_currency[0]} дорівнює {currencies[Active_currency[0]][To_active_currency[0]]} {To_active_currency[0]}\n(щоб вибрати знову провишіть /start)")
                        else:
                            await get_data(url,Active_currency[0],To_active_currency[0],mode=2)
                            with open("Telegram_bot_currency_dealer/Currencies_data.json",encoding="utf-8") as file:
                                currencies = json.load(file)
                            await c.message.answer(f"1 {Active_currency[0]} дорівнює {currencies[Active_currency[0]][To_active_currency[0]]} {To_active_currency[0]}\n(щоб вибрати знову провишіть /start)")
    Active_currency.clear()
    To_active_currency.clear()

    
if __name__ == "__main__":
    executor.start_polling(Dp,skip_updates=True)
