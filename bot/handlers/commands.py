from typing import Optional, Union

from aiogram.types import Message

from bot.api.photos import get_random_photo
from bot.databases.clickhouse import get_db, crud
from bot.main import bot, dp, anti_flood
from bot.schemas.photo import VkPhoto


@dp.message_handler(commands=['start'])
@dp.throttled(anti_flood, rate=3)
async def start_message(message: Message):
    with get_db() as db:
        user = crud.get_user(db, message)

    if user.blocked_at:
        text = f"Вы заблокированы.\nДата блокировки {user.blocked_at}." \
               f"\nЕсли вы считаете что были заблокированы по ошибке свяжитесь с администрацией"
        return await message.answer(text=text)

    text = f"Ваш токен для загрузки фото: {user.token}\n" \
           f"Ваш лимит фотографий {user.limit}\n" \
           f"Вы пригласили: {user.refs_count} чел." \
           f"Дата регистрации: {user.created_at}"

    return await message.answer(text)


@dp.message_handler(commands=['rand'])
@dp.throttled(anti_flood, rate=1)
async def random_photo(message: Message):
    with get_db() as db:
        user = crud.get_user(db, message)

    photo: Union[VkPhoto, dict] = await get_random_photo(user.token, ignore_groups=False)

    if not type(photo) is VkPhoto:
        return await message.answer(photo.get('detail', 'some error'))

    return await message.answer(text=photo.get_text_for_message())


@dp.message_handler(commands=['rand_pm'])
@dp.throttled(anti_flood, rate=1)
async def random_photo(message: Message):
    with get_db() as db:
        user = crud.get_user(db, message)

    photo: Union[VkPhoto, dict] = await get_random_photo(user.token, ignore_groups=True)

    if not type(photo) is VkPhoto:
        return await message.answer(photo.get('detail', 'some error'))

    return await message.answer(text=photo.get_text_for_message())
