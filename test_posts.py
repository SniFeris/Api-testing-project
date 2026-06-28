import requests
BASE_URL = "https://jsonplaceholder.typicode.com"

#Test that API returns post with ID 1
def test_get_single_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
    assert "userId" in data

#Test that API returns a list of posts
def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data, list)
    assert "id" in data[0]
    assert "title" in data[0]
    assert "body" in data[0]    
    assert "userId" in data[0]

#Test that API returns comments for a post with ID 1
def test_get_comments_for_post():
    response = requests.get(f"{BASE_URL}/posts/1/comments")
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0
    assert data[0]["postId"] == 1
    assert "id" in data[0]
    assert "name" in data[0]
    assert "email" in data[0]
    assert "body" in data[0]

#Test that API creates a new post
def test_create_post():
    payload = {
        "title": "Test title",
        "body": "Test body",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    data = response.json()
    assert response.status_code == 201
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data
    
#Test that API returns  404 for nonexisting post
def test_get_non_existing_post():
    response = requests.get(f"{BASE_URL}/posts/9999")
    assert response.status_code == 404

#Test that API updates existing post
def test_update_post():
    payload = {
        "title": "Bauskas alus",
        "body": "alus",
        "userId" : 1
    }
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)
    data = response.json()
    assert response.status_code == 200
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert data["id"] == 1

#Test that API deletes a post
def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200