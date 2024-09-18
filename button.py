from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from baza import Menyu_Sql, Food_Sql, Taomlar, Ichimliklar




menyu = InlineKeyboardBuilder()

for tugma in Menyu_Sql():
    menyu.button(text=f"{tugma[1]}", callback_data=f"{tugma[1]}")
menyu.add(InlineKeyboardButton(text=f"Zakaz berish ", callback_data='zakaz'))
menyu.adjust(2)


taomlar = InlineKeyboardBuilder()

for tugma in Taomlar():
    taomlar.button(text=f"{tugma[1]}", callback_data=f"{tugma[1]}")
# taomlar.add(InlineKeyboardButton(text=f"maxsulot qoshish", callback_data='qoshish'))
taomlar.adjust(3)

ichimliklar = InlineKeyboardBuilder()

for tugma in Ichimliklar():
    ichimliklar.button(text=f"{tugma[1]}", callback_data=f"{tugma[1]}")
# ichimliklar.add(InlineKeyboardButton(text=f"maxsulot qoshish", callback_data='qoshish'))
ichimliklar.adjust(3)


buyurtma_sonlar = InlineKeyboardBuilder()

for i in range(1, 10):
    buyurtma_sonlar.button(text=f"{i}", callback_data=f"{i}")
buyurtma_sonlar.adjust(3)