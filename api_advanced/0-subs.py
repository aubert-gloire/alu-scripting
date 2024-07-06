#!/usr/bin/python3

"""
A module to fetch and return the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Fetches the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers or 0 if an error occurs.
    """
    USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
    URL = f"https://api.reddit.com/r/{subreddit}/about"
    try:
        response = requests.get(URL, allow_redirects=False,
                                headers={'User-Agent': USER_AGENT}).json()
        return response.get("data", {}).get("subscribers", 0)
    except Exception:
        return 0


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
