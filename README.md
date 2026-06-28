# API Testing Project

This project contains automated API tests for JSONPlaceholder.

The tests are written with Python, requests and pytest.

## Tested API

https://jsonplaceholder.typicode.com

## Covered scenarios

- Get a single post by ID
- Get a list of posts
- Get comments for a post with ID 1
- Create a new post
- Get nonexisting post and check 404 response
- Update an existing post
- Delete a post

## Tools used

- Python
- requests
- pytest

## How to run tests

```bash
py -m pytest test_posts.py