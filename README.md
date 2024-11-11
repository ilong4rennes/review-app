# Review-Master

**Review-Master** is a Django-based web application similar to Yelp, where users can review various businesses and services. This README will guide you through setting up and running the project on your local machine.

## Prerequisites

To run Review-Master, you need the following installed on your system:

- **Python** (latest version)
- **Homebrew** (for macOS users)
- **PostgreSQL** (version 14)

## Getting Started

### Step 1: Fork and Clone the Repository

1. **Fork this repository** on GitHub to make your own copy.
2. **Clone the repository** to your local machine:
   ```bash
   git clone https://github.com/ilong4rennes/review-master.git
   cd review-master
   ```

### Step 2: Install Python and Virtual Environment

1. **Install Python** (if not already installed):
   ```bash
   brew install python
   ```

   Note: `pip`, Python’s package manager, will be installed automatically.

2. **Install Virtualenv** (if not already installed):
   ```bash
   pip3 install virtualenv
   ```

### Step 3: Install and Configure PostgreSQL

1. **Install PostgreSQL 14**:
   ```bash
   brew install postgresql@14
   ```

2. **Start the PostgreSQL service**:
   ```bash
   brew services start postgresql@14
   ```

3. **Create a PostgreSQL Database and User**:

   - Open the PostgreSQL interactive terminal:
     ```bash
     psql postgres
     ```

   - Run the following commands in the terminal to set up your database and user:
     ```sql
     CREATE DATABASE mydb;
     CREATE USER myuser WITH PASSWORD 'mypassword';
     ALTER ROLE myuser SET client_encoding TO 'utf8';
     ALTER ROLE myuser SET default_transaction_isolation TO 'read committed';
     ALTER ROLE myuser SET timezone TO 'UTC';
     GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;
     ```

   - Exit the PostgreSQL terminal by typing `\q`.

### Step 4: Set Up the Django Project

1. **Create and Activate a Virtual Environment**:
   ```bash
   virtualenv venv
   source venv/bin/activate
   ```

2. **Install the Required Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the Database Settings**:
   - In the Django project directory, open `settings.py`.
   - Update the database configuration to match the PostgreSQL setup:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'mydb',
             'USER': 'myuser',
             'PASSWORD': 'mypassword',
             'HOST': 'localhost',
             'PORT': '',
         }
     }
     ```

4. **Run Database Migrations**:
   ```bash
   python manage.py migrate
   ```

### Step 5: Create a Superuser for the Admin Panel

To access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up an admin account.

### Step 6: Run the Django Development Server

1. **Start the server**:
   ```bash
   python manage.py runserver
   ```

2. Open a browser and navigate to `http://127.0.0.1:8000/reviewmaster` to view the application.

To access the admin panel, go to `http://127.0.0.1:8000/admin` and log in with the superuser credentials you created.

---

This completes the setup for Review-Master. Enjoy exploring your Yelp-like web application!
