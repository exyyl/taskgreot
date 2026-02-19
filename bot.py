import os
import logging
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Токен из переменных окружения
TOKEN = os.environ.get('BOT_TOKEN')

async def start(update: Update, context):
    await update.message.reply_text('Бот работает!')

async def send_message(update: Update, context):
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text='Сообщение отправлено!')

def main():
    if not TOKEN:
        print("ОШИБКА: BOT_TOKEN не найден в переменных окружения!")
        return
    
    # Создание приложения
    app = Application.builder().token(TOKEN).build()
    
    # Обработчики
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("send", send_message))
    
    print("Бот запущен...")
    app.run_polling()

if __name__ == '__main__':
    main()
