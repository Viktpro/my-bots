import logging
import os
import sys
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Токен
TOKEN = os.environ.get('PORTFOLIO_TOKEN', '8088348800:AAEgsVU7x1w-9FBr1gS9Xx74e_sVbYyBHzU')

# Логирование
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger()


# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("👩‍💻 Обо мне", callback_data='about')],
        [InlineKeyboardButton("🤖 Мои боты", callback_data='bots')],
        [InlineKeyboardButton("📞 Контакты", callback_data='contacts')],
    ]
    await update.message.reply_text(
        "🌟 Привет! Я бот-портфолио Вики",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# Кнопки
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'about':
        await query.edit_message_text("👩‍💻 Вика, 15 лет, Python-разработчик")
    elif query.data == 'bots':
        kb = [[InlineKeyboardButton("🤖 Нейробот", url="https://t.me/vika_neiro_bot")],
              [InlineKeyboardButton("🔙 Назад", callback_data='back')]]
        await query.edit_message_text("Мои боты:", reply_markup=InlineKeyboardMarkup(kb))
    elif query.data == 'contacts':
        await query.edit_message_text("📱 @vika_pro")
    elif query.data == 'back':
        await start(query.message, context)


# Запуск
def main():
    if not TOKEN:
        logger.error("Нет токена!")
        sys.exit(1)

    print(f"🚀 Запуск бота {TOKEN[:8]}...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("✅ Бот запущен!")
    app.run_polling()


if __name__ == '__main__':
    main()