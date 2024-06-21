from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import pandas as pd
from django.http import JsonResponse
from django.shortcuts import render
from .utils import get_recommendations
import json

@login_required
def home(request):
    # Load the DataFrame from the pickle file
    movies_df = pd.read_pickle('recommendation system/movie_df.pkl')

    # Handle NaN values in the 'Languages' column by replacing them with an empty string
    movies_df['Languages'] = movies_df['Languages'].fillna('')

    # Extract movie titles from the 'Title' column, drop null values, and sort alphabetically
    movie_titles = sorted(movies_df['Title'].dropna().tolist())

    # Extract unique languages from the 'Languages' column, drop null values, and sort alphabetically
    languages = sorted(movies_df['Languages'].str.split(', ').explode().dropna().unique().tolist())

    return render(request, 'home.html', {'movie_titles': movie_titles, 'languages': languages})

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_auth:login")  # Redirect to the login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

def SignUpView(request):
    return render(request, "signup.html", {})

def custom_logout(request):
    logout(request)
    return redirect('login_auth:signup')  # Redirect to the signup page after logout

from django.shortcuts import render
import json

# Load the DataFrame
df_1 = pd.read_pickle('recommendation system/movie_df.pkl')

def recommend_movies(request):
    # Get selected_movies and languages from GET parameters
    selected_movies = request.GET.get('selected_movies', '[]')
    languages = request.GET.get('languages', '').split(',')

    # Convert selected_movies from JSON string to Python list
    selected_movies = json.loads(selected_movies)

    # Get movie recommendations using the recommendation function
    recommendations = get_recommendations(selected_movies, languages=languages)

    # Render the 'movie.html' template with recommendations
    return render(request, 'movie.html', {'recommendations': recommendations})



def movie_info(request, title):
    # Filter the DataFrame to get the movie details
    movie_row = df_1[df_1['Title'] == title].iloc[0]
    movie = {
        'title': movie_row['Title'],
        'image': movie_row['Image'],
        'release_date': movie_row.get('Release Date', 'N/A'),
        'director': movie_row.get('Director', 'N/A'),
        'genres': movie_row.get('Genre', 'N/A'),
        'imdb_score': movie_row.get('IMDb Score', 'N/A'),
        'summary': movie_row.get('Summary', 'N/A'),
        'actors': movie_row.get('Actors', 'N/A'),
        'awards_received': int(movie_row.get('Awards Received', 0)) if pd.notnull(movie_row.get('Awards Received')) else 'N/A',
        'awards_nominated_for': int(movie_row.get('Awards Nominated For', 0)) if pd.notnull(movie_row.get('Awards Nominated For')) else 'N/A'
    }
    return render(request, 'movie_info.html', {'movie': movie})
