DjangoSite

An example Django website using Django

🛠️ Features

Project Showcase: Display a portfolio of projects with descriptions and technologies used.

User Authentication: Secure login and registration system for users.

Responsive Design: Ensures usability across various devices.
Real Python
+1

🚀 Installation

Clone the repository:

git clone https://github.com/marjanrezaei/djangosite.git
cd djangosite


Set up a virtual environment:

python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`


Install dependencies:

pip install -r requirements.txt


Apply migrations:

python manage.py migrate


Create a superuser:

python manage.py createsuperuser


Run the development server:

python manage.py runserver


Access the application at http://127.0.0.1:8000
.

📂 Project Structure

accounts/: Handles user authentication and profiles.

blog/: Manages blog posts and related content.

djangosite/: Contains the main project settings and configurations.

media/: Stores user-uploaded files.

statics/: Contains static files like CSS, JavaScript, and images.

templates/: Holds HTML templates for rendering views.

website/: Handles the main website content and pages.
Real Python

🧪 Testing

To run tests, use:

python manage.py test

📄 License

This project is licensed under the MIT License.
GitHub

Feel free to modify this template to better fit your project's specifics. If you need further assistance or additional sections, such as deployment instructions or API documentation, don't hesitate to ask!
