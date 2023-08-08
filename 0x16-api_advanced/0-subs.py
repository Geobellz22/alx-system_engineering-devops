#!/sr/bin/python3
""" Script that queries API"""

import requests


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'MyBot/1.0'}  # Replace with your User-Agent

    headers = {'User-Agent': 'MyBot/1.0'}  # Replace with your User-Agent

    response = requests.get(base_url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        subsribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
