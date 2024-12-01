from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


import app.keyboards as kb

router = Router()

class Register(StatesGroup):
    name = State()
    age = State()
    phon_number = State()

#Дикоратор для обработки сообщений
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет', reply_markup=kb.main) # При отправке сообщения "Привет" откроется клавиатура
    await message.reply('как дела? ')


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы нажали на кнопку помощи')

@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберете категорию товара', reply_markup=kb.catalog)

@router.callback_query(F.data == 't-shirt')
async def t_shirt(callback: CallbackQuery ):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Вы выбрали категорию футболок')

@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введите ваше имя ')

@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer('Введите ваш возраст')

@router.message(Register.age)
async def register_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.phon_number)
    await message.answer('Отпрвте ваш номер телефона', reply_markup=kb.get_number)


@router.message(Register.phon_number, F.contact)
async def register_fon_number(message: Message, state: FSMContext):
    await state.update_data(phon_number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f'Ваше имя {data['name']}\nВаш возраст {data['age']}\nВаш номер телефона {data['phon_number']} ')
    await state.clear()
