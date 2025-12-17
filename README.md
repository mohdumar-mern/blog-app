# 📝 Django Blog Application

A simple and clean **Blog Web Application** built using **Django**.  
This project supports user authentication, post creation, media uploads, and is production-ready for deployment on platforms like **Render**.

---

## 🚀 Features

- User Registration & Login (Django Auth)
- Create & View Blog Posts
- Author name auto-linked with logged-in user
- Image upload support (Post Banner)
- Slug-based post URLs
- Static & Media file handling
- Clean UI with custom CSS
- SQLite database (easy setup)
- Production-ready settings

---

## 🛠 Tech Stack

- **Backend:** Django 6.0
- **Database:** SQLite
- **Frontend:** HTML, CSS, JavaScript
- **Authentication:** Django Built-in Auth
- **Deployment:** Render
- **Server:** Gunicorn
- **Static Files:** Whitenoise

---

## 📁 Project Structure

myproject/
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── posts/
│   ├── templates/
│   │   └── posts/
│   │       ├── post_new.html
│   │       ├── post_page.html
│   │       └── post_list.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── test.py
├── users/
│   ├── templates/
│   │   └── users/
│   │       ├── login.html
│   │       └── register.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── test.py
├── templates/
├── static/
├── media/
├── db.sqlite3
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md

---

## ⚙️ Installation (Local Setup)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/mohdumar-mern/blog-app
cd blog-app

py -m venv .venv
source .venv/bin/activate   # Linux/Mac
source .venv\Scripts\activate      # Windows

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
http://127.0.0.1:8000/

```

## 🌌 Media & Static Files

- Media files stored in /media/
- Static files served using Whitenoise
- Works in both development & production

---

## 🌐 Deployment (Render)

### Build Command

- pip install -r requirements.txt
- gunicorn myproject.wsgi
- DEBUG=False
- ALLOWED_HOSTS=your-render-url.onrender.com

## 🔐 Authentication Flow

- Register → Auto Login
- Login → Redirect to posts
- Logout → Redirect to login page
- Author name automatically assigned from logged-in user

## 📌 Future Improvements

- Comments system
- Likes & bookmarks
- Rich text editor
- Pagination
- Search functionality
- User profiles

## 👨‍💻 Author

### Mohd Umar

*Full Stack Developer (MERN + Python/Django)*

GitHub: https://github.com/mohdumar-mern

LinkedIn: https://www.linkedin.com/in/mohd-umar-mern-stack-developer/

## ⭐ Support

If you like this project:

- ⭐ Star the repo
- 🍴 Fork it
- 🧠 Learn Django deeply

## 📄 License

This project is open-source and available under the MIT License.