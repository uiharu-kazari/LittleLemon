# Insomnia API Testing Guide

This guide provides step-by-step instructions for testing the LittleLemon API with Insomnia REST Client.

## Quick Start

### 1. Start the Django Server
```bash
cd c:\Users\chenguang_xu\Desktop\Sandbox\bd-capstone-project\littlelemon
conda activate django
python manage.py runserver
```

Server will run at: `http://127.0.0.1:8000`

### 2. Open Insomnia
- Download from https://insomnia.rest/ (if not already installed)
- Create a new Workspace or Request Collection

### 3. Register a New User

**Request Details:**
- **Method:** POST
- **URL:** `http://localhost:8000/restaurant/api/register/`
- **Content-Type:** JSON
- **Body:**
```json
{
    "username": "testuser",
    "password": "Test@Password123",
    "email": "testuser@example.com"
}
```

**Response:**
```json
{
    "message": "User created successfully",
    "token": "abc123def456xyz789",
    "username": "testuser"
}
```

**✅ Save the token!** You'll need it for all other requests.

---

## Setting Up Authentication

For all endpoints below (except login/register), you must include the authentication token:

1. Click the **Auth** tab in Insomnia
2. Select **Bearer Token** from the dropdown
3. Paste your token in the **Token** field

Alternatively, in the **Header** tab, add:
```
Authorization: Token abc123def456xyz789
```

---

## API Endpoints Testing

### User Login
**Method:** POST  
**URL:** `http://localhost:8000/restaurant/api/login/`  
**Auth:** None (public endpoint)

**Body:**
```json
{
    "username": "testuser",
    "password": "Test@Password123"
}
```

**Response:**
```json
{
    "message": "Login successful",
    "token": "new_token_xyz",
    "username": "testuser"
}
```

---

## Menu API

### List All Menu Items
**Method:** GET  
**URL:** `http://localhost:8000/restaurant/api/menu/`  
**Auth:** Bearer Token (Required)

**Expected Response:**
```json
[
    {
        "ID": 1,
        "title": "Pasta Carbonara",
        "price": "12.99",
        "inventory": 50
    },
    {
        "ID": 2,
        "title": "Pizza Margherita",
        "price": "15.50",
        "inventory": 40
    }
]
```

### Create a Menu Item
**Method:** POST  
**URL:** `http://localhost:8000/restaurant/api/menu/`  
**Auth:** Bearer Token (Required)

**Body:**
```json
{
    "title": "Grilled Salmon",
    "price": 24.99,
    "inventory": 25
}
```

**Expected Response (201 Created):**
```json
{
    "ID": 3,
    "title": "Grilled Salmon",
    "price": "24.99",
    "inventory": 25
}
```

### Get Specific Menu Item
**Method:** GET  
**URL:** `http://localhost:8000/restaurant/api/menu/1/`  
**Auth:** Bearer Token (Required)

**Expected Response:**
```json
{
    "ID": 1,
    "title": "Pasta Carbonara",
    "price": "12.99",
    "inventory": 50
}
```

### Update Menu Item
**Method:** PUT  
**URL:** `http://localhost:8000/restaurant/api/menu/1/`  
**Auth:** Bearer Token (Required)

**Body:**
```json
{
    "title": "Pasta Carbonara",
    "price": 13.99,
    "inventory": 45
}
```

**Expected Response:**
```json
{
    "ID": 1,
    "title": "Pasta Carbonara",
    "price": "13.99",
    "inventory": 45
}
```

### Partially Update Menu Item
**Method:** PATCH  
**URL:** `http://localhost:8000/restaurant/api/menu/1/`  
**Auth:** Bearer Token (Required)

**Body:**
```json
{
    "inventory": 30
}
```

### Delete Menu Item
**Method:** DELETE  
**URL:** `http://localhost:8000/restaurant/api/menu/1/`  
**Auth:** Bearer Token (Required)

**Expected Response:** 204 No Content

---

## Bookings API

### List All Bookings
**Method:** GET  
**URL:** `http://localhost:8000/restaurant/api/bookings/`  
**Auth:** Bearer Token (Required)

**Expected Response:**
```json
[
    {
        "ID": 1,
        "name": "John Doe",
        "no_of_guests": 4,
        "booking_date": "2025-12-20T19:00:00Z"
    }
]
```

### Create a Booking
**Method:** POST  
**URL:** `http://localhost:8000/restaurant/api/bookings/`  
**Auth:** Bearer Token (Required)

**Body:**
```json
{
    "name": "Jane Smith",
    "no_of_guests": 2,
    "booking_date": "2025-12-25T19:30:00Z"
}
```

**Expected Response (201 Created):**
```json
{
    "ID": 2,
    "name": "Jane Smith",
    "no_of_guests": 2,
    "booking_date": "2025-12-25T19:30:00Z"
}
```

### Get Specific Booking
**Method:** GET  
**URL:** `http://localhost:8000/restaurant/api/bookings/1/`  
**Auth:** Bearer Token (Required)

### Update Booking
**Method:** PUT  
**URL:** `http://localhost:8000/restaurant/api/bookings/1/`  
**Auth:** Bearer Token (Required)

**Body:**
```json
{
    "name": "John Doe",
    "no_of_guests": 5,
    "booking_date": "2025-12-20T20:00:00Z"
}
```

### Update Partial Booking Details
**Method:** PATCH  
**URL:** `http://localhost:8000/restaurant/api/bookings/1/`  
**Auth:** Bearer Token (Required)

**Body:**
```json
{
    "no_of_guests": 6
}
```

### Delete Booking
**Method:** DELETE  
**URL:** `http://localhost:8000/restaurant/api/bookings/1/`  
**Auth:** Bearer Token (Required)

**Expected Response:** 204 No Content

---

## Static HTML Content

### View Homepage
**Method:** GET  
**URL:** `http://localhost:8000/restaurant/`  
**Auth:** None

This serves the static `index.html` file.

---

## Django Admin Panel

### Access Admin
**URL:** `http://localhost:8000/admin/`

**Login with:**
- Username: (created during superuser setup)
- Password: (set during superuser setup)

You can manage Menu items and Bookings directly from the admin panel.

---

## Testing Workflow

### Recommended Test Sequence:

1. **✅ Register** - Create a user account
   - POST `/restaurant/api/register/`
   - Save the returned token

2. **✅ Add Auth** - Set up Bearer Token authentication in Insomnia
   - Copy token from step 1
   - Add to all subsequent requests

3. **✅ Test Menu Operations**
   - GET list: `/restaurant/api/menu/`
   - POST create: `/restaurant/api/menu/`
   - GET one: `/restaurant/api/menu/1/`
   - PUT update: `/restaurant/api/menu/1/`
   - DELETE: `/restaurant/api/menu/1/`

4. **✅ Test Booking Operations**
   - GET list: `/restaurant/api/bookings/`
   - POST create: `/restaurant/api/bookings/`
   - GET one: `/restaurant/api/bookings/1/`
   - PUT update: `/restaurant/api/bookings/1/`
   - DELETE: `/restaurant/api/bookings/1/`

5. **✅ Test Authentication**
   - POST login: `/restaurant/api/login/`
   - Verify token works for API calls

---

## Common Issues & Solutions

### 401 Unauthorized
- **Cause:** Missing or invalid authentication token
- **Fix:** Ensure Bearer Token is set in Auth tab or Header

### 400 Bad Request
- **Cause:** Missing required fields in request body
- **Fix:** Check that all required fields are included (e.g., `username`, `password`, `name`, `no_of_guests`)

### 404 Not Found
- **Cause:** Wrong URL or resource doesn't exist
- **Fix:** Verify the URL path and resource ID

### 500 Internal Server Error
- **Cause:** Server-side issue
- **Fix:** Check server console for error messages

### Token Expired
- **Fix:** Re-login to get a new token

---

## Sample Collection Export

You can import this as a collection in Insomnia for quick testing:

1. Create environment variable:
   - `base_url`: `http://localhost:8000`
   - `token`: (paste token here after registration)

2. Use in requests as:
   - `{{ base_url }}/restaurant/api/menu/`
   - Auth: `{{ token }}`

---

## Database Reset

If you need to clear all data and start fresh:

```bash
python manage.py flush
python manage.py migrate
```

Then create a new superuser and re-populate sample data.
