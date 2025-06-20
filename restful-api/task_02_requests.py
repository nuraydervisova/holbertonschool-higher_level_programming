# task_02_requests.py

import requests
import csv

API_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    """Fetches all posts from JSONPlaceholder and prints the status code and titles."""
    response = requests.get(API_URL)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))

def fetch_and_save_posts():
    """Fetches all posts from JSONPlaceholder and saves id, title, body to posts.csv."""
    response = requests.get(API_URL)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        # Structure the data
        data_to_save = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]
        
        # Write to CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for row in data_to_save:
                writer.writerow(row)
        print("Saved posts.csv")

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
