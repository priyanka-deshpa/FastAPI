# FastAPI Vendor Management System

## Overview
This is a simple Vendor Management System built with FastAPI. It provides CRUD operations for managing vendors and includes user authentication with JWT-based authorization.

## Features
- **Vendor Management**: Create, read, update, and delete vendors.
- **User Authentication**: Register users and issue JWT access tokens.
- **Database Integration**: Uses SQLite with SQLAlchemy ORM.

## Requirements
- Python 3.8+
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- Passlib (for password hashing)
- PyJWT (for authentication)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/fastapi-vendor-management.git
   cd fastapi-vendor-management
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints
### User Authentication
- **Register a new user**: `POST /register/`
  - Request Body: `{ "email": "user@example.com", "password": "securepassword" }`
  - Response: `{ "access_token": "jwt_token", "token_type": "bearer" }`

### Vendor Management
- **Create a vendor**: `POST /vendors/`
- **Retrieve a vendor**: `GET /vendors/{vendor_id}`
- **Update a vendor**: `PUT /vendors/{vendor_id}`
- **Delete a vendor**: `DELETE /vendors/{vendor_id}`

## License
This project is licensed under the MIT License.

