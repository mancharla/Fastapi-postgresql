# 🏥 Hospital FastAPI Project (PostgreSQL)

## 📌 Objective

Build a REST API using FastAPI to manage **Doctors** and **Patients** with proper validation and database integration.

---

## 🛠 Tech Stack

* Python 3.9+
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* Uvicorn

---

## 🚀 Features

* Doctor APIs (Create, List, Get by ID)
* Patient APIs (Create, List)
* PostgreSQL database integration
* Input validation using Pydantic
* Error handling using HTTPException

---

## 📂 Project Setup

### 1. Clone Repository

```bash
git clone <your-repo-link>
cd Hospital_api
```

---

### 2. Create Virtual Environment

```bash
python -m venv env
```

Activate environment:

**Windows:**

```bash
env\Scripts\activate
```

**Linux/Mac:**

```bash
source env/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic[email]
```

---

### 4. Setup PostgreSQL

Create database:

```sql
CREATE DATABASE hospital_db;
```

---

### 5. Configure Database

Update `DATABASE_URL` in `main.py`:

```python
DATABASE_URL = "postgresql://postgres:your_password@localhost:5432/hospital_db"
```

⚠️ If password contains special characters (like `@`), encode it:

* `@` → `%40`

Example:

```python
postgresql://postgres:abc%40245%40def@localhost:5432/hospital_db
```

---

### 6. Run the Application

```bash
uvicorn main:app --reload
```

---

### 7. Access API Docs

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 📌 API Endpoints

### 👨‍⚕️ Doctor APIs

| Method | Endpoint      | Description      |
| ------ | ------------- | ---------------- |
| POST   | /doctors      | Create doctor    |
| GET    | /doctors      | List doctors     |
| GET    | /doctors/{id} | Get doctor by ID |

---

### 🧑‍🤝‍🧑 Patient APIs

| Method | Endpoint  | Description    |
| ------ | --------- | -------------- |
| POST   | /patients | Create patient |
| GET    | /patients | List patients  |

---

## ✅ Validation Rules

* Email must be valid
* Age must be greater than 0
* Request validation using Pydantic

## ⚠️ Error Handling

* Uses FastAPI `HTTPException`
* Returns proper status codes (404, 422, etc.)

Include:

* Swagger UI (`/docs`)
* POST & GET API responses
* Database records (pgAdmin)

## 🧠 How It Works

1. FastAPI handles incoming requests
2. Pydantic validates request data
3. SQLAlchemy interacts with PostgreSQL
4. Data is stored/retrieved from database
5. Response is returned to client

