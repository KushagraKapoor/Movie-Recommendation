import joblib
import pandas as pd

# Load the DataFrame and similarity matrix
df = pd.read_pickle('recommendation system/movies_df.pkl')
cosine_sim = joblib.load('recommendation system/cosine_sim.pkl')
df_1 = pd.read_pickle('recommendation system/movie_df.pkl')

def get_recommendations(movie_titles, languages=[], num_recommendations=10):
    # Get indices of the input movies
    indices = [df[df['Title'] == title].index[0] for title in movie_titles if not df[df['Title'] == title].empty]
    
    # If no movies match the titles, return an empty list
    if not indices:
        return []

    # Calculate similarity scores for the input movies
    sim_scores = sum(cosine_sim[idx] for idx in indices) / len(indices)
    sim_scores = list(enumerate(sim_scores))

    # Get details of input movies for director and actors comparison
    input_movies_details = df.iloc[indices]

    # Adjust similarity scores based on language matches
    if languages:
        for i, (movie_idx, score) in enumerate(sim_scores):
            movie_details = df.iloc[movie_idx]
            movie_languages = movie_details['Languages']
            if any(lang in movie_languages for lang in languages):
                sim_scores[i] = (movie_idx, score * 2.0)  # Significantly increase the score for language matches

    # Adjust similarity scores based on director and actors matches
    for i, (movie_idx, score) in enumerate(sim_scores):
        movie_details = df.iloc[movie_idx]
        movie_director = movie_details['Director']
        movie_actors = set(movie_details['Actors'].split(', '))
        
        # Check if the movie director or any actor matches with the input movies
        for _, input_movie in input_movies_details.iterrows():
            input_director = input_movie['Director']
            input_actors = set(input_movie['Actors'].split(', '))
            
            if movie_director == input_director:
                score *= 1.2  # Increase score if director matches
            if not movie_actors.isdisjoint(input_actors):
                score *= 1.1  # Increase score if any actor matches
        
        sim_scores[i] = (movie_idx, score)
    
    # Sort the movies based on the adjusted similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices of the top movies, excluding the input movies
    movie_indices = [i[0] for i in sim_scores if i[0] not in indices][:num_recommendations]

    # Filter the recommended movies by selected languages
    recommended_movies = df.iloc[movie_indices]
    if languages:
        recommended_movies = recommended_movies[recommended_movies['Languages'].apply(lambda x: any(lang in x for lang in languages))]

    # Match titles from df with df_1 to get image URLs
    recommendations_with_images = []
    for index, row in recommended_movies.iterrows():
        title = row['Title']
        # Match title with df_1
        image_row = df_1[df_1['Title'] == title]
        if not image_row.empty:
            image_url = image_row.iloc[0]['Image']
            # Append title and image URL to recommendations list
            recommendations_with_images.append({'title': title, 'image': image_url})
    
    return recommendations_with_images
