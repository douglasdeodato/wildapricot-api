import requests
import base64
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the API key from the environment variables
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY is not set in the .env file")

# Endpoint URL for token request
token_url = "https://oauth.wildapricot.org/auth/token"

# Base64 encode the API key
api_key_b64 = base64.b64encode(f"APIKEY:{API_KEY}".encode()).decode()

# Define the headers for the request
headers = {
    "Host": "oauth.wildapricot.org",
    "Authorization": f"Basic {api_key_b64}",
    "Content-Type": "application/x-www-form-urlencoded"
}

# Define the payload for the request
data = {
    "grant_type": "client_credentials",
    "scope": "auto"
}

# Make the POST request to obtain the token
response = requests.post(token_url, headers=headers, data=data)

if response.status_code == 200:
    token_data = response.json()
    access_token = token_data["access_token"]
    print("Access Token:", access_token)
    refresh_token = token_data.get("refresh_token")
    if refresh_token:
        print("Refresh Token:", refresh_token)
else:
    print("Failed to obtain the access token. Status code:", response.status_code)
    print("Response Content:", response.text)
