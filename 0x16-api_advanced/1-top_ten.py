#!/usr/bin/python3
"""
A module that queries the reddit API
"""
import sys
import requests


def top_ten(subreddit):
    """Returns the top ten posts for a given subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    client_id = 'SmK-O0b7WRWToYTSesQgJw'
    client_secret = 'Q9VyH5FCZAnvOfZqZQKvbxMFySY0yQ'

    headers = {
        'User-Agent': 'Test_alx_user_agent',
        'Authorization': f'Basic {base64.b64encode(
                            f"{client_id}:{client_secret}".encode()).decode()}'
    }
    params = {'limit': 3}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        print(None)
    else:
        posts = response.json().get('data', {}).get('children', None)
        if posts is None:
            print(None)
        else:
            for post in posts:
                print(post.get('data', {}).get('author', None))
