from aiogram import Bot, Dispatcher, types

from asyncio import run

import asyncio


dp = Dispatcher()


async def startup_answer(bot: Bot):
    await bot.send_message(921347523, "Bot ishga tushdi! ✅")


async def shutdown_answer(bot: Bot):
    await bot.send_message(921347523, "Bot ishdan to'xtadi! ❌")



async def echo(message: types.Message, bot: Bot):
    await message.copy_to(chat_id=message.chat.id)


async def start():
    dp.startup.register(startup_answer)
    dp.message.register(echo)
    dp.shutdown.register(shutdown_answer)
    bot = Bot("7611119839:AAHdiDZ9-olh2EldSCKdE6ktewlhFYvIs3M")
    await dp.start_polling(bot, polling_timeout=1)


print("The bot is running!")

run(start())

