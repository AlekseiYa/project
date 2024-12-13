from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.database.request import get_categories, get_category_item


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],   #Клавиатура которя высвечиваеться с низу 
                                     [KeyboardButton(text='Корзина')],
                                     [KeyboardButton(text='Контакты'),
                                      KeyboardButton(text='О Нас')]],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню...')



#Инлайн клавиатура 
async def catigories():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f"category_{category.id}"))
    keyboard.add(InlineKeyboardButton(text='НА Главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()  #adjust - регулеровка клавиатуры по ширине т.е. в одном ряду может быть до 2х кнопок
                                            # as_murup - используеться всегда когда используеться билдер, что бы привратить в клавиатуру 



async def items(category_id):
    all_items = await get_category_item(category_id)
    keyboard = InlineKeyboardBuilder()
    for item in all_items:
        keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f"item_{item.id}"))
    keyboard.add(InlineKeyboardButton(text='На Главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()








# catalog = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Футболки', callback_data='t-shirt')],
#     [InlineKeyboardButton(text='Кросовки', callback_data='sneakers')],
#     [InlineKeyboardButton(text='Кепки', callback_data='cap')]])

# get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер', 
#                                                            request_contact=True)]],
#                                             resize_keyboard=True)