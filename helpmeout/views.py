from django.shortcuts import render
from django.http import HttpResponse
import requests
import psycopg2
from requests_oauthlib import OAuth1
from urllib.parse import parse_qs
from helpmeout.models import AccessToken

#from django.template import loader

def index(request):
    return(render(request, 'helpmeout/index.html'))

def index_de(request):
    return(render(request, 'helpmeout/index.de.html'))

def callback(request):
    req = dict(request.GET)

    my_key = 'xBYpYzZ7uuiDaapMZod660fbS'
    secret = '9z1dxaTrRbsZRJUzIwjGMaC3LGQWP7IHy7D74zbpa3cFGNGchw'
    oauth_verif = req['oauth_verifier'][0]
    oauth_token = req['oauth_token'][0]

    request_url = "https://api.twitter.com/oauth/access_token"
    auth_url = "https://api.twitter.com/oauth/authorize"
    twitter = OAuth1(my_key, client_secret=secret)
    r = requests.post(request_url, auth=twitter, data={'oauth_token':oauth_token, 'oauth_verifier':oauth_verif})

    parsed = parse_qs(r.content)
    for key, value in parsed.items():
        parsed[key] = [x.decode('utf-8') for x in parsed[key]]
    oauth_token = str(parsed.get(b'oauth_token')[0])
    ot_secret = str(parsed.get(b'oauth_token_secret')[0])
    uid = str(parsed.get(b'user_id')[0])
    sname = str(parsed.get(b'screen_name')[0])

    hat = AccessToken(oauth_token=oauth_token, ot_secret=ot_secret, user_id=uid, screen_name=sname)
    hat.save()

    return(render(request, 'helpmeout/callback.html'))
