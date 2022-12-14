import tweepy
import chaves
import time
from datetime import date , datetime





def api():
    auth = tweepy.OAuthHandler(chaves.api_key, chaves.api_secret)
    auth.set_access_token(chaves.access_token, chaves.access_token_secret)

    return tweepy.API(auth)


def tweet(api: tweepy.API, message: str, image_path=None):
    if image_path:
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)

    print('Tweeted successfully!')


def diff_datas(data1,data2):

    d1 = datetime.strptime(data1, "%Y-%m-%d")
    d2 = datetime.strptime(data2, "%Y-%m-%d")
    return(abs(d2-d1).days)



if __name__ == '__main__':
    api = api()
    data_copa = "2026-6-8"

    while True:
        hoje = str(date.today())
        resultado= diff_datas(data_copa,hoje)
        print("{} dias entre {} e {}".format(resultado, hoje, data_copa))
        tweet(api, 'Faltam {} para a Copa do Mundo 2026.'.format(resultado))
        time.sleep(86400)
        if resultado == 0:
            tweet(api,"A Copa é hoje!!!")
            break
        else:
            continue







    
    
    