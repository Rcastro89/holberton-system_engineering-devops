#!/usr/bin/python3
"""
    Prints count of all searched for words in hot post titles.
"""


import requests


def count_words(subreddit, word_list, hot_list=[], aft=None):
    """
        Counts words in all hot post titles
    """

    dic = {}
    for x in word_list:
        dic[x] = 0

    head = {
        'User-Agent': 'reinaldo'
    }

    response = requests.get('https://www.reddit.com/r/{}/hot.json?after={}'
                            .format(subreddit, aft), headers=head)

    if (not response.status_code == 200 or
       not response.json().get('data').get('children')):
        return None

    aft = response.json().get('data').get('after')
    hot_list += [x.get('data').get('title') for x in
                 [y for y in response.json().get('data').get('children')]]
    if aft:
        count_words(subreddit, word_list, hot_list, aft)
    else:
        for title in hot_list:
            for key in dic:
                dic[key] += title.lower().split(' ').count(key.lower())
        sort = [(v, k) for k, v in dic.items()]
        sort.sort(reverse=True)
        for v, k in sort:
            if v:
                print('{}: {}'.format(k, v))
