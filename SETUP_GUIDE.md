# LittleLemon Django REST API - Setup Guide

This guide will help you set up and run the LittleLemon restaurant booking application with Django REST Framework, MySQL, and user authentication.

## Prerequisites

- Python 3.8+
- MySQL Server running locally
- Conda or pip for package management

## Installation Steps

### 1. Activate Django Environment
```bash
conda activate django
```

### 2. Create MySQL Database
Run the database creation script:
```bash
python create_db.py
```

Expected output:
```
✅ Database 'littlelemon_db' created or already exists
✅ MySQL connection is closed
```

**If you get connection errors:**
- Make sure MySQL is running
- Update credentials in `littlelemon/settings.py` if they're different:
  - Change `"USER": "root"` 
  - Change `"PASSWORD": "root"`
  - Change `"HOST": "localhost"`

### 3. Apply Migrations
```bash
python manage.py migrate
```

### 4. Create a Superuser (Admin)
```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 5. Load Sample Data (Optional)
```bash
python manage.py shell < add_sample_data.py
```

Or run migrations to populate initial data.

## Running the Server

```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`

## API Endpoints

### Authentication Endpoints

#### 1. User Registration
**POST** `/restaurant/api/register/`
```json
{
    "username": "john_doe",
    "password": "securepassword123",
    "email": "john@example.com"
}
```

Response:
```json
{
    "message": "User created successfully",
    "token": "abc123token456",
    "username": "john_doe"
}
```

#### 2. User Login
**POST** `/restaurant/api/login/`
```json
{
    "username": "john_doe",
    "password": "securepassword123"
}
```

Response:
```json
{
    "message": "Login successful",
    "token": "abc123token456",
    "username": "john_doe"
}
```

### Menu API Endpoints
(Requires Authentication - Add `Authorization: Token <token>` header)

#### List All Menu Items
**GET** `/restaurant/api/menu/`

#### Create Menu Item
**POST** `/restaurant/api/menu/`
```json
{
    "title": "Pasta Carbonara",
    "price": 12.99,
    "inventory": 50
}
```

#### Get Menu Item
**GET** `/restaurant/api/menu/{id}/`

#### Update Menu Item
**PUT** `/restaurant/api/menu/{id}/`
```json
{
    "title": "Pasta Carbonara",
    "price": 13.99,
    "inventory": 45
}
```

#### Delete Menu Item
**DELETE** `/restaurant/api/menu/{id}/`

### Table Booking API Endpoints
(Requires Authentication - Add `Authorization: Token <token>` header)

#### List All Bookings
**GET** `/restaurant/api/bookings/`

#### Create Booking
**POST** `/restaurant/api/bookings/`
```json
{
    "name": "John Doe",
    "no_of_guests": 4,
    "booking_date": "2025-12-20T19:00:00Z"
}
```

#### Get Booking
**GET** `/restaurant/api/bookings/{id}/`

#### Update Booking
**PUT** `/restaurant/api/bookings/{id}/`
```json
{
    "name": "John Doe",
    "no_of_guests": 5,
    "booking_date": "2025-12-20T19:30:00Z"
}
```

#### Delete Booking
**DELETE** `/restaurant/api/bookings/{id}/`

## Testing with Insomnia

1. **Download Insomnia** from https://insomnia.rest/

2. **Create a new request collection** for LittleLemon API

3. **First, Register/Login** to get an authentication token:
   - Method: POST
   - URL: `http://localhost:8000/restaurant/api/register/`
   - Body (JSON):
     ```json
     {
         "username": "testuser",
         "password": "testpass123"
     }
     ```
   - Copy the returned `token`

4. **Set up Authentication for subsequent requests:**
   - For each API request, go to the **Auth** tab
   - Select **Bearer Token**
   - Paste the token from step 3

5. **Test Menu API:**
   - GET: `http://localhost:8000/restaurant/api/menu/`
   - POST: `http://localhost:8000/restaurant/api/menu/` with JSON body

6. **Test Booking API:**
   - GET: `http://localhost:8000/restaurant/api/bookings/`
   - POST: `http://localhost:8000/restaurant/api/bookings/` with JSON body

## Running Unit Tests

Run all tests:
```bash
python manage.py test
```

Run specific test file:
```bash
python manage.py test tests.test_views
python manage.py test tests.test_models
```

## Admin Panel

Access Django admin at: `http://localhost:8000/admin/`
- Use superuser credentials created in step 4
- Manage Menu items and Bookings directly

## Database Schema

### Menu Table
- ID (Primary Key)
- title (CharField)
- price (DecimalField)
- inventory (IntegerField)

### Booking Table
- ID (Primary Key)
- name (CharField)
- no_of_guests (IntegerField)
- booking_date (DateTimeField)

### User Table (Django Default)
- id (Primary Key)
- username
- password
- email
- etc.

## Troubleshooting

### MySQL Connection Error
- Verify MySQL is running: `mysql -u root -p`
- Check credentials in `littlelemon/settings.py`
- Run `python create_db.py` again

### Migration Errors
```bash
python manage.py makemigrations
python manage.py migrate
```

### Token Authentication Issues
- Always include `Authorization: Token <your_token>` header
- Get new token if expired
- Check token is correctly copied

### Static Files Not Loading
```bash
python manage.py collectstatic
```

## Project Structure

```
littlelemon/
├── manage.py
├── littlelemon/
│   ├── settings.py (Database & REST Framework config)
│   ├── urls.py
│   └── wsgi.py
├── restaurant/
│   ├── models.py (Menu, Booking models)
│   ├── views.py (API Views & Authentication)
│   ├── serializers.py
│   ├── urls.py (API routes)
│   └── migrations/
├── tests/
│   ├── test_models.py
│   └── test_views.py
├── templates/
│   └── index.html
├── create_db.py (MySQL database setup)
└── add_sample_data.py (Sample data population)
```

## Features Implemented

✅ Django REST Framework API  
✅ MySQL Database Integration  
✅ Token-based Authentication  
✅ User Registration & Login  
✅ Menu CRUD Operations  
✅ Table Booking CRUD Operations  
✅ Unit Tests  
✅ Static HTML Content Serving  
✅ Git Version Control  

All assignment criteria are now met!
