import streamlit as st
import pickle
import gzip
import pandas as pd
import requests

# Set page title and layout
st.set_page_config(page_title="Movie Recommender System", page_icon="🎬", layout="wide")


def fetch_poster_by_search(movie_title):
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        url = f"http://www.omdbapi.com/?t={movie_title}&apikey=trilogy"
        res = requests.get(url, headers=headers, timeout=3)
        if res.status_code == 200:
            poster = res.json().get("Poster")
            if poster and poster != "N/A":
                return poster
    except Exception:
        pass


# Load preprocessed data and similarity matrix
@st.cache_data
def load_data():
    with gzip.open("movies.pkl.gz", "rb") as f:
        movies = pickle.load(f)
    with gzip.open("similar.pkl.gz", "rb") as f:
        similarity = pickle.load(f)
    return movies, similarity


movies, similarity = load_data()


def recommend(movie_title):
    movie_index = movies[movies["title"] == movie_title].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []
    recommendations_movie_poster = []

    for i in movie_list:
        title = movies.iloc[i[0]]["title"]
        recommendations.append(title)
        poster_url = fetch_poster_by_search(title)
        recommendations_movie_poster.append(poster_url)

    return recommendations, recommendations_movie_poster


st.title("🎬 Movie Recommender System")

movie_list = movies["title"].values
selected_movie = st.selectbox("Select a movie to get recommendations", movie_list)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)
    st.subheader(f"Movies similar to '{selected_movie}':")

    cols = st.columns(5)

    for idx, col in enumerate(cols):
        with col:
            if idx < len(names):
                st.text(names[idx])
                st.image(posters[idx], use_container_width=True)
