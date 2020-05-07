# 0x16. API advanced

## Learning Objectives


- How to read API documentation to find the endpoints you’re looking for
- How to use an API with pagination
- How to parse JSON results from an API
- How to make a recursive API call
- How to sort a dictionary by value

[Reddi API](https://www.reddit.com/dev/api/)

### Tasks

_**0. How many subs?**_
Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

_**1. Top Ten**_
Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

_**2. Recurse it!**_
Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.
