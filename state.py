from aiogram.fsm.state import State, StatesGroup


class Food(StatesGroup):
    menyu = State()
    taomlar = State()
    ichimliklar = State()
    soni = State()