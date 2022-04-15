import telebot
from misc import TOKEN


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Приветствуем вас в нашем боте 🤩')


@bot.message_handler(content_types=['text'])
def text_handler(message):
    global message_id
    text = message.text  # '2 + 5 + 5 + 7'
    sum_ = 0
    if '+' in text:
        for number in text.split('+'):
            sum_ += int(number)
    bot.reply_to(message, sum_)


# message_id = None
# @bot.message_handler(content_types=['text'])
# def text_handler(message):
#     global message_id
#     text = message.text  # '2 + 5 + 5 + 7'
#     sum_ = 0
#     if '+' in text:
#         for number in text.split('+'):
#             sum_ += int(number)
#
#     if message_id:
#         bot.edit_message_text(f'{text} = {sum_}', message.chat.id, message_id)
#     else:
#         my_message = bot.send_message(message.chat.id, f'{text} = {sum_}')
#         message_id = my_message.message_id
#
#     bot.delete_message(message.chat.id, message.message_id)


bot.polling(none_stop=True)
