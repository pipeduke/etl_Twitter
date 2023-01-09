# Importar librerias
import tweepy
import pandas as pd 
import json
from datetime import datetime

# Definir función que será ejecutada por el DAG
def run_tw_etl():

    # Claves de acceso a la API de Twitter

    access_key = "7vhh55asZGNKZCDhldtCZ9tYB" 
    access_secret = "XFhYvhrEX2JJTU934r1tHuaXoSwlWR7F6pxH9cXramIVEZd4dX" 
    consumer_key = "130601217-Yf3jub3y3g37KV0AhiKO57eDUyV1K1ILxeRUSf7O"
    consumer_secret = "BO25ZmRnG7t0rRsrGuOTCEeM2oGUSEaEn7U5B6ysvAozQ"

    # Autenticación Twitter
    auth = tweepy.OAuthHandler(access_key, access_secret)   
    auth.set_access_token(consumer_key, consumer_secret) 

    # Creación API object 
    api = tweepy.API(auth)

    # Array que va a contener los datos
    tw_list = []
    # En este caso consultaremos los tweets más populares de un termino que puede ser relevante en la industria: "energíaRenovable" 
    for status in tweepy.Cursor(api.search_tweets, q = 'energiarenovable', tweet_mode='popular').items(100):
    # Agregamos fecha(formateada), likes, retweets, idioma y nombre del usuario al array
        tw_list.append([datetime.strftime(status.created_at,'%d-%m-%Y'), status.favorite_count, status.retweet_count, status.lang, status.user.screen_name])

    # Crear DataFrame con las columnas definidas
    tw_list = pd.DataFrame(tw_list, columns=['Date', 'Likes', 'Retweets','Lang', 'User'])

    # Exportar a CSV
    tw_list.to_csv("dataTweets.csv", index=False, sep ='|', encoding="utf-8")