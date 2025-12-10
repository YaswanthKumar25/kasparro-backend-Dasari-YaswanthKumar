# Kasparro Backend & ETL Assignment  
**Author:** Dasari Yaswanth Kumar  

---

## 🚀 Project Overview  

This project implements a backend + ETL pipeline that:

- Fetches product data from an external API  
- Transforms and stores data in a relational database (SQLite)  
- Exposes product data via REST endpoints  
- Supports pagination, search, and ordering  

Built with **Django + Django REST Framework**, following clean architecture and coding standards.

---

## 📂 Folder Structure  

```text
kasparro-backend-Dasari-YaswanthKumar/
│
├── core/                      # Django project folder
│   ├── settings.py
│   └── urls.py
│
├── products/                  # Main app (ETL + API)
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── management/
│       └── commands/
│           └── run_etl.py    # ETL pipeline script
│
├── db.sqlite3                 # SQLite database
├── manage.py                  # Django manage file
├── requirements.txt           # Dependencies
└── README.md                  # This file
```

## 🔄 ETL Flow Diagram
```
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
      update_or_create() logic
              |
              v
+---------------------------+
|     SQLite Database       |
|    products_product       |
+-------------+-------------+
              |
              v
+---------------------------+
|    Django REST API        |
|     /api/products/        |
+---------------------------+
```
## 🌐 API Endpoints

GET /api/products/ — list all products (pagination, search, ordering)
GET /api/products/<id>/ — get details of a single product

## 🛠 Setup & Run
# 1. Clone / move to project folder  
cd kasparro-backend-Dasari-YaswanthKumar  

# 2. Activate virtual environment  
.\venv\Scripts\activate   # Windows  

# 3. Install dependencies (first time)  
pip install -r requirements.txt  

# 4. Apply migrations  
python manage.py makemigrations  
python manage.py migrate  

# 5. Run ETL to fetch and load external data  
python manage.py run_etl  

# 6. Start development server  
python manage.py runserver  

Then open in browser:
http://127.0.0.1:8000/api/products/ or http://127.0.0.1:8000/api/products/1/

## 🎯 Engineering Decisions

Django + DRF for clean REST API design
SQLite for simplicity and easy local setup
ETL via a Django management command — clear separation of concerns
Use of update_or_create() ensures idempotency & safe re-runs
Clean, modular project structure for maintainability

## 🔮 Future Improvements

Scheduled ETL (e.g. using cron or Celery)
Add authentication & permissions
More filtering options (price range, categories)
Error handling logging for ETL failures
Switch to a production-grade database if needed
