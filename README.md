# teslatoken 

This program provides a skeleton to obtain Tesla user API tokens with your application's OAuth client ID.

It is by no means feature complete, is missing some protections for public use (such as using a state to prevent CSRF).

This program was used for an internal proof-of-concept and offers no warranties - you accept you use this at your own risk.

The skeleton listens on the following endpoints:

- /forward - creates the redirect URL to forward the user to the Tesla account site, where they can authorise the app
- /callback - redirect endpoint after the user successfully authenticates and authorises the app. It will obtain access and request tokens for the user and output them to the browser for use in your application

You will have to set the `redirect_url` variable to your own domain (same as that registered in the Tesla developer portal)
The North America/Pacific hostname is used for `tesla_audience`. Change it to the server that matches your region (refer Tesla Developer documentation)

It is recommended to run this program behind a reverse proxy/ingress controller

## requirements

- Tesla developer account (https://developer.tesla.com)
- Third-party application active in your Tesla developer account
- Docker 


## Installation
To use this as a docker container, you will have to build it with the included Dockerfile

## Environment variables

| Variable | Description | Default |
| :---- | --- | --- |
| TESLA_CLIENT_ID | OAuth client ID from Tesla Developer portal | None |
| TESLA_CLIENT_SECRET | OAuth client secret from Tesla Developer portal | None |


## run it

to run it native you have to first install the requirements with pip or your package manager

native:

    pip3 install -r requirements.txt
    sudo uvicorn app.main:app --reload --host 0.0.0.0 --port 80

   
## validate

if it's running properly you should get redirected to Tesla when browsing to

http://IP_ADDRESS/forward
