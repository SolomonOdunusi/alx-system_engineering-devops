#!/usr/bin/python3
"""
A module that queries the reddit API
"""
import requests
import base64


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    client_id = 'SmK-O0b7WRWToYTSesQgJw'
    client_secret = 'Q9VyH5FCZAnvOfZqZQKvbxMFySY0yQ'

    headers = {
        'User-Agent': 'Test_alx_user_agent',
        'Authorization': f'Basic {base64.b64encode(
                            f"{client_id}:{client_secret}".encode()).decode()}'
    }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    else:
        subscribers = response.json().get('data', {}).get('subscribers', 0)
        return subscribers
