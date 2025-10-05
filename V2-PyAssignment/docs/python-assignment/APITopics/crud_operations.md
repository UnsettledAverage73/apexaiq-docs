# CRUD Operations

CRUD is an acronym that stands for Create, Read, Update, and Delete. These four basic functions are the persistent storage actions that are essential for any application that interacts with a database or a persistent data store. In the context of APIs, CRUD operations correspond directly to HTTP methods for interacting with resources.

## Understanding CRUD

### 1. Create (C)

*   **Purpose**: To add new data or resources to the system.
*   **API/HTTP Method**: Typically handled by the `POST` HTTP method.
    *   A `POST` request sends data to the server to create a new resource.
*   **Database Operation**: `INSERT` (e.g., in SQL databases).
*   **Example (API Request)**:
    ```
    POST /users
    Content-Type: application/json

    {
      "name": "Jane Doe",
      "email": "jane.doe@example.com"
    }
    ```
*   **Typical API Response**: `201 Created` with the newly created resource and its URI.

### 2. Read (R)

*   **Purpose**: To retrieve existing data or resources from the system.
*   **API/HTTP Method**: Typically handled by the `GET` HTTP method.
    *   A `GET` request retrieves data without modifying it.
*   **Database Operation**: `SELECT` (e.g., in SQL databases).
*   **Examples (API Requests)**:
    *   **Get all resources**: `GET /users`
    *   **Get a single resource by ID**: `GET /users/123`
*   **Typical API Response**: `200 OK` with the requested resource(s) in the response body.

### 3. Update (U)

*   **Purpose**: To modify existing data or resources in the system.
*   **API/HTTP Methods**: Can be handled by `PUT` or `PATCH` HTTP methods.
    *   **PUT**: Used to replace an entire resource. The client sends the complete, updated representation of the resource.
    *   **PATCH**: Used to apply partial modifications to a resource. The client sends only the data fields that need to be updated.
*   **Database Operation**: `UPDATE` (e.g., in SQL databases).
*   **Example (API Request - PUT)**:
    ```
    PUT /users/123
    Content-Type: application/json

    {
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
    ```
*   **Example (API Request - PATCH)**:
    ```
    PATCH /users/123
    Content-Type: application/json

    {
      "email": "new.email@example.com"
    }
    ```
*   **Typical API Response**: `200 OK` (with or without updated resource) or `204 No Content`.

### 4. Delete (D)

*   **Purpose**: To remove data or resources from the system.
*   **API/HTTP Method**: Typically handled by the `DELETE` HTTP method.
    *   A `DELETE` request asks the server to remove the specified resource.
*   **Database Operation**: `DELETE` (e.g., in SQL databases).
*   **Example (API Request)**:
    ```
    DELETE /users/123
    ```
*   **Typical API Response**: `200 OK` (if a response body indicates success), `204 No Content` (for successful deletion with no body), or `202 Accepted` (if deletion is async).

## CRUD in RESTful APIs

In the context of RESTful APIs, the mapping between CRUD operations and HTTP methods is a fundamental principle:

| CRUD Operation | HTTP Method | Description                                            |
| :------------- | :---------- | :----------------------------------------------------- |
| Create         | `POST`      | Creates a new resource.                                |
| Read           | `GET`       | Retrieves a resource or a collection of resources.     |
| Update         | `PUT`/`PATCH`| Replaces (PUT) or partially updates (PATCH) a resource. |
| Delete         | `DELETE`    | Removes a resource.                                    |

## Importance of CRUD

*   **Standardization**: Provides a clear and consistent way to design and interact with data-driven applications and APIs.
*   **Predictability**: Clients can anticipate how to perform common operations on resources.
*   **Simplicity**: Simplifies the API design by mapping common data operations to well-understood HTTP methods.
*   **Maintainability**: Easier to maintain systems when core data operations follow a predictable pattern.

Virtually all data-centric applications and APIs rely on the CRUD paradigm to manage their persistent data.
