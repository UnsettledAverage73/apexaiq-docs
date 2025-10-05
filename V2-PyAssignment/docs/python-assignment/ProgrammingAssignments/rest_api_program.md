# Programming Assignment: Interact with a REST API

This assignment focuses on writing a Python program to interact with an external REST API using the `requests` library. We will use a publicly available API (e.g., JSONPlaceholder) to perform common operations like fetching data, creating resources, and updating resources.

## Assignment Objective

Write a Python script that:

1.  **Fetches all posts** from `https://jsonplaceholder.typicode.com/posts`.
2.  **Fetches a single post** by its ID (e.g., post ID 5).
3.  **Creates a new post** using a `POST` request.
4.  **Updates an existing post** using a `PUT` or `PATCH` request.
5.  **Deletes a post** using a `DELETE` request.
6.  **Includes error handling** for API requests (e.g., network issues, bad responses).

## Prerequisites

*   Python installed (preferably in a virtual environment).
*   `requests` library installed: `pip install requests`

## Python Code Solution

```python
import requests
import json

<!-- -->
def fetch_all_posts(base_url):
    """Fetches all posts from the API."""
    print("\n--- Fetching all posts ---")
    try:
        response = requests.get(f"{base_url}/posts")
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        posts = response.json()
        print(f"Fetched {len(posts)} posts. Showing first 3:")
        for i, post in enumerate(posts[:3]):
            print(f"  ID: {post['id']}, Title: {post['title'][:50]}...")
        return posts
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error fetching all posts: {e}")
    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error fetching all posts: {e}")
    except requests.exceptions.Timeout:
        print("Timeout error fetching all posts.")
    except requests.exceptions.RequestException as e:
        print(f"An unexpected error occurred fetching all posts: {e}")
    return None

def fetch_single_post(base_url, post_id):
    """Fetches a single post by its ID."""
    print(f"\n--- Fetching post with ID: {post_id} ---")
    try:
        response = requests.get(f"{base_url}/posts/{post_id}")
        response.raise_for_status()
        post = response.json()
        print(f"  Fetched Post ID: {post['id']}, Title: {post['title'][:50]}...")
        print(f"  Body: {post['body'][:70]}...")
        return post
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error fetching post {post_id}: {e}")
    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error fetching post {post_id}: {e}")
    except requests.exceptions.Timeout:
        print(f"Timeout error fetching post {post_id}.")
    except requests.exceptions.RequestException as e:
        print(f"An unexpected error occurred fetching post {post_id}: {e}")
    return None

def create_new_post(base_url, title, body, user_id):
    """Creates a new post using a POST request."""
    print("\n--- Creating a new post ---")
    payload = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    try:
        response = requests.post(f"{base_url}/posts", json=payload)
        response.raise_for_status()
        new_post = response.json()
        print(f"  New Post Created! ID: {new_post['id']}, Title: {new_post['title'][:50]}...")
        return new_post
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error creating post: {e}")
    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error creating post: {e}")
    except requests.exceptions.Timeout:
        print("Timeout error creating post.")
    except requests.exceptions.RequestException as e:
        print(f"An unexpected error occurred creating post: {e}")
    return None

def update_post(base_url, post_id, new_title=None, new_body=None):
    """Updates an existing post using a PATCH request."""
    print(f"\n--- Updating post with ID: {post_id} ---")
    payload = {}
    if new_title: payload["title"] = new_title
    if new_body: payload["body"] = new_body

    if not payload:
        print("  No update data provided.")
        return None

    try:
        response = requests.patch(f"{base_url}/posts/{post_id}", json=payload)
        response.raise_for_status()
        updated_post = response.json()
        print(f"  Post ID {post_id} Updated! Title: {updated_post['title'][:50]}...")
        return updated_post
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error updating post {post_id}: {e}")
    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error updating post {post_id}: {e}")
    except requests.exceptions.Timeout:
        print(f"Timeout error updating post {post_id}.")
    except requests.exceptions.RequestException as e:
        print(f"An unexpected error occurred updating post {post_id}: {e}")
    return None

def delete_post(base_url, post_id):
    """Deletes a post by its ID."""
    print(f"\n--- Deleting post with ID: {post_id} ---")
    try:
        response = requests.delete(f"{base_url}/posts/{post_id}")
        response.raise_for_status()
        print(f"  Post ID {post_id} deleted successfully (Status: {response.status_code}).")
        return True
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error deleting post {post_id}: {e}")
    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error deleting post {post_id}: {e}")
    except requests.exceptions.Timeout:
        print(f"Timeout error deleting post {post_id}.")
    except requests.exceptions.RequestException as e:
        print(f"An unexpected error occurred deleting post {post_id}: {e}")
    return False


if __name__ == "__main__":
    API_BASE_URL = "https://jsonplaceholder.typicode.com"

    # 1. Fetch all posts
    all_posts = fetch_all_posts(API_BASE_URL)

    # 2. Fetch a single post
    single_post = fetch_single_post(API_BASE_URL, 5)

    # 3. Create a new post
    new_post_data = create_new_post(
        API_BASE_URL,
        "My Awesome New Title",
        "This is the body content of my brand new post.",
        101
    )

    # 4. Update an existing post (using PATCH for partial update)
    if new_post_data:
        updated_post_data = update_post(
            API_BASE_URL,
            new_post_data['id'],
            new_title="Updated Title for My New Post"
        )

    # 5. Delete a post
    # Note: JSONPlaceholder API simulates deletion, but doesn't actually remove resources.
    # We'll attempt to delete the post we just created.
    if new_post_data:
        delete_post(API_BASE_URL, new_post_data['id'])

    print("\n--- Demonstrating Error Handling (e.g., 404 Not Found) ---")
    fetch_single_post(API_BASE_URL, 9999) # Non-existent post ID

    print("\nAPI interaction program finished.")
```
