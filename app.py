import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster_by_search(movie_title):
    try:
        response = requests.get(
            f'https://api.themoviedb.org/3/search/movie?api_key=d33723eed56fc8a8fea33e606fd7feb4&query={movie_title}'
        )
        data = response.json()
        if data['results'] and data['results'][0]['poster_path']:
            return "http://image.tmdb.org/t/p/w500/" + data['results'][0]['poster_path']
    except:
        pass
    return "https://via.placeholder.com/500x750?text=No+Poster"


movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similar.pkl', 'rb'))


def recommend(movie_title):
    movie_index = movies[movies['title'] == movie_title].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []
    recommendations_movie_poster = []

    for i in movie_list:
        movie_title = movies.iloc[i[0]]['title']
        recommendations.append(movie_title)
        poster_url = fetch_poster_by_search(movie_title)
        recommendations_movie_poster.append(poster_url)

    return recommendations, recommendations_movie_poster


st.title("🎬 Movie Recommender System")

movie_list = movies['title'].values
selected_movie = st.selectbox("Select a movie to get recommendations", movie_list)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)
    st.subheader(f"Movies similar to '{selected_movie}':")

    cols = st.columns(5)

    for idx, col in enumerate(cols):
        with col:
            if idx < len(names):
                st.text(names[idx])
                st.image(posters[idx])