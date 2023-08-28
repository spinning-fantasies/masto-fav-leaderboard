import os
import json
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
instance_url = os.getenv('MASTODON_INSTANCE_URL')
access_token = os.getenv('MASTODON_ACCESS_TOKEN')
# print(instance_url, access_token)

# Make a GET request to the API endpoint for your statuses
api_url = f"{instance_url}/api/v1/accounts/verify_credentials"
headers = {"Authorization": f"Bearer {access_token}"}
# print(headers)

response = requests.get(api_url, headers=headers)
# print(response)

if response.status_code == 200:
    data = response.json()
    # print(data)

    account_id = data.get("id")
    # print(account_id)
    
    # Now get the full list of statuses for the authenticated account
    statuses_url = f"{instance_url}/api/v1/accounts/{account_id}/statuses"
    # print(statuses_url)
    
    response = requests.get(statuses_url, headers=headers)
    # print(response)
    
    if response.status_code == 200:
        statuses = response.json()
        # print(statuses)

        # for status in statuses:
            # print(status.get("content"))
    else:
        print("Failed to retrieve statuses.")

    data = []
    
    for x in range(0, len(statuses)-1):
        print(statuses[x]['created_at'].format().split("T")[0], statuses[x]['url'])

else:
    print("Failed to authenticate.")