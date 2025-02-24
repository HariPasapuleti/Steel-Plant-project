# Steel Plant Machine Management System

## Overview
The Steel Plant Machine Management System is a Django-based web application designed to streamline the management of machines in a steel plant. The system allows employees to log in, add new machines, view machine details, and raise complaints regarding machine issues. The project utilizes a user authentication system and email confirmation for account activation.

---
## Features
- **User Authentication**: Secure login and signup with email confirmation for account activation.
- **Add Machine**: Employees can add new machines with details such as name, model, manufacturer, and location.
- **View Machines**: Displays a list of machines with detailed information and an image.
- **Raise Complaints**: Employees can raise complaints for specific machines, which are indexed and stored.
- **Responsive Design**: User-friendly interface with Bootstrap for responsiveness.

---
## Technology Stack
- **Backend**: Django
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite
- **Email Integration**: Django Email Framework

---
## Installation

### Prerequisites
- Python 3.8 or above
- Django 4.x

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/HariPasapuleti/Steel-Plant-project.git
   cd Steel-Plant-project
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations to set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`.

---
## Configuration

### Email Settings
To enable email confirmation for user signup, configure the email settings in `settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<your-email-password>'
```

### Static and Media Files
Ensure static and media files are configured correctly:
```python
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Run the following command to collect static files:
```bash
python manage.py collectstatic
```

---
## Usage

### User Authentication
1. Sign up on the homepage with a unique username, email, and password.
2. Confirm your email address using the link sent to your registered email.
3. Log in with your credentials.

### Machine Management
1. Navigate to the "Add New Machine" page to add machine details.
2. View all machines on the "Machine Details" page.
3. Raise complaints for specific machines by submitting the complaint text in the form provided.

---
## Project Structure
```
steel-plant-management/
├── authentication/       # User authentication app
│   ├── templates/
│   │   ├── authentication/
│   │   │   ├── signup.html
│   │   │   ├── signin.html
│   │   │   ├── index.html
│   │   └── email_confirmation.html
│   ├── views.py          # Authentication views
│   └── tokens.py         # Email token generation
├── machine/              # Machine management app
│   ├── templates/
│   │   ├── machine/
│   │   │   ├── add_machine.html
│   │   │   ├── machine_list.html
│   ├── views.py          # Machine views
│   ├── forms.py          # Machine forms
│   ├── models.py         # Machine models
├── steel_plant/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
└── manage.py             # Django management script
```

<!--
## Screenshots
### Home Page
![Home Page](screenshots/home.png)

### Machine List
![Machine List](screenshots/machine_list.png)
-->

---
## Future Enhancements
- Add a feature for machine status tracking.
- Implement role-based access for different user levels.
- Integrate complaint resolution notifications.

---
## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
