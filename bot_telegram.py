from telegram import Update, ParseMode, Poll, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, dispatcher,CommandHandler

#Token de la API
TOKEN = ''
# CHAT_ID = "828006449"

#Mensaje de bienvenida
def start(update,context : CallbackContext):
    print(update.message.chat.id)
    update.message.reply_text("""
    ¡Hola Bienvenid@ a Legado Financiero, da click aquí /inicio para ver el video de bienvenida!

-Nuestras redes sociales las puedes encontrar dandole click aquí /RedesSociales

-Si necesitas hablar con alguien del equipo haz click aquí /help
    """)


def video_bienvenida(update: Updater, context: CallbackContext):
    #aquí escribimos para poder replicar el mensaje
    # print(update.message.chat.id)
    update.message.reply_text("<a href = 'https://www.youtube.com/watch?v=9W1vQWtdbVM'> Video de Bienvenida, gracias por formar parte de Legado Financiero </a>", parse_mode = ParseMode.HTML)


#Esta función esta realizada para el HELP de los usuarios y envíe el contacto del usuario con el que se comunicaran.
def help(update, contex: CommandHandler):
    contact = ''
    username = ''
    update.message.reply_contact(contact,username)

def finish(update, context):

    button1 = InlineKeyboardButton(
        text = 'Página web',
        url = 'https://cursos.legadofinanciero.mx/home/sign_up'
    )

    button2 = InlineKeyboardButton(
        text = 'Facebook',
        url= 'https://www.facebook.com/LegadoFinancieroOficial' 
    )

    button3 = InlineKeyboardButton(
        text = 'Suscribete a nuestro canal de Youtube',
        url = 'https://www.youtube.com/c/LegadoFinanciero')

    update.message.reply_text(
        text = "Siguenos en nuestras redes sociales, haz click en tu red social favorita :D",
        reply_markup = InlineKeyboardMarkup([
            [button1],
            [button2],
            [button3]
        ])
    )


def main():
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command,video_bienvenida))

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('inicio', video_bienvenida))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('RedesSociales', finish))


    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()