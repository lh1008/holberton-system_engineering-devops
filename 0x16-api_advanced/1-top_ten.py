#!/usr/bin/python3
""" Module that queries the Reddit API """
import requests


def top_ten(subreddit):
    """ Method that prints the titles of 10 first posts """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    req = requests.get(url,
                       headers={'User-Agent': 'me'},
                       allow_redirects=False)

    if req.status_code == 404:
        return(print('None'))
    else:
        info = req.json()
        for v in range(10):
            print(info['data']['children'][v]['data']['title'])
