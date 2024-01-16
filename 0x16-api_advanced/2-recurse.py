#!/usr/bin/python3
"""
A module that queries the reddit API
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function to get all hot articles for a given subreddit.

    Args:
        subreddit (str): The subreddit to query
        hot_list (list): A list to store the titles of hot articles
        after (str): The param for pagination

    Returns: returns a list or None
    """
    base_url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    response = requests.get(base_url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    if not posts:
        return hot_list

    for post in posts:
        hot_list.append(post['data']['title'])

    after = data.get('data', {}).get('after')
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
