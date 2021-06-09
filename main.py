from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from variables import *
import random
from commands import *

token = "1838699032:AAExmKGdJxh1XbvBoGUtKtWKR-nDySaQUFs"


def main():
    upd = Updater(token, use_context=True)
    disp = upd.dispatcher

    disp.add_handler(CommandHandler("fhelp", help_command))
    disp.add_handler(CommandHandler("fciao", ciao_command))
    disp.add_handler(CommandHandler("fbuonanotte", buonanotte_command))
    disp.add_handler(CommandHandler("ftettometro", tettometro_command))
    disp.add_handler(CommandHandler("fritardometro", ritardometro_command))
    disp.add_handler(CommandHandler("ffigometro", figometro_command))
    disp.add_handler(CommandHandler("faltezzometro", altezzometro_command))
    disp.add_handler(CommandHandler("findovino", indovino_command))
    disp.add_handler(CommandHandler("fspotilink", spotilink_command))
    disp.add_handler(CommandHandler("fytlink", ytlink_command))
    upd.start_polling()
    upd.idle()


if __name__ == '__main__':
    main()
    print("Flavia è on-line")