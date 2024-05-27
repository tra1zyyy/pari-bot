from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio

from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import F
from aiogram.filters.state import StateFilter
from userstates import UserStates
from keyboardhelper import keyboards

import pariservice as ps

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message, state: FSMContext):
    kb = keyboards[UserStates.BASE]
    await  message.answer("Привет, я эхо-бот!", reply_markup=kb)
    await state.set_state(UserStates.BASE)

@dp.message(Command("test"), StateFilter(UserStates.BASE))
async def send_welcome(message: types.Message):
    await message.answer('Я в состоянии BASE')


@dp.message(F.text == "Мои пари", StateFilter(UserStates.BASE))
async def moi_pari(message: types.Message):
    text = "Ваши пари"
    paris = ps.get_paris(message.from_user.id)
    for pari in paris:
        text += "\n" + pari
    await message.answer(text)

@dp.message(F.text == "Создать пари", StateFilter(UserStates.BASE))
async def create_pari(message: types.Message):
    text = ps.add_pari(message.from_user.id, message.text)
    await message.answer(text)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
