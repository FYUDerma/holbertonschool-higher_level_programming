#!/usr/bin/python3
import requests
import csv


url = "https://jsonplaceholder.typicode.com/posts"
def fetch_and_print_posts():
    """Fetches posts from the JSONPlaceHolder."""
    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(f"{post['title']}")


def fetch_and_save_posts():
    """Fetchs post from the JSONPlaceHolder."""
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        posts = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in data]
        with open("posts.csv", "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts)
