from django import template
import os
import requests
from requests_oauthlib import OAuth1
from urllib.parse import parse_qs

register = template.Library()

@register.simple_tag
def signinurl():
    """ Step 1 of the authentication workflow, obtain a temporary
    resource owner key and use it to redirect the user. The user
    will authorize the client (our flask app) to access its resources
    and perform actions in its name (aka get feed and post updates)."""

    my_key = 'xBYpYzZ7uuiDaapMZod660fbS'
    secret = '9z1dxaTrRbsZRJUzIwjGMaC3LGQWP7IHy7D74zbpa3cFGNGchw'

    request_url = "https://api.twitter.com/oauth/request_token"
    auth_url = "https://api.twitter.com/oauth/authorize"
    cb_url = 'http://malteheckelen.com/helpmeout/callback'

    # In this step you will need to supply your twitter provided key and secret
    twitter = OAuth1(my_key, client_secret=secret)

    # We will be using the default method of supplying parameters, which is
    # in the authorization header.
    r = requests.post(request_url, auth=twitter, data={'callback_url':cb_url})

    # Extract the temporary resource owner key from the response
    parsed = parse_qs(r.content)
    for key, value in parsed.items():
        parsed[key] = [x.decode('utf-8') for x in parsed[key]]
    token = parsed.get(b"oauth_token")[0]

    # Create the redirection url and send the user to twitter
    # This is the start of Step 2
    auth = u"{url}?oauth_token={token}".format(url=auth_url, token=token)
    return(auth)
