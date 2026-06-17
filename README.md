# 🛍️ Products API (Django + DRF + Vanilla JS)

This is a simple full-stack project built with **Django**, **Django REST Framework**, and **Vanilla JavaScript**.
It demonstrates how to create a basic API and interact with it from the frontend using `fetch`.

---

## 🚀 Features

* Create a product (name, price)
* List all products
* REST API built with Django REST Framework
* Simple frontend using HTML, CSS, and Vanilla JS
* Fetch API integration

---

## 🧱 Tech Stack

* Backend: Django, Django REST Framework
* Frontend: HTML, CSS, JavaScript (Vanilla)
* API: RESTful (JSON)

---

## 📁 Project Structure

```
test_full_stack/
│
├── config/
├── full_stack/
├── .gitignore
├── index.html
├── LICENSE
└── manage.py
└── README.md
└── requirements.txt
└── style.css
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone git@github.com:turdialixasanbayev/full_stack_test.git
cd test_full_stack
```

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / Mac
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install django djangorestframework
```

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the server

```bash
python manage.py runserver
```

Server will run at:

```
http://127.0.0.1:8000/
```

---

## 🔌 API Endpoints

### GET - List Products

```
GET /api/products/
```

Response:

```json
[
  {
    "id": 1,
    "name": "Product 1",
    "price": "100.00"
  }
]
```

---

### POST - Create Product

```
POST /api/products/
```

Request body:

```json
{
  "name": "New Product",
  "price": 50
}
```

---

## 🌐 Frontend Usage

Open `index.html` in your browser.

Features:

* Add new product
* View product list
* Automatic refresh after creating product

---

## ⚠️ Notes

* Make sure Django server is running before using the frontend
* If frontend runs separately, enable CORS:

```bash
pip install django-cors-headers
```

Add to `settings.py`:

```python
INSTALLED_APPS = [
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True
```

---

## 📌 Future Improvements

* Update & Delete API
* Form validation
* Error handling
* Loading states
* Authentication (JWT)

---

## 👨‍💻 Author

Turdiali Xasanbayev

---

## 📄 License

This project is open-source and available for learning purposes.
