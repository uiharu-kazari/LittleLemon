LittleLemon Restaurant API - Test Endpoints
=============================================

This file contains all API endpoints that peers should test.

Total API Endpoints: 9

=== Authentication Endpoints (No Token Required) ===

1. /restaurant/api/register/
   Method: POST
   Purpose: User registration
   Required Fields: username, password, email (optional)
   Example: 
   {
       "username": "testuser",
       "password": "password123",
       "email": "test@example.com"
   }

2. /restaurant/api/login/
   Method: POST
   Purpose: User login and token retrieval
   Required Fields: username, password
   Example:
   {
       "username": "testuser",
       "password": "password123"
   }

=== Menu API Endpoints (Token Required) ===

3. /restaurant/api/menu/
   Method: GET
   Purpose: List all menu items
   Auth: Bearer Token

4. /restaurant/api/menu/
   Method: POST
   Purpose: Create new menu item
   Auth: Bearer Token
   Required Fields: title, price, inventory
   Example:
   {
       "title": "Grilled Salmon",
       "price": 24.99,
       "inventory": 25
   }

5. /restaurant/api/menu/{id}/
   Method: GET
   Purpose: Retrieve specific menu item
   Auth: Bearer Token

6. /restaurant/api/menu/{id}/
   Method: PUT
   Purpose: Update menu item (full update)
   Auth: Bearer Token
   Example:
   {
       "title": "Grilled Salmon",
       "price": 25.99,
       "inventory": 20
   }

7. /restaurant/api/menu/{id}/
   Method: PATCH
   Purpose: Partial update of menu item
   Auth: Bearer Token

8. /restaurant/api/menu/{id}/
   Method: DELETE
   Purpose: Delete menu item
   Auth: Bearer Token

=== Table Booking API Endpoints (Token Required) ===

9. /restaurant/api/bookings/
   Method: GET
   Purpose: List all table bookings
   Auth: Bearer Token

10. /restaurant/api/bookings/
    Method: POST
    Purpose: Create new table booking
    Auth: Bearer Token
    Required Fields: name, no_of_guests, booking_date
    Example:
    {
        "name": "John Doe",
        "no_of_guests": 4,
        "booking_date": "2025-12-25T19:30:00Z"
    }

11. /restaurant/api/bookings/{id}/
    Method: GET
    Purpose: Retrieve specific booking
    Auth: Bearer Token

12. /restaurant/api/bookings/{id}/
    Method: PUT
    Purpose: Update booking (full update)
    Auth: Bearer Token

13. /restaurant/api/bookings/{id}/
    Method: PATCH
    Purpose: Partial update of booking
    Auth: Bearer Token

14. /restaurant/api/bookings/{id}/
    Method: DELETE
    Purpose: Delete booking
    Auth: Bearer Token

=== Static Content ===

15. /restaurant/
    Method: GET
    Purpose: View static HTML homepage
    Auth: None required

=== Admin Panel ===

/admin/
    Purpose: Django admin panel for managing data
    Auth: Superuser credentials

=== Testing Instructions ===

1. Start the server:
   python manage.py runserver

2. Register a user via /restaurant/api/register/
   
3. Use the returned token for all subsequent requests
   (Add to header: Authorization: Token <your_token>)

4. Test all endpoints using Insomnia REST Client

5. Run unit tests:
   python manage.py test tests --verbosity=2

=== Additional Documentation ===

See SETUP_GUIDE.md for installation instructions
See INSOMNIA_TESTING_GUIDE.md for detailed testing examples
See ASSIGNMENT_VERIFICATION.md for criteria verification
