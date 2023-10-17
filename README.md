# wildapricot_api_auth.py 

The access token is obtained from an API. The code makes an HTTP POST request to Wild Apricot's OAuth service at the token_url (https://oauth.wildapricot.org/auth/token). The OAuth service processes this request and, if the API key is valid, it responds with an access token.


This access token is then used to authenticate your requests when interacting with Wild Apricot's Admin API and Member API. The token serves as a credential to prove that your application is authorized to access the protected resources on those APIs.


# check-api-credentials.py

check api credentials.