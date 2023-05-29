import telebot

TOKEN_BOT = ''## Тут токен бота
CHAT_ID = '' ## Идентифика́тор пользователя в Telegram
bot = telebot.TeleBot(TOKEN_BOT)

bot.send_message(CHAT_ID,'Task3_1 Success!!!!')
