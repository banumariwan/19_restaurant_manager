# Restaurant Manager

A Django web application for managing restaurant tables, menu items, and orders with authentication and admin panel access.

## Features

- 🔐 **User Authentication**: Register and log in to access the system.  
- 👨‍💼 **Admin Panel**: Manage tables, menu items, and orders via Django admin.  
- 📝 **CRUD Operations**: Add, view, update, and delete menu items and orders.  
- 🍽️ **Order Management**: Assign orders to tables and view order details.  
- 🔍 **Filtering & Sorting**: Filter and sort students or menu items (depending on feature extension).  
- 🛡️ **Login Required**: All operations require authentication for security.

---

## Quick Start

### Clone Repository

```bash
git clone https://github.com/banumariwan/restaurant_manager.git
cd restaurant_manager
Install Dependencies
bash
Copy code
pip install django
Apply Migrations
bash
Copy code
python manage.py migrate
Create Superuser
bash
Copy code
python manage.py createsuperuser
Start Development Server
bash
Copy code
python manage.py runserver
Visit http://localhost:8000 to log in and manage the restaurant.

Project Structure
bash
Copy code
restaurant_manager/
│
├─ restaurant_manager/       # Django project configuration
├─ restaurant/               # Main app (tables, menu, orders)
│  ├─ migrations/
│  ├─ templates/
│  │   ├─ add_order.html
│  │   ├─ orders_list.html
│  │   └─ ...
│  ├─ models.py
│  ├─ views.py
│  ├─ forms.py
│  └─ urls.py
├─ manage.py
└─ README.md
Tech Stack
Python 3.x

Django 5.x

SQLite (default DB)

HTML/CSS for templates

Django Authentication
