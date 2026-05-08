# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

In this assignment, you will build a simple REST API using FastAPI and Python. You will learn how to create endpoints, validate request data, and return structured JSON responses.

## 📝 Tasks

### 🛠️	Create a FastAPI App with Core Endpoints

#### Description
Set up a FastAPI application and implement basic CRUD-style endpoints for managing a list of books.

#### Requirements
Completed program should:

- Create a FastAPI app instance in `starter-code.py`.
- Implement `GET /books` to return all books.
- Implement `GET /books/{book_id}` to return one book by id.
- Implement `POST /books` to add a new book.


### 🛠️	Validate Data with Pydantic Models

#### Description
Add request and response models so your API enforces required fields and data types.

#### Requirements
Completed program should:

- Define a `BookCreate` model for incoming POST data.
- Define a `Book` model that includes an `id` field.
- Return a `404` status when a book id does not exist.
- Ensure invalid request data returns validation errors from FastAPI.


### 🛠️	Add Update and Delete Endpoints

#### Description
Complete the API by adding update and delete behavior for existing books.

#### Requirements
Completed program should:

- Implement `PUT /books/{book_id}` to update an existing book.
- Implement `DELETE /books/{book_id}` to remove a book.
- Return clear JSON messages for successful update and delete actions.
- Keep API responses consistent and easy to read for clients.
