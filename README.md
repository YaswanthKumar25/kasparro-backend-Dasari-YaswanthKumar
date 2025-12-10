# Kasparro Backend & ETL Assignment  
**Author:** Dasari Yaswanth Kumar  
**Track:** Backend & ETL Systems  

---

## 🔍 Overview

This project implements the Backend & ETL challenge assigned by Kasparro.

It includes:

- ETL pipeline fetching data from an external API  
- Transforming and loading data into a relational database  
- Exposing RESTful API endpoints to access the ingested data  
- Search, ordering, and pagination support  

The goal is to demonstrate clear engineering, modular design, and production-style thinking.

---

## 🏗 Architecture & Design

The system is divided into **three clean components**:

### **1️⃣ ETL Pipeline**
- Fetches data from: `https://fakestoreapi.com/products`
- Parses JSON response
- Loads data into SQLite DB
- Uses `update_or_create()` for:
  - Avoiding duplicates  
  - Allowing safe multiple ETL runs  
  - Providing basic recovery logic  

### **2️⃣ Database Layer – SQLite**
- Simple relational storage
- Uses Django ORM
- Suitable for assignment and local execution

### **3️⃣ REST API Layer**
Implemented using Django REST Framework:

- Retrieve list of products
- Retrieve single product
- Search (`?search=`)  
- Ordering (`?ordering=`)  
- Pagination (DRF default)

---

📂 Folder Structure
-------------------
kasparro-backend-Dasari-YaswanthKumar/
│
├── core/
│   ├── settings.py
│   └── urls.py
│
├── products/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── management/
│   │   └── commands/
│   │       └── run_etl.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md

🔄 ETL Flow Diagram
-------------------
+---------------------------+
|   External API (JSON)     |
|   fakestoreapi.com        |
+-------------+-------------+
              |
              v
+---------------------------+
|       ETL Pipeline        |
|   (run_etl command)       |
+-------------+-------------+
              |
     update_or_create()
              |
              v
+---------------------------+
|     SQLite Database       |
|     products_product      |
+-------------+-------------+
              |
              v
+---------------------------+
|     Django REST API       |
|   /api/products/          |
+---------------------------+


## 🧩 API Endpoints

### **GET /api/products/**
Returns the list of all products  
Supports:
- Pagination  
- Search: `?search=laptop`  
- Ordering: `?ordering=price`  

### **GET /api/products/<id>/**
Returns a single product.

---

## 🛠 How to Run the Project

### **1. Move to project directory**
cd kasparro-backend-Dasari-YaswanthKumar
2. Activate virtual environment
.\venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Apply migrations
python manage.py makemigrations
python manage.py migrate
5. Run ETL
python manage.py run_etl
6. Start server
python manage.py runserver
7. Open APIs
http://127.0.0.1:8000/api/products/
http://127.0.0.1:8000/api/products/1/
📌 Engineering Choices
Django REST Framework for clarity and rapid API development

SQLite as a lightweight and simple relational DB

ETL written as a Django management command

update_or_create() ensures idempotency and recovery

API design follows REST principles

Clean, modular folder structure

🚀 Future Enhancements
Scheduled ETL (Celery + cron)

Add authentication

Add category filtering

Centralized logging for ETL errors

Multi-source ingestion

