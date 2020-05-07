#!/usr/bin/python3
""" Module that queries the Reddit API """
import requests
from collections import OrderedDict

def number_of_subscribers(subreddit):
    """ Method that returns the number of subscribers """
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)

    req = requests.get(url,
                       headers = {'User-Agent': 'me'},
                       allow_redirects=False)
    if subreddit is False:
        return(0)
    info = req.json()
    return(info['data']['children'][0]['data']['subreddit_subscribers'])

if __name__ == '__main__':
    number_of_subscribers()
