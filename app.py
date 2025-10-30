import streamlit as st
import pandas as pd

# ===================== PAGE CONFIG =====================
st.set_page_config(page_title="🎬 Movie Recommendation App", layout="wide")

# ===================== CUSTOM CSS =====================
st.markdown("""
    <style>
        body {
            background-color: black;
            color: white;
        }
        .stApp {
            background-color: #000000;
        }
        .movie-card {
            background-color: #1a1a1a;
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0px 0px 10px rgba(255,255,255,0.1);
        }
        img {
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# ===================== MOVIE DATA =====================
movies = pd.DataFrame({
    "Title": [
        "Inception", "The Dark Knight", "Interstellar", "Avengers: Endgame", "The Matrix",
        "Titanic", "Avatar", "Joker", "The Shawshank Redemption", "Forrest Gump",
        "The Godfather", "Pulp Fiction", "Fight Club", "The Lion King", "Frozen",
        "Toy Story", "Up", "Finding Nemo", "Coco", "Inside Out",
        "Black Panther", "Doctor Strange", "Iron Man", "Thor: Ragnarok", "Spider-Man: No Way Home",
        "Guardians of the Galaxy", "Ant-Man", "Captain Marvel", "Eternals", "The Flash",
        "Batman Begins", "Man of Steel", "Wonder Woman", "Aquaman", "Shazam!",
        "The Conjuring", "Annabelle", "IT", "Insidious", "Get Out",
        "Us", "Parasite", "Oppenheimer", "Barbie", "Tenet",
        "Dune", "The Prestige", "Now You See Me", "The Hunger Games", "Divergent",
        "The Maze Runner", "John Wick", "Mad Max: Fury Road", "Gladiator", "Braveheart"
    ],
    "Genre": [
        "Sci-Fi", "Action", "Sci-Fi", "Action", "Sci-Fi",
        "Romance", "Sci-Fi", "Thriller", "Drama", "Drama",
        "Crime", "Crime", "Thriller", "Animation", "Animation",
        "Animation", "Animation", "Animation", "Animation", "Animation",
        "Action", "Action", "Action", "Action", "Action",
        "Action", "Action", "Action", "Action", "Action",
        "Action", "Action", "Action", "Action", "Action",
        "Horror", "Horror", "Horror", "Horror", "Horror",
        "Thriller", "Thriller", "Biography", "Comedy", "Sci-Fi",
        "Sci-Fi", "Mystery", "Mystery", "Adventure", "Adventure",
        "Adventure", "Action", "Action", "Action", "Action"
    ],
    "Rating": [
        8.8, 9.0, 8.6, 8.4, 8.7,
        7.8, 7.9, 8.4, 9.3, 8.8,
        9.2, 8.9, 8.8, 8.5, 7.5,
        8.3, 8.2, 8.1, 8.4, 8.1,
        8.3, 7.5, 7.9, 8.0, 8.5,
        8.0, 7.3, 6.9, 6.5, 6.2,
        8.2, 7.1, 7.4, 7.0, 7.1,
        7.5, 6.7, 7.3, 6.8, 7.7,
        7.0, 8.6, 8.4, 7.1, 7.3,
        8.2, 8.5, 7.3, 7.2, 7.0,
        7.1, 8.0, 8.1, 8.5, 8.3
    ],
    "Poster": [
        "https://m.media-amazon.com/images/I/51oD2VviQwL._AC_.jpg",
        "https://m.media-amazon.com/images/I/51k0qa6qF9L._AC_.jpg",
        "https://m.media-amazon.com/images/I/71y7iBVD5KL._AC_SL1500_.jpg",
        "https://m.media-amazon.com/images/I/71niXI3lxlL._AC_SL1500_.jpg",
        "https://m.media-amazon.com/images/I/51EG732BV3L._AC_.jpg",
        "https://m.media-amazon.com/images/I/71lWzE4XrBL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81D+KJkO3aL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81xQBb5jRzL._AC_SL1500_.jpg",
        "https://m.media-amazon.com/images/I/51NiGlapXlL._AC_.jpg",
        "https://m.media-amazon.com/images/I/61KcQ4A+g4L._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/41+eK8zBwQL._AC_.jpg",
        "https://m.media-amazon.com/images/I/71c05lTE03L._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/71A7+9vD7KL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81H7K0a3n+L._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/61qCTrf6UBL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81Wb+z4I7fL._AC_SL1500_.jpg",
        "https://m.media-amazon.com/images/I/61+uX7yUDkL._AC_SL1024_.jpg",
        "https://m.media-amazon.com/images/I/71tFihl1XNL._AC_SL1024_.jpg",
        "https://m.media-amazon.com/images/I/81Y5WuARqpL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/91e0lTzFjBL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81x+oFJc6PL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/71niXI3lxlL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/71eA1c5kNdL._AC_SL1000_.jpg",
        "https://m.media-amazon.com/images/I/81N+8KX8HhL._AC_SL1500_.jpg",
        "https://m.media-amazon.com/images/I/81K8iGz2exL._AC_SL1500_.jpg",
        "https://m.media-amazon.com/images/I/81AIqVkhxLL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/71W8vV+4g9L._AC_SL1500_.jpg",
        "https://m.media-amazon.com/images/I/81xOclTDyRL._AC_SL1500_.jpg",
        "https://m.media-amazon.com/images/I/81Zt42ioCgL._AC_SL1500_.jpg",
        "https://m.media-amazon.com/images/I/71QGvsjIgeL._AC_SL1000_.jpg",
        "https://m.media-amazon.com/images/I/61OUGpUfAyL._AC_SL1024_.jpg",
        "https://m.media-amazon.com/images/I/61zqjC2+4+L._AC_SL1000_.jpg",
        "https://m.media-amazon.com/images/I/81Y0V8d5fBL._AC_SL1500_.jpg",
        "https://m.media-amazon.com/images/I/71KqKk5bNHL._AC_SL1500_.jpg",
        "https://m.media-amazon.com/images/I/81ykcN8kKoL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/71Qf+vCvB9L._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81xYcx6CL6L._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/91Z7FJX1IrL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81vZVqybmuL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/91gDY0n1+dL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81D4Q1UiyCL._AC_SL1500_.jpg",
        "https://m.media-amazon.com/images/I/81V+oFzceLL._AC_SL1500_.jpg",
        "https://m.media-amazon.com/images/I/71FSzIGeMAL._AC_SL1500_.jpg",
        "https://m.media-amazon.com/images/I/81hs6z+9LHL._AC_SL1500_.jpg",
        "https://m.media-amazon.com/images/I/71UwDrT9yJL._AC_SL1500_.jpg",
        "https://m.media-amazon.com/images/I/71i4Zs4LV+L._AC_SL1500_.jpg",
        "https://m.media-amazon.com/images/I/81sLRtYPhUL._AC_SL1500_.jpg",
        "https://m.media-amazon.com/images/I/91FhZp9hKxL._AC_SL1500_.jpg",
        "https://m.media-amazon.com/images/I/81tpPl0KUIL._AC_SL1500_.jpg",
        "https://m.media-amazon.com/images/I/81rUuL8dr-L._AC_SL1500_.jpg",
        "https://m.media-amazon.com/images/I/71YqMnjwOrL._AC_SL1500_.jpg",
        "https://m.media-amazon.com/images/I/81s1Du3zuzL._AC_SL1500_.jpg",
        "https://m.media-amazon.com/images/I/71d5M6U8qOL._AC_SL1500_.jpg",
        "https://m.media-amazon.com/images/I/91BV8tXrSGL._AC_SL1500_.jpg"
    ]
})

# ===================== UI =====================
st.title("🍿 Movie Recommendation System")
st.markdown("### Find movies by your favorite genre 🎬")

genre = st.selectbox("Select Genre", sorted(movies["Genre"].unique()))

filtered_movies = movies[movies["Genre"] == genre].reset_index(drop=True)

st.markdown(f"### Showing {len(filtered_movies)} movies in **{genre}** genre")

cols = st.columns(4)
for i, row in filtered_movies.iterrows():
    with cols[i % 4]:
        st.markdown(f"""
            <div class="movie-card">
                <img src="{row['Poster']}" width="180">
                <h4>{row['Title']}</h4>
                <p>⭐ Rating: {row['Rating']}</p>
            </div>
        """, unsafe_allow_html=True)
