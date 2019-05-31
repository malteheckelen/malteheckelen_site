import os
import requests
from requests_oauthlib import OAuth1
from urllib.parse import parse_qs
#from flask import Flask, request, redirect, session

my_key = 'xBYpYzZ7uuiDaapMZod660fbS'
secret = '9z1dxaTrRbsZRJUzIwjGMaC3LGQWP7IHy7D74zbpa3cFGNGchw'
ACCESS_TOKEN = '596534051-Ek823Ey14jXe9ZL4Sd1S0Y0BNTfzYl2U5gY6MeAU'
ACCESS_TOKEN_SECRET = '25KDBi2xzKy0T8eyC3huffldO910iXjPJ7ficyDZ0QtnO'

request_url = "https://api.twitter.com/oauth/request_token"
auth_url = "https://api.twitter.com/oauth/authorize"
access_url = "https://api.twitter.com/oauth/access_token"
update_url = "http://api.twitter.com/1/statuses/update.json"


def demo():
    """ Step 1 of the authentication workflow, obtain a temporary
    resource owner key and use it to redirect the user. The user
    will authorize the client (our flask app) to access its resources
    and perform actions in its name (aka get feed and post updates)."""

    # In this step you will need to supply your twitter provided key and secret
    twitter = OAuth1(my_key, client_secret=secret)

    # We will be using the default method of supplying parameters, which is
    # in the authorization header.
    r = requests.post(request_url, auth=twitter)

    # Extract the temporary resource owner key from the response
    parsed = parse_qs(r.content)
    for key, value in parsed.items():
        parsed[key] = [x.decode('utf-8') for x in parsed[key]]
    token = parsed.get(b"oauth_token")[0]

    # Create the redirection url and send the user to twitter
    # This is the start of Step 2
    auth = u"{url}?oauth_token={token}".format(url=auth_url, token=token)
    print(auth)

demo()
