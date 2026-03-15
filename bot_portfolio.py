import logging
import os
import sys
import traceback
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from dotenv import load_dotenv

# Загружаем переменные из .env файла (для локального запуска)
load_dotenv()

# Токен из переменных окружения (на Render задаётся через Dashboard)
TOKEN = os.environ.get('PORTFOLIO_TOKEN')

# Настройка логирования (максимально подробно)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,  # DEBUG уровень для максимальной информации
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('bot.log')  # Сохраняем логи в файл
    ]
)
logger = logging.getLogger(__name__)


# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Главное меню портфолио"""
    try:
        user = update.effective_user
        user_name = user.first_name if user.first_name else "Гость"

        logger.info(f"Пользователь {user.id} ({user_name}) запустил бота")

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
    except Exception as e:
        logger.error(f"Ошибка в start: {e}")
        logger.error(traceback.format_exc())


# Обработчик кнопок
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
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
    except Exception as e:
        logger.error(f"Ошибка в button_handler: {e}")
        logger.error(traceback.format_exc())


# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
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
    except Exception as e:
        logger.error(f"Ошибка в help_command: {e}")


# Команда /projects
async def projects_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
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
    except Exception as e:
        logger.error(f"Ошибка в projects_command: {e}")


# Команда /skills
async def skills_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
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
    except Exception as e:
        logger.error(f"Ошибка в skills_command: {e}")


# Команда /contacts
async def contacts_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
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
    except Exception as e:
        logger.error(f"Ошибка в contacts_command: {e}")


# Главная функция
def main():
    """Запускает бота портфолио с подробной диагностикой"""
    print("\n" + "=" * 50)
    print("🚀 ЗАПУСК БОТА ПОРТФОЛИО")
    print("=" * 50)

    # Проверяем Python версию
    print(f"🐍 Python версия: {sys.version}")
    print(f"📁 Текущая директория: {os.getcwd()}")
    print(f"📄 Файлы в директории: {os.listdir('.')}")

    # Проверяем токен
    print(f"\n🔑 Проверка токена...")
    if not TOKEN:
        print("❌ ОШИБКА: Токен не найден!")
        print("   Убедитесь, что переменная PORTFOLIO_TOKEN установлена в Render Dashboard")
        print("   Переменные окружения:", list(os.environ.keys()))
        sys.exit(1)

    print(f"✅ Токен найден: {TOKEN[:8]}...{TOKEN[-4:]}")

    # Проверяем подключение к Telegram API
    print(f"\n🌐 Проверка подключения к Telegram API...")
    try:
        import socket
        import httpx

        # Проверяем DNS
        print("   Проверка DNS api.telegram.org...")
        socket.gethostbyname('api.telegram.org')
        print("   ✅ DNS работает")

        # Проверяем HTTP подключение
        print("   Проверка HTTP подключения...")
        client = httpx.Client(timeout=10)
        response = client.get('https://api.telegram.org')
        if response.status_code == 200:
            print("   ✅ Telegram API доступен")
        else:
            print(f"   ⚠️ Telegram API вернул код {response.status_code}")
    except Exception as e:
        print(f"❌ ОШИБКА ПОДКЛЮЧЕНИЯ: {e}")
        print("   Возможно, требуется VPN или прокси")

    # Запускаем бота
    print(f"\n🤖 Инициализация бота...")
    try:
        # Настраиваем логирование
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.DEBUG,
            handlers=[
                logging.StreamHandler(sys.stdout)
            ]
        )

        logger.info("=" * 50)
        logger.info("🚀 СОЗДАНИЕ ПРИЛОЖЕНИЯ")

        # Создаём приложение с увеличенным таймаутом
        app = Application.builder().token(TOKEN).connect_timeout(30).read_timeout(30).write_timeout(30).build()
        logger.info("✅ Приложение создано")

        # Добавляем обработчики
        logger.info("📝 Добавление обработчиков...")
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("help", help_command))
        app.add_handler(CommandHandler("projects", projects_command))
        app.add_handler(CommandHandler("skills", skills_command))
        app.add_handler(CommandHandler("contacts", contacts_command))
        app.add_handler(CallbackQueryHandler(button_handler))
        logger.info("✅ Обработчики добавлены")

        # Запускаем бота
        logger.info("🚀 Запуск polling...")
        print("\n" + "=" * 50)
        print("✅ БОТ УСПЕШНО ЗАПУЩЕН!")
        print("=" * 50 + "\n")

        app.run_polling()

    except Exception as e:
        logger.error(f"❌ КРИТИЧЕСКАЯ ОШИБКА: {e}")
        logger.error(traceback.format_exc())
        print("\n" + "=" * 50)
        print("❌ БОТ УПАЛ С ОШИБКОЙ")
        print("=" * 50)
        sys.exit(1)


if __name__ == '__main__':
    main()