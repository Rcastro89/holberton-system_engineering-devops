#!/usr/bin/python3
"""
    Recursive function
"""
import requests


def recurse(subreddit, hot_list=[], after='', count=0):
    """
        Return that prints.
    """
    params = {
        'after': after,
        'count': count,
        'limit': 100
    }
    req = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'
                       .format(subreddit),
                       headers={"User-Agent": "reinaldo"},
                       allow_redirects=False, params=params).json()
    try:
        results = req["data"]
        after = results["after"]
        count += results["dist"]
        for post in results["children"]:
            hot_list.append(post["data"]["title"])
        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        return hot_list
    except Exception:
        return None
