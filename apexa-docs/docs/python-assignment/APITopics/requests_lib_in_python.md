# Requests Library in Python

The `requests` library is an elegant and simple HTTP library for Python, designed to be user-friendly. It allows you to send HTTP/1.1 requests (GET, POST, PUT, DELETE, etc.) with ease, handling complexities like connection pooling, SSL verification, content encoding, and much more, which are often cumbersome with Python's built-in `urllib` module. It's the de facto standard for making HTTP requests in Python.

## Installation

Before you can use the `requests` library, you need to install it. It's highly recommended to do this within a [virtual environment](V2-PyAssignment/virtual_environments_pip.md).

```bash
pip install requests
```

## Basic Usage

### 1. `GET` Request

Used to retrieve data from a specified resource.

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

print(f"Status Code: {response.status_code}")
print(f"Response Headers: {response.headers['Content-Type']}")
print(f"Response Body (JSON): {response.json()}")

# Access specific data from JSON response
print(f"Post Title: {response.json().get('title')}")
```

### 2. `POST` Request

Used to send data to a server to create a new resource.

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

response = requests.post(url, json=payload)

print(f"Status Code: {response.status_code}") # Should be 201 Created
print(f"Response Body (JSON): {response.json()}")
```

### 3. `PUT` Request

Used to send data to a server to update an existing resource. It typically replaces the entire resource.

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
payload = {
    "id": 1,
    "title": "new foo title",
    "body": "new bar body",
    "userId": 1
}

response = requests.put(url, json=payload)

print(f"Status Code: {response.status_code}") # Should be 200 OK
print(f"Response Body (JSON): {response.json()}")
```

### 4. `PATCH` Request

Used to send data to a server to apply partial modifications to an existing resource.

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
payload = {
    "title": "just a new title"
}

response = requests.patch(url, json=payload)

print(f"Status Code: {response.status_code}") # Should be 200 OK
print(f"Response Body (JSON): {response.json()}")
```

### 5. `DELETE` Request

Used to remove a specified resource from the server.

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.delete(url)

print(f"Status Code: {response.status_code}") # Should be 200 OK
print(f"Response Body (JSON): {response.json()}") # Often empty or a confirmation
```

## Important Features of `requests`

### 1. Query Parameters

Pass data in the URL as query parameters using the `params` argument (a dictionary).

```python
import requests

url = "https://jsonplaceholder.typicode.com/comments"
params = {"postId": 1}

response = requests.get(url, params=params)
print(f"Comments for postId 1: {response.json()}")
```

### 2. Custom Headers

Send custom HTTP headers using the `headers` argument (a dictionary).

```python
import requests

url = "https://api.github.com/events"
headers = {
    "User-Agent": "MyPythonApp/1.0",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)
print(f"GitHub Events Status: {response.status_code}")
```

### 3. Authentication

`requests` supports various authentication methods, including Basic Authentication.

```python
import requests
from requests.auth import HTTPBasicAuth

url = "https://api.example.com/user"
response = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
print(f"Auth Status: {response.status_code}")
```

### 4. Timeouts

Specify a `timeout` value to prevent requests from hanging indefinitely.

```python
import requests

url = "https://httpbin.org/delay/5" # An endpoint that delays response by 5 seconds
try:
    response = requests.get(url, timeout=3) # Set timeout to 3 seconds
    print(response.status_code)
except requests.exceptions.Timeout:
    print("The request timed out.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
```

### 5. Sessions

For making multiple requests to the same host, a `Session` object can improve performance by persisting certain parameters across requests (like headers, cookies, and authentication) and reusing the underlying TCP connection.

```python
import requests

with requests.Session() as session:
    session.headers.update({'X-Custom-Header': 'Hello'})
    session.auth = ('user', 'pass')

    # All requests made with this session will have the custom header and auth
    response1 = session.get("https://httpbin.org/headers")
    print(response1.json()["headers"])

    response2 = session.get("https://httpbin.org/basic-auth/user/pass")
    print(f"Auth successful: {response2.status_code == 200}")
```

### 6. Error Handling

`requests` provides custom exceptions for network problems, invalid HTTP responses, and timeouts.

```python
import requests

try:
    response = requests.get("https://bad-url-example.com")
    response.raise_for_status() # Raises an HTTPError for bad responses (4xx or 5xx)
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.exceptions.ConnectionError as e:
    print(f"Connection Error: {e}")
except requests.exceptions.RequestException as e:
    print(f"An unexpected error occurred: {e}")
```

The `requests` library is a powerful and flexible tool for interacting with web services in Python, making network programming significantly simpler.
