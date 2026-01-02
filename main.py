import os, random, asyncio, time
from flask import Flask
from threading import Thread
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# --- SERVER FOR 24/7 ---
app = Flask('')
@app.route('/')
def home(): return "SHIVAM JI BOT IS ACTIVE 🟢"

def run(): app.run(host='0.0.0.0', port=os.getenv('PORT', 10000))
def keep_alive(): Thread(target=run, daemon=True).start()

# --- BOT CONFIG ---
TOKEN = '8575823663:AAEcmHcKNy9daZrL8gZc8jTFxorZ1m3ECec'
bot = Bot(token=TOKEN, parse_mode="Markdown")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply("💀 *OMEGA V25 ACTIVE*\n━━━━━━━━━━━━━━\n🔥 *POWERED BY SHIVAM JI*")

@dp.message_handler(commands=['create'])
async def gen(message: types.Message):
    bin_v = message.get_args()[:6] if message.get_args() else "489504"
    res = [f"`{bin_v}{''.join(random.choices('0123456789', k=10))}|{random.randint(1,12):02d}|2028|{random.randint(100,999)}`" for _ in range(10)]
    await message.reply(f"💳 *SHIVAM JI DATA*\n━━━━━━━━━━━━━━\n" + "\n".join(res) + "\n━━━━━━━━━━━━━━\n🔥 *POWERED BY SHIVAM JI*")

if __name__ == '__main__':
    keep_alive()
    executor.start_polling(dp, skip_updates=True)
  
