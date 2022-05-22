#!/usr/bin/python3
"""conect to Api reddit"""
import requests


def top_ten(subreddit):
    """return numbers of subscribers API"""

    try:
        req = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'
                           .format(subreddit),
                           headers={"User-Agent": "reinaldo"},
                           allow_redirects=False,).json()
        titulos = req['data']['children']
        for x in titulos:
            print(x['data']['title'])
    except Exception:
        print(None)
