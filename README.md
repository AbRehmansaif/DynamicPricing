# 🧠 Dynamic Pricing System

A Django-based web application that automatically predicts and adjusts product prices based on sales trends using machine learning.

---

## 🚀 Features

- 📊 AI-powered price prediction using historical sales data
- 🛍️ Product management with base, max, and selling prices
- 📈 Weekly sales analysis and trend tracking
- ⚙️ Admin dashboard to view and manage products
- 🧠 Integrated ML model (Random Forest Regressor)
- 🗃️ API support using Django REST Framework (optional)

---

## 🏗️ Tech Stack

- Backend: Django, Django REST Framework
- ML: Scikit-learn, Pandas, Joblib
- Frontend: HTML, Tailwind CSS (optional)
- Database: SQLite (default, easy to change)
- Environment: Python 3.x, Virtualenv

---

## 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/AbRehmansaif/DynamicPricing.git
   cd DynamicPricing
2. **Create and activate virtual environment**
   ```bash
    python -m venv env
    source env/bin/activate    # Linux/macOS
    .\env\Scripts\activate     # Windows
   ```
3. ***Install dependencies***
   ```bash
   pip install -r requirements.txt
   ```
4. ***Apply migrations***
   ```bash
     python manage.py makemigrations
     python manage.py migrate
   ```
5. ***Create superuser***
   - For admin access
  ```bash
    python manage.py createsuperuser
  ```
6. ***Run the server***
  ```bash
    python manage.py runserver
  ```

**📁 Project Structure**
  
  ![image](https://github.com/user-attachments/assets/da36d8c5-70e2-47ed-8f4d-e4430d4c2148)

**🤖 Machine Learning Model**
  - Model: RandomForestRegressor
 - Features: weekly_sales, last_week_sales, base_price
 - Output: predicted_selling_price
 - Stored using: joblib

You can retrain the model with:
  ```bash
    python pricing/ml/train_model.py
  ```

## 📬 Contact
Developer: Abdul Rehman
Email: abdulrehmanarain713@gmail.com
LinkedIn: [Your LinkedIn](https://www.linkedin.com/in/abdul-rehman-ssuetian/)



