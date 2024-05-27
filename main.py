from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio

from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.state import StateFilter
from userstates import UserStates
from keyboardhelper import keyboards

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message, state: FSMContext):
    kb = keyboards[UserStates.BASE]
    await bot.send_message(message.chat.id, "Привет, я эхо-бот!", reply_markup=kb)
    await state.set_state(UserStates.BASE)

@dp.message(Command("test"), StateFilter(UserStates.BASE))
async def send_welcome(message: types.Message):
    await message.answer('Я в состоянии BASE')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
