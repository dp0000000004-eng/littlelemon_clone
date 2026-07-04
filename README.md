# 🍋 Little Lemon Restaurant Management System

A Django-based web application designed to manage restaurant operations such as reservations, menu items, and customer interactions. Built as a learning project to practice Django models, views, forms, and templates.

---

## ✨ Features
- **Reservation Management**: Add, view, and manage customer bookings.
- **Menu Management**: Create and update menu items with details like name, description, and price.
- **User Authentication**: Secure login/logout system for staff.
- **Admin Dashboard**: Manage reservations and menu items through Django’s built-in admin.
- **Responsive UI**: Simple, clean interface for easy navigation.

---

## 🛠️ Tech Stack
- **Backend**: Django (Python)
- **Database**: SQLite 
- **Frontend**: HTML, CSS, Django Templates
- **Other Tools**: Django ORM, Django Admin

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/littlelemon.git
   cd littlelemon

2. **Create and activate a virtual envirnoment**
    ```bash 
    python -m venv venv
    source venv/bin/activate   # On Linux/Mac
    venv\Scripts\activate      # On Windows
3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    Run migrations
4. **Run Migratoins**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    Create a superuser 
5. **Create Superser for Admin Panel**
    ```bash
    python manage.py createsuperuser
    Start the development server`
5. **Run Deployment Server**
    ```bash
    python manage.py runserver
    ```
## 🚀 Usage
- Visit http://127.0.0.1:8000/ to access the app.

- Use the Admin Panel at http://127.0.0.1:8000/admin/ to manage reservations and menu items.

- Customers can view the menu and make reservations via the frontend.


## 🤝 Contributing
- Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

## 📜 License
- This project is licensed under the MIT License — feel free to use and modify it.

## 🙌 Acknowledgments
- Inspired by the Little Lemon Restaurant project idea.

- Thanks to Django’s amazing documentation and tutorials.

