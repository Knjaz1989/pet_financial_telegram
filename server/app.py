from telebot import types, TeleBot

from settings import config


API_TOKEN = config.BOT_TOKEN

bot = TeleBot(API_TOKEN)


# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=False
    )
    markup.row('Добавить покупку')
    bot.send_message(
        message.from_user.id,
        'Добро пожаловать',
        reply_markup=markup,
    )


#     bot.reply_to(message, """\
# Hi there, I am EchoBot.
# I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
# """)

# @bot.message_handler(commands=['add_purchase'])
# def button_message(message):
#
#     item1 = types.KeyboardButton("Добавить покупку")
#     markup.add(item1)


# # Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, message.text)


bot.infinity_polling()
