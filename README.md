# Task & Project Management – Backend (Django)

## Live URLs
- Backend API: https://angel-portal-backend.onrender.com/
- Frontend App: https://angel-portal-frontend.vercel.app/

---

## Test Credentials

### Admin
- Email: admin@gmail.com
- Password: 123

### Users
- Email: user@gmail.com  
  Password: user123

- Email: abc@gmail.com  
  Password: abc

---

## API Overview
Authentication: JWT (Authorization: Bearer <token>)

### Authentication
- `POST /api/auth/login/`  
  Login and receive JWT token

- `POST /api/auth/register/`  
  Register a new user

---

### Projects (Admin Only)
- `GET /api/projects/`  
  List all projects

- `POST /api/projects/`  
  Create a project

---

### Tasks
- `GET /api/tasks/`  
  Admin: all tasks  
  User: only assigned tasks

- `POST /api/tasks/`  
  Admin only – create and assign tasks

- `PATCH /api/tasks/{id}/`  
  Update task status  
  Only Admin can close overdue tasks

---

### Projects with Tasks
- `GET /api/projects-with-tasks/`  
  Returns projects with related tasks  
  Admin sees all tasks  
  Users see only assigned tasks

---

### Overdue Task Logic (Django Feature)
- `POST /api/run-overdue-check/`  
  Admin only  
  - Marks past-due tasks as `OVERDUE`
  - Overdue tasks cannot move back to `IN_PROGRESS`
  - Only Admin can close overdue tasks

---

## Setup (Local)

### Environment Variables
```env
SECRET_KEY=your-secret-key
DEBUG=True

MYSQL_DB_NAME=
MYSQL_USER=
MYSQL_PASSWORD=
MYSQL_HOST=
MYSQL_PORT=3306

ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:5173
```
---

### Run Locally
- `pip install -r requirements.txt`
- `docker compose up -d`
- `python manage.py migrate`
- `python manage.py runserver`

