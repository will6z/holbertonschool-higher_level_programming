#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        titles = [post['title'] for post in posts]
        for title in titles:
            print(title)
    else:
        print("Failed to fetch posts")

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        with open('posts.csv', 'w', newline='') as file:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            
            writer.writerows({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            } for post in posts)
    else:
        print("Failed to fetch posts")

