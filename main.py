from aiogram import Bot, Dispatcher, executor, types
import logging
import functions as fn

API_TOKEN = '5425362241:AAExEwOYjtsBGBsac4mfKZOpCDF1BOaXWz8'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
TEXT = ''
flag = 'encrypt'


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(f"Hi!\nI'm EncryptBot!\nI can encrypt and decrypt messages with couple of interesting cyphers\n"
                        f"Use {'/help'} for a list of commands")


@dp.message_handler(commands=['encrypt', 'decrypt'])
async def send_welcome(message: types.Message):
    global TEXT, flag
    await message.reply('Choose cypher:\n'
                        '/Morse\n/Caesar\n/XOR\n/QR')
    if 'encrypt' in message.text:
        flag = 'encrypt'
    if 'decrypt' in message.text:
        flag = 'decrypt'


@dp.message_handler(commands=['Morse'])
async def send_welcome(message: types.Message):
    global TEXT, flag
    if flag == 'encrypt':
        await message.reply(fn.morse_encode(TEXT))
    else:
        if TEXT[0] in fn.rus_alph:
            await message.reply(fn.morse_decode(TEXT, 'Russian'))
        else:
            await message.reply(fn.morse_decode(TEXT, 'English'))


@dp.message_handler()
async def send_welcome(message: types.Message):
    global TEXT
    TEXT = message.text
    if '/' not in message.text:
        await message.reply('Do you want to /encrypt or /decrypt a message')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
