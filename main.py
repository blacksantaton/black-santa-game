import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Получаем токен из переменной окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Обработчики команд
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Добро пожаловать в мою игру. Жми /tap, чтобы начать собирать монеты!")

@dp.message_handler(commands=['tap'])
async def tap(message: types.Message):
    await message.reply("Вы собрали 1 монету!")

if __name__ == '__main__':
    # Указание порта по умолчанию (Render ожидает открытые порты)
    port = os.getenv('PORT', 8080)
    print(f"Listening on port {port}...")  # Это будет полезно для дебага
    executor.start_polling(dp, skip_updates=True)
