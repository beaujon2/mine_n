from threading import Thread
import asyncio
from flask import Flask, request
from aiogram import types
from mine2 import bot, dp  # on importe le bot et le dispatcher


WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"https://https://mine-n.onrender.com{WEBHOOK_PATH}"

app = Flask(__name__)

@app.route(WEBHOOK_PATH, methods=["POST"])
async def telegram_webhook():
    update = types.Update.model_validate(await request.get_json())
    await dp.feed_update(bot, update)
    return {"status": "ok"}

async def set_webhook():
    await bot.set_webhook(WEBHOOK_URL)

if __name__ == "__main__":
    asyncio.run(set_webhook())
    app.run(host="0.0.0.0", port=8080)
