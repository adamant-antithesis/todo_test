Project "Your Task Manager"
The "Your Task Manager" is a web-based platform designed to help users manage their tasks. It allows users to create, update, delete, and track the status of tasks.

---Features

Task Management: Users can create tasks with titles, descriptions, and assigned users.

Status Tracking: Tasks can be assigned different statuses such as "In Progress," "Completed," or "Pending."

User Authentication: Secure user authentication system using Django's built-in authentication framework.

Responsive Design: The application is designed to be responsive and accessible on various devices and screen sizes.

Pagination: Tasks are paginated for better navigation and performance.

---Local Server Setup:

Requirements

    Python 3.x
    Django 3.x
    
---Installation and Configuration

1.Clone the repository:

    git clone https://github.com/adamant-antithesis/todo_test.git

2.Navigate to the task_manager_test directory (at the same level as the manage.py file):

    cd task_manager_test

3.Create a virtual environment (optional but recommended):

    python -m venv env

4. Activate the virtual environment:

    On Windows - env\Scripts\activate
    On macOS and Linux - source env/bin/activate

5.Install dependencies:

    pip install -r requirements.txt

6.Create a database with the name "task_manager_db":

Access the PostgreSQL shell by using the following command and press Enter:

    psql -U <username> (use the default username - postgres, password - postgres)

Once you are in the PostgreSQL shell, create the database "todobase" with the following command:

    CREATE DATABASE task_manager_db;

7.Exit the PostgreSQL shell:

To exit the PostgreSQL shell, type the command \q and press Enter.

8. Create .env file on 'task_manager_test' level

    SECRET_KEY=<your_secret_key>
    DB_PASSWORD=<your_db_password>

9.Create and apply migrations (you should be in the task_manager directory at the same level as the manage.py file):

    python manage.py makemigrations
    python manage.py migrate

10.Create a superuser to manage the admin panel:

    python manage.py createsuperuser

11.Run tests:

    python manage.py test

12.Start the server:

    python manage.py runserver



---Usage

Signup/Login: New users can sign up for an account, while existing users can log in using their credentials.

Task Creation: Users can create new tasks by providing a title, description, and optionally assigning them to other users.

Task Management: Users can view, update, and delete tasks from their dashboard.

Status Updates: Tasks can be marked as "In Progress," "Completed," or "Pending" etc. to track their progress.

Logout: Users can log out of their accounts to securely end their sessions.
