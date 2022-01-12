from telegram import Update, ParseMode, Poll, InlineKeyboardButton, InlineKeyboardMarkup, replymarkup, update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, dispatcher,CommandHandler

#Token de la API
TOKEN = '2116461521:AAE7epHA5Pv0P8B2oFax7MeEETES4z5bKqo'

#Mensaje de bienvenida
def start(update, context : CallbackContext):
    print(update.message.chat.id)
    update.message.reply_text("""
    ¡Hola Bienvenid@ al bot de Legado Financiero!
    Haz click en lo que te interesa
    - /Invertir 
    - /Educarme
    - /Help
    """)

def educarme(update: Updater, context:CallbackContext):
    update.message.reply_text(''' 
        Elige/click en una opción
    - /ContenidosGratuitos
    - /Mentoria
    ''')

def contenido_Gratuito(update:Updater, context: CallbackContext):
    update.message.reply_text("Bienvenido al contenido gratuito de Legado Financiero, te dejamos el video de bienvenida, ¡esperamos que lo disfrutes!")
    update.message.reply_text("<a href = 'https://www.youtube.com/watch?v=9W1vQWtdbVM'>Video de bienvenida</a>", parse_mode = ParseMode.HTML)

    
    button1 = InlineKeyboardButton(
        text = 'Registrate en nuestra página web',
        url = 'https://cursos.legadofinanciero.mx/home/sign_up')

    button2 = InlineKeyboardButton(
        text = 'Participa en nuestros lives de Facebook',
        url = 'https://www.facebook.com/LegadoFinancieroOficial')

    button3 = InlineKeyboardButton(
        text = 'Suscribete a nuestro canal de Youtube',
        url = 'https://www.youtube.com/c/LegadoFinanciero')

    update.message.reply_text(
        text = 'En los siguientes botones puedes registrarte a nuestra página web, seguirnos en nuestras redes sociales o conocer nuestros productos /Productos',
        reply_markup = InlineKeyboardMarkup([
           [button1], [button2],[button3]
        ])
    )

def productos(update: Updater, context: CallbackContext):
    
    button4 = InlineKeyboardButton(
        text = 'Gestión de Capital',
        url = 'https://cursos.legadofinanciero.mx/home/sign_up')

    button5 = InlineKeyboardButton(
        text = 'Pools de inversión',
        url = 'https://www.facebook.com/LegadoFinancieroOficial')

    button6 = InlineKeyboardButton(
        text = 'Fondo de libertad',
        url = 'https://www.youtube.com/c/LegadoFinanciero')

    update.message.reply_text(
        text = 'Da click en tu vehículo de inversión favorito y podrás ver un video explicandote a detalle',
        reply_markup = InlineKeyboardMarkup([
           [button4], [button5],[button6]
        ])
    )


def mentoria(update: Updater, context: CallbackContext):
    update.message.reply_text("<a href = 'https://www.youtube.com/watch?v=9W1vQWtdbVM'>Video de bienvenida</a>", parse_mode = ParseMode.HTML)
    
    button7 = InlineKeyboardButton(
        text = 'Accede a nuestros contenidos VIP',
        url = 'https://cursos.legadofinanciero.mx/home/sign_up'
    )

    button8 = InlineKeyboardButton(
        text = 'Accede a nuestro grupo VIP',
        url = 'https://t.me/+XSkg995g9cQ3ZDUx'
    )
    
    button9 = InlineKeyboardButton(
        text = 'Accede a nuestro grupo silenciado',
        url = 'https://t.me/+XSkg995g9cQ3ZDUx'
    )

    update.message.reply_text(
    text = '     Contenido VIP',
    reply_markup = InlineKeyboardMarkup([
    [button7],[button8],[button9]
    ])
)

#Esta función esta realizada para el HELP de los usuarios y envíe el contacto del usuario con el que se comunicaran.
def help(update, context: CommandHandler):
    button10 = InlineKeyboardButton(
        text = 'Grupo de soporte',
        url = 'https://t.me/+XSkg995g9cQ3ZDUx'
    )
    
    update.message.reply_text(
    text = 'Accede al grupo de soporte',
    reply_markup = InlineKeyboardMarkup([
        [button10]
    ])
)



def main():
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher
    
    # dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command,video_bienvenida))

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('Educarme', educarme))
    dispatcher.add_handler(CommandHandler('Mentoria', mentoria))
    dispatcher.add_handler(CommandHandler('ContenidosGratuitos', contenido_Gratuito))
    dispatcher.add_handler(CommandHandler('Productos', productos))
    dispatcher.add_handler(CommandHandler('Help', help))


    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()