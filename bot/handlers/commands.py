from aiogram.types import Message

from bot.databases.clickhouse import get_db, crud
from bot.main import bot, dp, anti_flood


@dp.message_handler(commands=['start'])
@dp.throttled(anti_flood, rate=3)
async def start_message(message: Message):
    with get_db() as db:
        user = crud.get_user_by_telegram_id(
            db=db,
            telegram_id=message.from_user.id,
            user_name=message.from_user.first_name
        )
    if user.blocked_at:
        text = f"Вы заблокированы.\nДата блокировки {user.blocked_at}." \
               f"\nЕсли вы считаете что были заблокированы по ошибке свяжитесь с администрацией"
        return await message.answer(text=text)

    text = f"Ваш токен для загрузки фото: {user.token}\n" \
           f"Ваш лимит фотографий {user.limit}\n" \
           f"Вы пригласили: {user.refs_count} чел." \
           f"Дата регистрации: {user.created_at}"

    return await message.answer(text)
