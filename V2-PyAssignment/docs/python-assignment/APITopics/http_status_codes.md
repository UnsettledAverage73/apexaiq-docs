# HTTP Status Codes

HTTP (Hypertext Transfer Protocol) status codes are three-digit numbers returned by a server in response to an HTTP request made by a client. These codes indicate whether a particular HTTP request has been successfully completed, providing critical information about the request's outcome. Understanding them is fundamental for working with APIs and debugging web applications.

## Structure of HTTP Status Codes

HTTP status codes are grouped into five classes, each indicating a different type of response:

*   **1xx (Informational)**: The request was received, continuing process.
*   **2xx (Success)**: The request was successfully received, understood, and accepted.
*   **3xx (Redirection)**: Further action needs to be taken by the user agent to fulfill the request.
*   **4xx (Client Error)**: The request contains bad syntax or cannot be fulfilled.
*   **5xx (Server Error)**: The server failed to fulfill an apparently valid request.

## Common HTTP Status Codes

### 1xx: Informational Responses

*   **`100 Continue`**: The server has received the request headers, and the client should proceed to send the request body.
*   **`101 Switching Protocols`**: The requester has asked the server to switch protocols and the server has agreed to do so.

### 2xx: Success Responses

*   **`200 OK`**: The request has succeeded. This is the most common status code for successful GET requests.
*   **`201 Created`**: The request has succeeded and a new resource has been created as a result. This is typically sent after a `POST` request or some `PUT` requests.
*   **`202 Accepted`**: The request has been accepted for processing, but the processing has not been completed. It is non-committal, meaning there is no guarantee that the action will eventually be taken.
*   **`204 No Content`**: The server successfully processed the request and is not returning any content. Typically used for `PUT` or `DELETE` requests where no response body is needed.

### 3xx: Redirection Messages

*   **`301 Moved Permanently`**: The resource has been permanently moved to a new URL. The client should update its links.
*   **`302 Found` (or `Moved Temporarily`)**: The resource is temporarily located at a different URL. The client should not change its links.
*   **`304 Not Modified`**: Indicates that the resource has not been modified since the version specified by the request headers `If-Modified-Since` or `If-None-Match`. The client can use a cached copy.

### 4xx: Client Error Responses

*   **`400 Bad Request`**: The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing).
*   **`401 Unauthorized`**: The client must authenticate itself to get the requested response. (Note: It means "unauthenticated", not "unauthorized").
*   **`403 Forbidden`**: The client does not have access rights to the content, so the server is refusing to give a proper response. Unlike `401`, the client's identity is known to the server.
*   **`404 Not Found`**: The server cannot find the requested resource. This is perhaps the most famous `4xx` error.
*   **`405 Method Not Allowed`**: The request method is known by the server but has been disabled and cannot be used for the requested resource.
*   **`409 Conflict`**: Indicates a request conflict with current state of the target resource. Often used for concurrent updates, where the client is trying to update a resource that has been modified by another client.
*   **`410 Gone`**: The requested content has been permanently deleted from the server, with no forwarding address.
*   **`429 Too Many Requests`**: The user has sent too many requests in a given amount of time ("rate limiting").

### 5xx: Server Error Responses

*   **`500 Internal Server Error`**: The server has encountered a situation it doesn't know how to handle. A generic error message, often indicating an unexpected condition on the server.
*   **`501 Not Implemented`**: The server does not support the functionality required to fulfill the request. This means the method is not implemented by the server.
*   **`502 Bad Gateway`**: The server, while acting as a gateway or proxy, received an invalid response from an upstream server.
*   **`503 Service Unavailable`**: The server is not ready to handle the request. Common causes are a server that is down for maintenance or is overloaded.
*   **`504 Gateway Timeout`**: The server, while acting as a gateway or proxy, did not receive a timely response from an upstream server or some other auxiliary server it needed to access to complete the request.

## Importance in API Development

Properly using and handling HTTP status codes is crucial for several reasons:

*   **Clear Communication**: Provides immediate feedback to the client about the outcome of their request.
*   **Error Handling**: Allows client applications to implement robust error handling logic based on the type of error.
*   **Debugging**: Helps developers quickly identify and diagnose issues in API interactions.
*   **SEO/Caching**: `3xx` and `4xx` codes are important for search engine optimization and proper caching behavior.

When designing or consuming APIs, always pay close attention to the HTTP status codes to ensure predictable and reliable communication.