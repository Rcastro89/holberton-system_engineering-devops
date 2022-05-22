#!/usr/bin/python3
"""conect to Api reddit"""
import requests


def number_of_subscribers(subreddit):
    """return numbers of subscribers API"""

    try:
        req = requests.get('https://www.reddit.com/r/{}/about.json'
                           .format(subreddit),
                           headers={"User-Agent": "reinaldo"},
                           allow_redirects=False,).json()
        return req['data']['subscribers']
    except Exception:
        return 0
