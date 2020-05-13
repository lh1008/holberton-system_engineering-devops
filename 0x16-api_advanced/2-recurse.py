#!/usr/bin/python3
""" Module that recursively queries the Reddit API """
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ Method that queries recursively hot titles of a given subreddit """

    if after is None:
        return []
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.\
        format(subreddit, after)

    req = requests.get(url,
                       headers={'User-Agent': 'me'},
                       allow_redirects=False)

    if req.status_code != 200:
        return(print('None'))
    else:
        info = req.json()
        for value in info.get('data').get('children'):
            hot_list.append(value.get('data').get('title'))
        after = info.get('data').get('after')
        recursively = recurse(subreddit, [], after)
        return hot_list + recursively
