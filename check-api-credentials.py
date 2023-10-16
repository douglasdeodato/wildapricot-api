import requests
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get credentials from environment variables
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
api_key = os.getenv("API_KEY")

if client_id is None or client_secret is None or api_key is None:
    print("Missing one or more of the required credentials.")
else:
    # Set your API endpoint URL
    url = "https://api.wildapricot.org"

    # Set the headers with credentials
    headers = {
        "client_id": client_id,
        "client_secret": client_secret,
        "apikey": api_key
    }

    # Make the GET request
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the response content
        print(response.text)
    else:
        # Print an error message if the request was not successful
        print(f"Request failed with status code: {response.status_code}")
