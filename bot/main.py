import asyncio
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor
from bot.settings import settings

loop = asyncio.get_event_loop()
bot = Bot(settings.bot_token, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage, loop=loop)


async def anti_flood(*args, **kwargs):
    m = args[0]
    await m.answer("Не флуди...")


async def send_to_admin(dp):
    await bot.send_message(chat_id=settings.admin_id, text=f"bot_started")


def start():
    from bot.handlers.commands import dp
    executor.start_polling(dp, on_startup=send_to_admin)
    import bot.handlers
