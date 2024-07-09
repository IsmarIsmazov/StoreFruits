import telepot


def send_telegram_message(message):
    bot_token = '6747788167:AAECUbwPu7iMRWyBMvY8wDzQhIyrS0_KtD0'
    chat_id = '1378772181'

    bot = telepot.Bot(bot_token)
    bot.sendMessage(chat_id, message)