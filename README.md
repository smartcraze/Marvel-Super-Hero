Marvel Superhero Collection

Welcome to the Marvel Superhero Collection repository! This project is a simple web application built while learning Django. It showcases a collection of Marvel superheroes with details displayed on a user-friendly UI.

Features

Add, view, and manage a collection of Marvel superheroes.

User-friendly interface to display hero details.

Built using Django for the backend.


Requirements

Before running the project, ensure you have the following installed:

Python (version 3.8 or higher)

Django (version 4.x or higher)


Installation

1. Clone the repository:

git clone https://github.com/your-username/marvel-superhero-collection.git
cd marvel-superhero-collection


2. Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


3. Install the required packages:

pip install -r requirements.txt


4. Run the database migrations:

python manage.py migrate


5. Start the development server:

python manage.py runserver


6. Open your browser and navigate to http://127.0.0.1:8000 to view the application.



Usage

Add new superheroes to your collection via the admin panel or the app interface.

View the complete list of superheroes along with their details.


Project Structure

marvel_superhero_collection/ - Main Django project folder.

heroes/ - App containing superhero-related models, views, and templates.

templates/ - HTML files for the user interface.

static/ - Static files (CSS, JavaScript, images).


Contributions

Feel free to fork the repository and submit pull requests to improve the application or add new features.

License

This project is licensed under the MIT License. See the LICENSE file for details.


---

Happy coding! 😊

