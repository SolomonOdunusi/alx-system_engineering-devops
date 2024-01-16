#!/usr/bin/python3
"""
A module that queries the reddit API
"""
import requests

def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Recursive function to count occurrences of keywords in the titles of 
    hot articles for a set of given subreddit.

    Args:
        subreddit (str): The subreddit to query.
        word_list (list): A list of keywords to count.
        after (str, optional): The param for pagination
        count_dict (dict, optional): A dict to store the counts of keywords.

    Returns: returns a dict or Nothing
    """
    if count_dict is None:
        count_dict = {}

    base_url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    response = requests.get(base_url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    if not posts:
        return count_dict

    for post in posts:
        title = post['data']['title'].lower()
        for word in word_list:
            if f' {word.lower()} ' in f' {title} ':
                count_dict[word.lower()] = count_dict.get(word.lower(), 0) + 1

    after = data.get('data', {}).get('after')
    if after:
        return count_words(subreddit, word_list, after, count_dict)
    else:
        return count_dict
