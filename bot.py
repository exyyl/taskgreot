import asyncio
from telegram import Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Токен бота (получи у @BotFather)
TOKEN = '8236195754:AAE9bdY8uD9roVwEFBxdxz8eqs08JRyRpPo'

# Команда /start
async def start(update, context):
    await update.message.reply_text('Привет! Я простой бот. Напиши мне что-нибудь!')

# Команда /help
async def help_command(update, context):
    await update.message.reply_text('Доступные команды:\n/start - Начать\n/help - Помощь\n/send - Отправить тестовое сообщение')

# Команда /send - отправляет сообщение
async def send_message(update, context):
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text='Это тестовое сообщение!')

# Обработка обычных сообщений
async def echo(update, context):
    user_message = update.message.text
    await update.message.reply_text(f'Ты написал: {user_message}')

# Функция для отправки сообщения в любой чат
async def send_message_to_chat(chat_id, text):
    """Отправляет сообщение в указанный чат"""
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=chat_id, text=text)

def main():
    # Создаем приложение
    app = Application.builder().token(TOKEN).build()
    
    # Добавляем обработчики команд
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("send", send_message))
    
    # Обработчик текстовых сообщений
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    # Запускаем бота
    print("Бот запущен...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
