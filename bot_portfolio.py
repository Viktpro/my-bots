import logging
import os
import asyncio
import sys
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from telegram.request import HTTPXRequest
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

# Токен для портфолио бота
TOKEN = os.environ.get('PORTFOLIO_TOKEN', '8088348800:AAEgsVU7x1w-9FBr1gS9Xx74e_sVbYyBHzU')
PROXY = os.environ.get('PROXY')  # Например: socks5://127.0.0.1:9150

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Главное меню портфолио"""
    user = update.effective_user
    user_name = user.first_name if user.first_name else "Гость"

    # Создаём красивое меню
    keyboard = [
        [InlineKeyboardButton("👩‍💻 Обо мне", callback_data='about')],
        [InlineKeyboardButton("🛠 Мои проекты", callback_data='projects')],
        [InlineKeyboardButton("🤖 Мои боты", callback_data='bots')],
        [InlineKeyboardButton("📊 Навыки", callback_data='skills')],
        [InlineKeyboardButton("📞 Контакты", callback_data='contacts')],
        [InlineKeyboardButton("📁 GitHub", url="https://github.com/Viktpro")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"🌟 <b>Привет, {user_name}!</b>\n\n"
        "Я <b>Вика</b> — Python-разработчик, специалист по Telegram-ботам и нейросетям.\n"
        "Мне 15 лет, и я уже создаю крутые проекты!\n\n"
        "👇 <b>Выбери раздел:</b>",
        parse_mode='HTML',
        reply_markup=reply_markup
    )

    logger.info(f"Пользователь {user.id} ({user_name}) запустил портфолио")


# Обработчик кнопок
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user = update.effective_user
    logger.info(f"Пользователь {user.id} нажал: {query.data}")

    if query.data == 'about':
        text = (
            "👩‍💻 <b>Обо мне</b>\n\n"
            "• Возраст: 15 лет\n"
            "• Город: РФ\n"
            "• Специализация: Python-разработчик\n\n"
            "🏆 <b>Достижения:</b>\n"
            "• Финалистка чемпионата «Профессионалы» по нейросетям\n"
            "• Окончила курс «Код будущего» от МФТИ с отличием\n"
            "• Участница хакатонов\n"
            "• 5+ успешных заказов на биржах\n\n"
            "💡 <b>Что я делаю:</b>\n"
            "• Telegram-боты любой сложности\n"
            "• Интеграция нейросетей (GigaChat, OpenAI)\n"
            "• Сайты-визитки\n"
            "• Помощь с Arduino\n\n"
            "🔙 /start"
        )
        await query.edit_message_text(text, parse_mode='HTML')

    elif query.data == 'projects':
        text = (
            "🛠 <b>Мои проекты</b>\n\n"
            "1️⃣ <b>Навигатор для школы</b>\n"
            "   • Flask, карты, QR-коды\n"
            "   • Помогает ученикам находить кабинеты\n\n"
            "2️⃣ <b>AI-ассистент на GigaChat</b>\n"
            "   • Интеграция с нейросетью Сбера\n"
            "   • Умный бот с 6 моделями\n\n"
            "3️⃣ <b>Elly Stats Bot</b>\n"
            "   • Аналитика видео для блогеров\n"
            "   • @elly_stats_bot\n\n"
            "4️⃣ <b>Генератор паролей</b>\n"
            "   • Веб-приложение на Flask\n"
            "   • Настраиваемые параметры\n\n"
            "🔙 /start"
        )
        await query.edit_message_text(text, parse_mode='HTML')

    elif query.data == 'bots':
        # Клавиатура для ботов
        keyboard = [
            [InlineKeyboardButton("🤖 Нейробот Вики", url="https://t.me/vika_neiro_bot")],
            [InlineKeyboardButton("📊 Elly Stats", url="https://t.me/elly_stats_bot")],
            [InlineKeyboardButton("🔙 Назад", callback_data='back_to_main')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        text = (
            "🤖 <b>Мои Telegram-боты</b>\n\n"
            "1️⃣ <b>@vika_neiro_bot</b>\n"
            "   • 6 AI-моделей (GigaChat, DeepSeek, Mistral, Llama, Qwen, Gemma)\n"
            "   • Распознавание фото\n"
            "   • Заметки, статистика\n"
            "   • Умный ассистент\n\n"
            "2️⃣ <b>@elly_stats_bot</b>\n"
            "   • Аналитика видео\n"
            "   • Статистика просмотров\n"
            "   • Для блогеров\n\n"
            "👇 <b>Нажми на кнопку, чтобы открыть бота:</b>"
        )
        await query.edit_message_text(text, parse_mode='HTML', reply_markup=reply_markup)

    elif query.data == 'skills':
        text = (
            "📊 <b>Мои навыки</b>\n\n"
            "🐍 <b>Python:</b>\n"
            "• aiogram, python-telegram-bot\n"
            "• Flask, Django (базово)\n"
            "• Работа с API\n"
            "• Базы данных (SQLite, PostgreSQL)\n\n"
            "🤖 <b>AI и нейросети:</b>\n"
            "• GigaChat API\n"
            "• OpenAI\n"
            "• Распознавание изображений\n\n"
            "🌐 <b>Web:</b>\n"
            "• HTML/CSS\n"
            "• Flask\n\n"
            "🔧 <b>Инструменты:</b>\n"
            "• Git, GitHub\n"
            "• Render, Railway\n"
            "• Arduino, Wokwi\n\n"
            "🔙 /start"
        )
        await query.edit_message_text(text, parse_mode='HTML')

    elif query.data == 'contacts':
        keyboard = [
            [InlineKeyboardButton("📱 Telegram", url="https://t.me/vika_pro")],
            [InlineKeyboardButton("📧 Email", url="mailto:vikaprohor0101@gmail.com")],
            [InlineKeyboardButton("💻 GitHub", url="https://github.com/Viktpro")],
            [InlineKeyboardButton("🛒 Kwork", url="https://kwork.ru/user/vika_pro")],
            [InlineKeyboardButton("🔙 Назад", callback_data='back_to_main')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        text = (
            "📞 <b>Контакты</b>\n\n"
            "📍 Telegram: @vika_pro\n"
            "📧 Email: vikaprohor0101@gmail.com\n"
            "🐙 GitHub: github.com/Viktpro\n"
            "💰 Kwork: kwork.ru/user/vika_pro\n\n"
            "👇 <b>Нажми на кнопку для связи:</b>"
        )
        await query.edit_message_text(text, parse_mode='HTML', reply_markup=reply_markup)

    elif query.data == 'back_to_main':
        keyboard = [
            [InlineKeyboardButton("👩‍💻 Обо мне", callback_data='about')],
            [InlineKeyboardButton("🛠 Мои проекты", callback_data='projects')],
            [InlineKeyboardButton("🤖 Мои боты", callback_data='bots')],
            [InlineKeyboardButton("📊 Навыки", callback_data='skills')],
            [InlineKeyboardButton("📞 Контакты", callback_data='contacts')],
            [InlineKeyboardButton("📁 GitHub", url="https://github.com/Viktpro")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(
            "🌟 <b>Портфолио Вики</b>\n\n"
            "Python-разработчик, специалист по Telegram-ботам и нейросетям.\n\n"
            "👇 <b>Выбери раздел:</b>",
            parse_mode='HTML',
            reply_markup=reply_markup
        )


# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔍 <b>Команды:</b>\n\n"
        "/start - Главное меню\n"
        "/help - Эта справка\n"
        "/projects - Мои проекты\n"
        "/bots - Telegram-боты\n"
        "/skills - Навыки\n"
        "/contacts - Контакты",
        parse_mode='HTML'
    )


# Команда /projects
async def projects_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛠 <b>Мои проекты</b>\n\n"
        "• Навигатор для школы (Flask)\n"
        "• AI-ассистент на GigaChat\n"
        "• Elly Stats Bot (@elly_stats_bot)\n"
        "• Нейробот Вики (@vika_neiro_bot)\n"
        "• Генератор паролей\n\n"
        "Подробнее в /start меню",
        parse_mode='HTML'
    )


# Команда /skills
async def skills_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 <b>Навыки:</b>\n\n"
        "• Python, Flask, aiogram\n"
        "• GigaChat, OpenAI\n"
        "• Git, GitHub\n"
        "• HTML/CSS\n"
        "• Arduino\n\n"
        "Подробнее в /start меню",
        parse_mode='HTML'
    )


# Команда /contacts
async def contacts_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📱 Telegram", url="https://t.me/vika_pro")],
        [InlineKeyboardButton("📧 Email", url="mailto:vikaprohor0101@gmail.com")],
        [InlineKeyboardButton("💻 GitHub", url="https://github.com/Viktpro")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "📞 <b>Контакты:</b>\n\n"
        "Telegram: @vika_pro\n"
        "Email: vikaprohor0101@gmail.com\n"
        "GitHub: github.com/Viktpro",
        parse_mode='HTML',
        reply_markup=reply_markup
    )


# ФУНКЦИЯ ЗАПУСКА БОТА
async def run_bot():
    """Асинхронный запуск бота"""
    logger.info(f"🚀 Запуск бота с токеном: {TOKEN[:8]}...")

    # Создаём приложение с поддержкой прокси если нужно
    if PROXY:
        logger.info(f"🔌 Использую прокси: {PROXY}")
        request = HTTPXRequest(proxy_url=PROXY, connection_pool_size=10)
        app = Application.builder().token(TOKEN).request(request).build()
    else:
        app = Application.builder().token(TOKEN).build()

    # Добавляем обработчики
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("projects", projects_command))
    app.add_handler(CommandHandler("skills", skills_command))
    app.add_handler(CommandHandler("contacts", contacts_command))
    app.add_handler(CallbackQueryHandler(button_handler))

    logger.info("✅ Обработчики добавлены")

    # Инициализация и запуск
    await app.initialize()
    await app.start()

    # Запуск polling
    logger.info("🔄 Запуск polling...")
    await app.updater.start_polling()

    logger.info("🚀 Бот успешно запущен и готов к работе!")

    # Держим бота запущенным
    try:
        while True:
            await asyncio.sleep(3600)  # Спим час
    except asyncio.CancelledError:
        logger.info("🛑 Получен сигнал остановки")
        # Корректное завершение
        await app.updater.stop()
        await app.stop()
        await app.shutdown()


def main():
    """Точка входа"""
    if not TOKEN:
        logger.error("❌ Ошибка: токен не найден!")
        sys.exit(1)

    logger.info("=" * 50)
    logger.info("🚀 ЗАПУСК БОТА ПОРТФОЛИО")
    logger.info(f"📱 Бот: @vika_pro_portfolio_bot")
    logger.info(f"🔑 Токен: {TOKEN[:8]}...{TOKEN[-4:]}")
    logger.info("=" * 50)

    try:
        # Создаём и устанавливаем цикл событий
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        # Запускаем бота
        loop.run_until_complete(run_bot())

    except KeyboardInterrupt:
        logger.info("🛑 Бот остановлен пользователем (Ctrl+C)")
    except Exception as e:
        logger.error(f"❌ Критическая ошибка: {e}")
        import traceback
        logger.error(traceback.format_exc())
        sys.exit(1)
    finally:
        logger.info("👋 Бот завершил работу")


if __name__ == '__main__':
    main()