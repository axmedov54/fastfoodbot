import asyncio
import logging
import sys
import sqlite3
from aiogram import Bot, Dispatcher, html, F,types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from config import BOT_TOKEN as token
from button import menyu, taomlar, ichimliklar, buyurtma_sonlar
from baza import Food_Sql
from state import Food
import time


TOKEN = token
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))



dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Assalom Aleykum, {html.bold(message.from_user.full_name)}!", reply_markup=menyu.as_markup())




@dp.callback_query(F.data, Food.menyu)
async def Taomlar(call: CallbackQuery, state: FSMContext):
    mijoz_taom = call.data
    await state.update_data({
        "taom":mijoz_taom
    })
    if mijoz_taom == "Ichimliklar":
        for taom in Food_Sql():
            if taom[0] == 1:
                await call.message.answer_photo(photo="https://uzbekistan.travel/storage/app/media/nargiza/cropped-images/kuhnyaj-0-0-0-0-1589979425.jpg", caption="ajoyib", reply_markup=taomlar.as_markup())
                await state.set_state(Food.ichimliklar)
    elif mijoz_taom == "Taomlar":
        for taom in Food_Sql():
            if taom[0] == 2:
                await call.message.answer_photo(photo="https://uzbekistan.travel/storage/app/media/nargiza/cropped-images/kuhnyaj-0-0-0-0-1589979425.jpg", caption="ajoyib", reply_markup=ichimliklar.as_markup())
                await state.set_state(Food.taomlar)


@dp.callback_query(F.data, Food.taomlar)
async def Taomlar(call: CallbackQuery, state: FSMContext):
    taomlar_royhat = call.data
    await state.update_data({
        'taomlar_royhat':taomlar_royhat
    })
    for taom in Food_Sql():
           if taom[1] == taomlar_royhat:
                await call.message.answer_photo(photo='https://t.me/xivabotuchun/736',caption=f"Taomlar: {taom[1]}\nNechta olasiz\nNarxi: {taom[2]} so'm", reply_markup=buyurtma_sonlar.as_markup())
                await state.set_state(Food.soni)    

@dp.callback_query(F.data, Food.ichimliklar)
async def Ichimliklar(call: CallbackQuery, state: FSMContext):
    taomlar_royhat = call.data
    await state.update_data({
        'taomlar_royhat':taomlar_royhat
    })
    for taom in Food_Sql():
            if taom[1] == taomlar_royhat:
                await call.message.answer_photo(photo='https://t.me/xivabotuchun/736', caption=f"Taomlar: {taom[1]}\nNechta olasiz\nNarxi: {taom[2]} so'm", reply_markup=buyurtma_sonlar.as_markup())
                await state.set_state(Food.soni)    


@dp.callback_query(F.data, Food.soni)
async def Taomlar_Zakaz(call: CallbackQuery, state: FSMContext):
    sonlar = call.data
    await state.update_data({
        'sonlar':sonlar
    })
    await call.answer("Buyurtma savatga qo`shildi ")
    time.sleep(2)
    await call.message.answer_photo(photo="https://uzbekistan.travel/storage/app/media/nargiza/cropped-images/kuhnyaj-0-0-0-0-1589979425.jpg", caption=f" Menyu", reply_markup=menyu.as_markup())
    await state.set_state(Food.state_menyu)



@dp.callback_query(F.data == "zakaz")
async def Karzinka(call: CallbackQuery):
 pass
    





async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


