# Task & Project Management – Backend (Django)

## Test Credentials

### Admin
Email: admin@gmail.com  
Password: 123 

### User
Email: user@gmail.com  
Password: user123  

---

## Live URLs

- Backend API: <BACKEND_LIVE_URL>
- Frontend App: <FRONTEND_LIVE_URL>

---

## API Routes

### Authentication
- POST /api/auth/login/  
  Login and receive JWT token

- POST /api/auth/register/  
  Register New User

---

### Projects (Admin Only)
- GET /api/projects/  
  List all projects

- POST /api/projects/  
  Create a new project

---

### Tasks
- GET /api/tasks/  
  Admin: all tasks  
  User: only assigned tasks

- POST /api/tasks/  
  Admin only – create and assign task

- PATCH /api/tasks/{id}/  
  Update task status  
  Only admin can close overdue tasks

---

### Projects with Tasks (Read API)
- GET /api/projects-with-tasks/  
  Returns projects with related tasks  
  Admin sees all tasks  
  Users see only assigned tasks

---

### Overdue Task Handling (Django Feature)
- POST /api/run-overdue-check/  
  Admin only  
  Marks past-due tasks as OVERDUE  
  Returns count of updated tasks

---

## Setup

### Environment Variables (.env)

```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=task_manager
DB_USER=taskuser
DB_PASSWORD=taskpass
DB_HOST=localhost
DB_PORT=3306

ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:5173


```

Run Locally
docker compose up -d
python manage.py migrate
python manage.py runserver
