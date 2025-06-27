# Flask REST API - User Management

This is a simple RESTful API built with Flask that allows for managing user data. It supports CRUD operations (Create, Read, Update, Delete) using an in-memory Python list.

## 📌 Features

- Get all users
- Get a user by ID
- Add a new user
- Update user information
- Delete a user

## 🛠️ Technologies Used

- Python 3
- Flask

## 🚀 How to Run

1. **Clone the repository**
bash
`git clone https://github.com/Tapas2001/user-management-api.git`
`cd user-management-api `

2. Install dependencies
bash
pip install flask

3. Run the app
bash
python app.py

## 📬 API Endpoints

| Method | Endpoint      | Description         |
| ------ | ------------- | ------------------- |
| GET    | `/users`      | Get all users       |
| GET    | `/users/<id>` | Get a user by ID    |
| POST   | `/users`      | Add a new user      |
| PUT    | `/users/<id>` | Update a user by ID |
| DELETE | `/users/<id>` | Delete a user by ID |


## 🧪 Sample JSON for POST/PUT
json

  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  }




