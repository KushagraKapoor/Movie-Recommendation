# Movie Recommendation System

This project is a Django-based movie recommendation system that utilizes a cosine similarity model to provide personalized movie recommendations to users. The system includes user authentication, movie details views, and enhanced recommendation algorithms based on director and actor matches.

## Screenshots

![Homepage](https://example.com/screenshots/homepage.png)

![Movie Details](https://example.com/screenshots/movie_details.png)

![Recommendations](https://example.com/screenshots/recommendations.png)


## Features

- User authentication: Users can sign up, log in, and log out of the system.
- Movie details: Users can view detailed information about movies, including release date, director, genres, IMDb score, summary, actors, and awards.
- Recommendation system: Utilizes a cosine similarity model to calculate similarity scores between movies and provide personalized recommendations.
- Director and actor matches: Implements a new approach to scoring matches in directors and actors to enhance the quality and relevance of recommendations.
- Responsive design: The web application is designed to be responsive and user-friendly across devices.

## Technologies Used

- Django: Python-based web framework for building web applications.
- pandas: Library for data manipulation and analysis, used for handling movie data.
- joblib: Library for joblib for loading and saving models and data.
- HTML/CSS: Frontend technologies for designing the user interface.
- JavaScript: Used for client-side interactivity and form validation.
- SQLite: Database used for storing user data and movie information.

## Setup Instructions

1. Clone the repository to your local machine.
2. Install the required Python packages using `pip install -r requirements.txt`.
3. Run database migrations using `python manage.py migrate`.
4. Load initial movie data using `python manage.py loaddata movies_data.json`.
5. Start the development server using `python manage.py runserver`.
6. Access the web application at `http://localhost:8000/`.

## Project Structure

- `manage.py`: Django project management script.
- `recommendation_system/`: Django app containing views, models, templates, and static files.
- `static/`: Contains CSS, JavaScript, and image files for the frontend.
- `templates/`: HTML templates for rendering views.
- `movies_data.json`: JSON file containing initial movie data for loading into the database.

## Contributors

- [Kushaga Kapoor](https://github.com/kushagrakapoor) - Developer and project lead.

