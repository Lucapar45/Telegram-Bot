from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telepot
import youtube_dl
from variables import *
import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from youtube_dl import YoutubeDL
from requests import get

def extract_name(text):
    return text.split()[1].strip()

def extract_question(text):
    question = ""
    for i in text.split():
        question = question + " " + i
    return question

def help_command(update, context):
    help_message = f"""Salve, io sono FlaviaBot, l'androide di Flavia!
Il comando /fhelp mostrerà questo messaggio!
Il comando /fciao ti saluta!
Il comando /ftettometro <name> ti dirà la tua misura di tette!
Il comando /fritardometro <name> ti dirà quanto sei ritardato/a!
Il comando /ffigometro <name> ti dirà quanto sei figa!
Il comando /faltezzometro <name> ti dirà quanto sei alto/a
Il comando /findovino <domanda> ti risponderà alla domanda
il comando /fspotilink <nome di una canzone> ti darà il link a spotify di quella canzone
il comando /fytlink <nome di una canzone> ti darà il link a youtube di quella canzone"""
    update.message.reply_text(help_message)

def ciao_command(update, context):
    ciao_message = random.choice(ciao_messages)
    update.message.reply_text(ciao_message)

def buonanotte_command(update, context):
    buonanotte_message = random.choice(buonanotte_messages)
    update.message.reply_text(buonanotte_message)

def indovino_command(update, context):
    indovino_question = extract_question(update.message.text)
    if indovino_question.strip() == "/findovino":
        indovino_text = "Almeno fammi una domanda coglione"
    else:
        indovino_question = indovino_question.replace("/findovino ", "")
        indovino_answer = random.choice(indovino_answers)
        indovino_text = f'La risposta alla domanda "{indovino_question.lower()} " è: {indovino_answer}'
    update.message.reply_text(indovino_text)

def tettometro_command(update, context):
    tettometro_number =  random.randint(1, 10)
    try:
        name = extract_name(update.message.text).title() + " ha"
        if name.lower() in kedra_possibilities:
            tettometro_number = 5
    except IndexError:
        name = "Hai"
    tettometro_text = f"{name} una {tettometro_number}° di tette! 🍒"
    update.message.reply_text(tettometro_text)

def ritardometro_command(update, context):
    ritardometro_number = str(random.randint(0, 100)) + "%"
    try:
        name = extract_name(update.message.text).title() + " è"
    except IndexError:
        name = "Sei"
    ritardometro_text = f"{name} al {ritardometro_number} ritardato/a! 😛"
    update.message.reply_text(ritardometro_text)

def figometro_command(update, context):
    figometro_number = str(random.randint(50, 100)) + "%"
    try:
        name = extract_name(update.message.text).title() + " è"
    except IndexError:
        name = "Sei"
    figometro_text = f"{name} al {figometro_number} figa! 😎"
    update.message.reply_text(figometro_text)

def altezzometro_command(update, context):
    altezzometro_number = str(random.randint(1,2)) + "." + str(random.randint(0,99)) + "m"
    try:
        name = extract_name(update.message.text).title() + " è"
    except IndexError:
        name = "Sei"
    altezzometro_text = f"{name} alto {altezzometro_number}! 📏"
    update.message.reply_text(altezzometro_text)

def spotilink_command(update, context):
    #setting Spotipy
    cid = "12bca93726cc4a7a85ae0082c02e1ef1"
    secret = "9f11fb518bba49729aeaf8dcd8be9907"
    client_credentials_manager = SpotifyClientCredentials(client_id = cid, client_secret = secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    name = extract_question(update.message.text)
    if name.strip() == "/fspotilink":
        update.message.reply_text("Almeno dimmi che devo cerca' coglione")
        print("splink fail")
    else:
        name = name.replace("/fspotilink", "")
        results = sp.search(q = "track: " + name, type = "track")
        items = results['tracks']['items']
        if len(items) == 0:
            update.message.reply_text("Nessun risultato fva")
        else:
            song = items[0]
            urls = song['external_urls']
            print(song['name'])
            update.message.reply_text(urls['spotify'])

def ytlink_command(update, context):
    ytdl = YoutubeDL()
    ytdl.add_default_info_extractors()
    name = extract_question(update.message.text)
    if name.strip() == "/fytlink":
        update.message.reply_text("Almeno dimmi che devo cercare, cretino")
    else:
        name = name.replace("/fytlink", "")
        with YoutubeDL(ytopt) as ytdl:
            try:
                get(name)
            except:
                video = ytdl.extract_info(f'ytsearch:{name}', download = False)['entries'][0]
            else:
                video = ytdl.extract_info(name, download = False)
        ytlink = video['webpage_url']
        update.message.reply_text(ytlink)

