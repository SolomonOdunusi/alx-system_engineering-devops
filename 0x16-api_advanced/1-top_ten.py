#!/usr/bin/python3
"""
A module that queries the reddit API
"""
import sys
import requests

def top_ten(subreddit):
    """Returns the top ten posts for a given subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {'limit': 3}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print(None)
    else:
        posts = response.json().get('data', {}).get('children', None)
        if posts is None:
            print(None)
        else:
            for post in posts:
                print(post.get('data', {}).get('author', None))
