from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from baza import Menyu_Sql, Food_Sql, Taomlar, Ichimliklar


# Menyu uchun klaviatura
menyu = InlineKeyboardBuilder()

for tugma in Menyu_Sql():
    menyu.button(text=f"{tugma[1]}", callback_data=f"{tugma[1]}")
menyu.add(InlineKeyboardButton(text=f"Zakaz berish ", callback_data='zakaz'))
menyu.adjust(2)





# Taomlar uchun klaviatura
taomlar = InlineKeyboardBuilder()



for tugma in Taomlar():
    taomlar.button(text=f"{tugma[1]}", callback_data=f"{tugma[1]}")
taomlar.adjust(3)

# Ichimliklar uchun klaviatura
ichimliklar = InlineKeyboardBuilder()

for tugma in Ichimliklar():
    ichimliklar.button(text=f"{tugma[1]}", callback_data=f"{tugma[1]}")
ichimliklar.adjust(3)

# Buyurtma sonlari uchun klaviatura
buyurtma_sonlar = InlineKeyboardBuilder()

for i in range(1, 10):
    buyurtma_sonlar.button(text=f"{i}", callback_data=f"{i}")
buyurtma_sonlar.adjust(3)