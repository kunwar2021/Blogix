# 📝 Blogix – Unified Full-Stack Django Project

**Blogix** is a full-stack blog management system built as a single, unified **Django** application featuring:
- A dynamic HTML/Bootstrap web interface
- Django REST Framework (DRF) APIs
- JWT Authentication (`djangorestframework-simplejwt`)
- Admin Panel and User Management Dashboards

---

## 📌 Features

- 🔐 JWT-based authentication & session auth
- 📝 Full CRUD for blog posts, categories, and comments
- 👥 Role-based access control (admin, staff, authors)
- 📦 DRF-powered REST API endpoints
- 🖥️ Django admin panel & custom author dashboard
- 📁 Media upload support (images, thumbnails)

---

## 🛠 Tech Stack

| Technology              | Role                  |
|-------------------------|------------------------|
| Django 5.x              | Full-Stack Framework   |
| Django REST Framework   | REST API Layer         |
| SimpleJWT               | JWT Authentication     |
| SQLite3                 | Database               |
| HTML5 / CSS3 / Bootstrap| Web UI Templates       |

---

## 🚀 Getting Started

### 1. Set Up a Virtual Environment (Optional)

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Database Setup

```bash
cd e2_blog
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 5. Run Server

```bash
python manage.py runserver 127.0.0.1:8000
```

Access the application in your browser:
- **Web App Home**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Panel**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- **REST API Endpoints**: [http://127.0.0.1:8000/api/blogs/](http://127.0.0.1:8000/api/blogs/)

---

## 🌐 API Overview

### Authentication APIs

- `POST /api/token/` – Obtain JWT access and refresh tokens
- `POST /api/users/` – Register new user

### Blog APIs

- `GET /api/blogs/` – List all blog posts
- `POST /api/blogs/` – Create a blog post
- `GET /api/categories/` – List all categories
- `GET /api/comments/` – List all comments

---

## 🔐 Authentication

Protected REST API endpoints require a JWT token:

**Header Example:**

```http
Authorization: Bearer <your_jwt_token>
```
