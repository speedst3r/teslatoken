from fastapi import FastAPI
from requests_oauthlib import OAuth2Session
from starlette.responses import RedirectResponse
import requests
import os
import sys

app = FastAPI()

TESLA_CLIENT_ID = os.getenv('TESLA_CLIENT_ID', None)
TESLA_CLIENT_SECRET = os.getenv('TESLA_CLIENT_SECRET', None)

if TESLA_CLIENT_ID is None or TESLA_CLIENT_SECRET is None:
    print("Please ensure Tesla client id and secret are set in the TESLA_CLIENT_ID and TESLA_CLIENT_SECRET variables")
    sys.exit(1)

authorization_base_url = "https://auth.tesla.com/oauth2/v3/authorize"
token_url = "https://auth.tesla.com/oauth2/v3/token"
scope = ['openid', 'offline_access', 'user_data', 'vehicle_device_data', 'vehicle_cmds', 'vehicle_charging_cmds',
          'energy_device_data', 'energy_cmds']
redirect_uri = "https://<your app domain>/callback"
tesla_audience = "https://fleet-api.prd.na.vn.cloud.tesla.com"

@app.get("/forward")
def forward():

    oauth = OAuth2Session(TESLA_CLIENT_ID, redirect_uri=redirect_uri, scope=scope)

    authorization_url, state = oauth.authorization_url(authorization_base_url)

    response = RedirectResponse(url=authorization_url)

    return response

@app.get("/callback")
def callback(code: str):

    oauth = OAuth2Session(TESLA_CLIENT_ID, redirect_uri=redirect_uri)

    token = oauth.fetch_token(token_url, code=code, client_secret=TESLA_CLIENT_SECRET,
                              include_client_id=True, audience=tesla_audience)

    return token
