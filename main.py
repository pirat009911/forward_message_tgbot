

from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes, CallbackContext
import config


# Функция для пересылки сообщений из одной группы в другую
async def forward_all(update: Update, context):
    target_chat_id = config.target_chat_id
    await context.bot.forward_message(chat_id=target_chat_id, from_chat_id=update.message.chat_id, message_id=update.message.message_id)

def main():
    #updater = Updater(config.token, update_queue=my_queue)
    application = Application.builder().token(config.token).build()

    application.add_handler(MessageHandler(filters.ALL, forward_all))
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
