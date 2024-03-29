Project "Your Task Manager"
The "Your Task Manager" is a web-based app designed to help users manage their tasks. It allows users to create, update, delete, and track the status of tasks.

---Features

-Task Management: Users can create tasks with titles, descriptions, and assigned users.

-Status Tracking: Tasks can be assigned different statuses such as "In Progress," "Resolved," or "On Hold" etc.

-User Authentication: Secure user authentication system using Django's built-in authentication framework.

-Responsive Design: The application is designed to be responsive and accessible on various devices and screen sizes.

-Pagination: Tasks are paginated for better navigation and performance.

---Local Server Setup:

Requirements

    Python 3.x
    asgiref==3.7.2
    Django==5.0.3
    psycopg2==2.9.9
    python-dotenv==1.0.1
    sqlparse==0.4.4
    tzdata==2024.1
    
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

Once you are in the PostgreSQL shell, create the database "task_manager_db" with the following command:

    CREATE DATABASE task_manager_db;

7.Exit the PostgreSQL shell:

To exit the PostgreSQL shell, type the command \q and press Enter.


8. Create .env file on 'task_manager_test' level.

   SECRET_KEY=<your_secret_key>

   DB_PASSWORD=<your_db_password>

                                               !!! IMPORTANT !!! 
To generate your SECRET_KEY you can use command -

    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'


9.Create and apply migrations (you should be in the 'task_manager_test' directory at the same level as the manage.py file):

    python manage.py makemigrations
    python manage.py migrate

10.Create a superuser to manage the admin panel:

    python manage.py createsuperuser

11.Run tests:

    python manage.py test

12.Start the server:

    python manage.py runserver

