import logging
from aiogram import Bot, Dispatcher, executor, types
from conf import TOKEN, ALLOWED_USERS
from db import Database

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

db = Database('db.sqlite3')


@dp.message_handler(commands="start")
async def start(message: types.Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, 'Your Login')
    # else:
    #     await bot.send_message(message.from_user.id, 'You are registered!')


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text in ALLOWED_USERS.keys():
            await bot.send_message(message.from_user.id, 'Your id')
        else:
            await bot.send_message(message.from_user.id, 'Access denied')
        if message.text in ALLOWED_USERS.values():
            if message.text == '1799244985':
                await bot.send_message(message.from_user.id, 'Your login: bogdan \nYour password: asqw1290 \nLInk: http://127.0.0.1:8080/')
            elif message.text == '1836086969':
                await bot.send_message(message.from_user.id, 'Your login: lovelas \nYour password: ewqdsa321 \nLInk: http://127.0.0.1:8080/')



        # else:
        #     if db.get_signup(message.from_user.id) == 'setnickname':
        #         if len(message.text) > 15:
        #             await bot.send_message(message.from_user.id, '>10')
        #         elif '@' in message.text or '/' in message.text:
        #             await bot.send_message(message.from_user.id, 'Incorrect symbol')
        #         else:
        #             db.set_login(message.from_user.id, message.text)
        #             db.set_signup(message.from_user.id, 'Done')
        #             await bot.send_message(message.from_user.id, 'Registration was successful')
        #     else:
        #         await bot.send_message(message.from_user.id, 'What?')



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
