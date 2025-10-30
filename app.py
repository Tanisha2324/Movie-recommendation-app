import streamlit as st
import pandas as pd

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="🎬 Movie Recommender",
    page_icon="🎥",
    layout="centered",
)

# -----------------------------
# Custom CSS styling
# -----------------------------
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #1f1c2c, #928dab);
        color: white;
    }
    .title {
        font-size: 48px;
        font-weight: 800;
        text-align: center;
        color: #FFD700;
        text-shadow: 2px 2px 10px #00000055;
    }
    .movie-card {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .movie-title {
        font-size: 22px;
        font-weight: 700;
        color: #00FFCC;
    }
    .movie-rating {
        color: #FFD700;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Movie Data
# -----------------------------
movies = pd.DataFrame({
    'Title': [
        'Inception', 'Titanic', 'Avengers: Endgame', 'The Dark Knight', 'La La Land',
        'The Conjuring', 'Interstellar', 'Frozen', 'Parasite', 'Dune',
        'Gladiator', 'Avatar', 'The Notebook', 'Joker', 'Toy Story',
        'Finding Nemo', 'Doctor Strange', 'Black Panther', 'Up', 'Inside Out',
        'Shutter Island', 'Us', 'The Matrix', 'Coco', 'The Lion King'
    ],
    'Genre': [
        'Sci-Fi', 'Romance', 'Action', 'Action', 'Romance',
        'Horror', 'Sci-Fi', 'Animation', 'Thriller', 'Sci-Fi',
        'Action', 'Sci-Fi', 'Romance', 'Drama', 'Animation',
        'Animation', 'Action', 'Action', 'Animation', 'Animation',
        'Thriller', 'Horror', 'Sci-Fi', 'Animation', 'Animation'
    ],
    'Rating': [
        8.8, 7.8, 8.4, 9.0, 8.0,
        7.5, 8.6, 7.4, 8.6, 8.3,
        8.5, 7.8, 7.9, 8.5, 8.3,
        8.2, 7.5, 7.3, 8.2, 8.1,
        8.1, 6.9, 8.7, 8.4, 8.5
    ],
    'Poster': [
        'https://m.media-amazon.com/images/I/51v5ZpFyaFL._AC_.jpg',  # Inception
        'https://m.media-amazon.com/images/I/71yAz0M0Q0L._AC_UF894,1000_QL80_.jpg',  # Titanic
        'https://m.media-amazon.com/images/I/81ExhpBEbHL._AC_SY679_.jpg',  # Avengers Endgame
        'https://m.media-amazon.com/images/I/71pox3sbRPL._AC_SY679_.jpg',  # Dark Knight
        'https://m.media-amazon.com/images/I/71eGx3bMT0L._AC_SY679_.jpg',  # La La Land
        'https://m.media-amazon.com/images/I/71WXIoa0aeL._AC_SY679_.jpg',  # Conjuring
        'https://m.media-amazon.com/images/I/91kFYg4fX3L._AC_SY679_.jpg',  # Interstellar
        'https://m.media-amazon.com/images/I/71Jxq3pJffL._AC_SY679_.jpg',  # Frozen
        'https://m.media-amazon.com/images/I/91TqDgq+EGL._AC_SY679_.jpg',  # Parasite
        'https://m.media-amazon.com/images/I/91m9r3gP0zL._AC_SY679_.jpg',  # Dune
        'https://m.media-amazon.com/images/I/51A3T9WgSGL._AC_.jpg',  # Gladiator
        'https://m.media-amazon.com/images/I/71c05lTE03L._AC_SY679_.jpg',  # Avatar
        'https://m.media-amazon.com/images/I/71oZ5k7tH5L._AC_SY679_.jpg',  # Notebook
