#!/usr/bin/env python3
import requests
import json

print("GitHub User Info Fetcher")
print("-" * 30)

username = input("Enter a GitHub username: ")

# Fetch user data from GitHub API
response = requests.get(f"https://api.github.com/users/{username}")

if response.status_code == 200:
    user = response.json()
    print(f"\nName: {user.get('name', 'Not provided')}")
    print(f"Bio: {user.get('bio', 'Not provided')}")
    print(f"Public repos: {user['public_repos']}")
    print(f"Followers: {user['followers']}")
else:
    print(f"Error: User '{username}' not found!")
