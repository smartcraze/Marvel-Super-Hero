

# Marvel Superhero Collection

A simple Django-based web application to manage and display a collection of Marvel superheroes. This project was created as part of learning Django.

## Features

- Add, view, and manage a collection of superheroes.
- User-friendly UI to showcase superhero details.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS
- **Database**: SQLite (default Django database)

## Installation

Follow these steps to set up and run the project locally:

1. **Clone the repository**  
   Run the following command to clone the project:  
   ```bash
   git clone https://github.com/your-username/marvel-superhero-collection.git
   cd marvel-superhero-collection

2. Set up a virtual environment
Create and activate a virtual environment:

On Linux/Mac:
```

python -m venv venv
source venv/bin/activate

On Windows:

python -m venv venv
venv\Scripts\activate



3. Install dependencies
Install the required Python packages:

pip install -r requirements.txt


4. Run database migrations
Apply migrations to set up the database:

python manage.py migrate


5. Start the development server
Start the Django development server:

python manage.py runserver


6. Access the application
Open your browser and navigate to:

http://127.0.0.1:8000


```

# Project Structure
```
marvel-superhero-collection/
│
├── heroes/               # App with models, views, templates
├── marvel_superhero_collection/  # Main Django project files
├── templates/            # HTML templates
├── static/               # Static files (CSS, JS, Images)
├── db.sqlite3            # Database
├── manage.py             # Django management script
└── requirements.txt      # Project dependencies
```
How to Use

1. Access the app through the browser.


2. Add or view superheroes in the collection.


3. Use the Django admin panel for advanced management (optional).



Contributions

Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for more details.


---

Happy Coding!


