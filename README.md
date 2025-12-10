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
