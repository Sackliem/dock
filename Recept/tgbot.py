import telebot
from Action import CommonAction
from datetime import datetime

token = "TOKEN"
commands = ["/start", "/help", "/order"]
bot = telebot.TeleBot(token)


def command_info():
    text = 'Command List:\n'
    text += '\n'.join(commands)
    text += "\n/order need your choose in menu\n Example:\n" \
            "/oder Cheese Bread Borsh"
    return text


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/help":
        bot.reply_to(message, command_info())
    if message.text == "/start":
        menu = CommonAction.get_menu()
        str_menu = ""
        for item in menu:
            st = ""
            for key, val in item.items():
                st = st + " " + str(key.upper()) + ": " + str(val)
            str_menu += st + "\n"
        bot.reply_to(message, f"\n {str_menu}\n")
    command_text = message.text.split()
    if command_text[0] == "/order" and len(command_text) == 1:
        bot.reply_to(message, f"Your order is {CommonAction.get_ordered_items(message.from_user.username)}")
    elif command_text[0] == "/order":
        if 18 >= datetime.now().time().hour >= 7:
            CommonAction.add(message.from_user.username, command_text[1:])
        else:
            bot.send_message(chat_id=421215287, text=f'Order from {message.from_user.username} is {command_text[1:]}')


bot.polling()
