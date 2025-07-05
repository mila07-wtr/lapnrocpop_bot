import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random

load_dotenv()

TOKEN = os.getenv("TOKEN")

if TOKEN is None:
    raise ValueError("Токен не найден! Проверь файл .env и его расположение")


greetings = [
    "Привет, друг! 🍿 Готов обсудить киношку?",
    "О, киношный гость! Что сегодня ищем: драмы, комедии или что-то душевное?",
    "Добро пожаловать в PopcornPal 🍿 — твой уютный киногид с юмором!"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(greetings))

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    
    if "грустно" in text or "плачу" in text:
        await update.message.reply_text("Обнимаю 🤗 Советую 'Виноваты звёзды' 🌟")
    elif "весело" in text or "улыбка" in text:
        await update.message.reply_text("Ты как солнышко сегодня! ☀️ Попробуй 'Мы – Миллеры' ��")
    elif "любовь" in text or "романтика" in text:
        await update.message.reply_text("О, любовь витает в воздухе! 💕 Глянь 'До встречи с тобой' или 'Ла-Ла Ленд'")
    else:
        await update.message.reply_text("Скажи, какое у тебя настроение или жанр? Я подскажу 🎬")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("PopcornPal запущен...")
app.run_polling()


