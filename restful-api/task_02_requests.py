#!/usr/bin/python3
import requests


def fetch_and_print_posts():
    """Fetches posts from the JSONPlaceHolder."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(f"{post['title']}")

def fetch_and_save_posts():
    """Fetchs post from the JSONPlaceHolder."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        data = response.json()
        with open("posts.csv", "w", newline='') as file:
            file.write(str(data))
