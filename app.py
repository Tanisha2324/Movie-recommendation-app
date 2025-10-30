import streamlit as st
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="🎬 Movie Recommender",
    page_icon="🍿",
    layout="centered"
)

# -----------------------------
# Custom CSS Styling
# -----------------------------
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #1f1c2c, #928dab);
        color: white;
        font-family: 'Poppins', sans-serif;
    }
    .title {
        font-size: 46px;
        font-weight: 800;
        text-align: center;
        color: #FFD700;
        text-shadow: 2px 2px 10px #00000055;
    }
    .movie-card {
        background-color: rgba(255, 255, 255, 0.12);
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.25);
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
# Movie Dataset (50+ entries)
# -----------------------------
movies = pd.DataFrame({
    "Title": [
        "Inception", "Titanic", "Avengers: Endgame", "The Dark Knight", "La La Land",
        "The Conjuring", "Interstellar", "Frozen", "Parasite", "Dune", "Gladiator",
        "Avatar", "The Notebook", "Joker", "Toy Story", "Finding Nemo", "Doctor Strange",
        "Black Panther", "Up", "Inside Out", "Shutter Island", "Us", "The Matrix",
        "Coco", "The Lion King", "Pulp Fiction", "Fight Club", "Forrest Gump",
        "The Shawshank Redemption", "The Godfather", "Avengers: Infinity War",
        "Spider-Man: No Way Home", "The Batman", "Guardians of the Galaxy", "Iron Man",
        "Thor: Ragnarok", "Captain America: Civil War", "Ant-Man", "WALL-E",
        "Moana", "Zootopia", "Encanto", "Cinderella", "Mulan", "Beauty and the Beast",
        "The Nun", "Annabelle", "Hereditary", "IT", "The Exorcist", "Get Out", "Nope",
        "The Silence of the Lambs", "Seven", "Gone Girl", "Knives Out", "Tenet"
    ],
    "Genre": [
        "Sci-Fi", "Romance", "Action", "Action", "Romance", "Horror", "Sci-Fi", "Animation",
        "Thriller", "Sci-Fi", "Action", "Sci-Fi", "Romance", "Drama", "Animation",
        "Animation", "Action", "Action", "Animation", "Animation", "Thriller", "Horror",
        "Sci-Fi", "Animation", "Animation", "Crime", "Drama", "Drama", "Drama", "Crime",
        "Action", "Action", "Action", "Action", "Action", "Action", "Action", "Action",
        "Animation", "Animation", "Animation", "Animation", "Animation", "Animation",
        "Horror", "Horror", "Horror", "Horror", "Horror", "Horror", "Horror",
        "Thriller", "Thriller", "Thriller", "Mystery", "Sci-Fi"
    ],
    "Rating": [
        8.8, 7.8, 8.4, 9.0, 8.0, 7.5, 8.6, 7.4, 8.6, 8.3, 8.5, 7.8, 7.9, 8.5,
        8.3, 8.2, 7.5, 7.3, 8.2, 8.1, 8.1, 6.9, 8.7, 8.4, 8.5, 8.9, 8.8, 8.8,
        9.3, 9.2, 8.4, 8.3, 8.1, 8.0, 7.9, 7.8, 7.6, 7.5, 8.4, 8.1, 8.0, 7.9,
        7.5, 7.4, 7.3, 6.8, 7.2, 7.3, 8.0, 8.1, 7.0, 7.8, 8.6, 8.4, 8.1, 7.9, 7.5
    ],
    "Poster": [
        "https://m.media-amazon.com/images/I/51v5ZpFyaFL._AC_.jpg",
        "https://m.media-amazon.com/images/I/71yAz0M0Q0L._AC_UF894,1000_QL80_.jpg",
        "https://m.media-amazon.com/images/I/81ExhpBEbHL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/71pox3sbRPL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/71eGx3bMT0L._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/71WXIoa0aeL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/91kFYg4fX3L._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/71Jxq3pJffL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/91TqDgq+EGL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/91m9r3gP0zL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/51A3T9WgSGL._AC_.jpg",
        "https://m.media-amazon.com/images/I/71c05lTE03L._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/71oZ5k7tH5L._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81RrwyY8SOL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/71aSmVZ9NBL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81A5ZFBPTcL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/71YjU5+9jSL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/71niXI3lxlL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/71cN8B5ZgSL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81BES+ts5-L._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81dZ4z8cvUL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/71y5xF3Q2VL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/71d7rfw8v9L._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81Z9B6lRtHL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/71R9pZGxdtL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81aA7hEEykL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/71K9Lb2l+PL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/71xBLRBYOiL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/91KkWf50SoL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/51EG732BV3L._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81AYq8X6g8L._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/91j0vB3kFzL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/91IUF+O+xvL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/91ZJtSVwkCL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81Y6rrnOkpL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81tH4zNfPUL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81J0XfC4v7L._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81Z2WJ6bqgL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81Z5Jf6Tj+L._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81U8Qk6YpFL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81bxpXAFibL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/91Kc7lAqvOL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81y3YV4bSnL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81OZLgRvtGL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81WqdcQ2kZL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81RYkZzF5mL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81bVZhjtrbL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81jvXbnqPGL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/91qvVdK85dL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81F5bfgkU8L._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/71rNJQ2g-EL._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81xTx-L7i+L._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81s3F8Z4HML._AC_SY679_.jpg",
        "https://m.media-amazon.com/images/I/81hZQYlf3OL._AC_SY679_.jpg"
    ]
})

# -----------------------------
# App Interface
# -----------------------------
st.markdown("<div class='title'>🎥 Movie Recommender System 🍿</div>", unsafe_allow_html=True)
st.write("### 💡 Choose a Genre to Discover New Movies:")

# Dropdown
selected_genre = st.selectbox("Select Genre", sorted(movies["Genre"].unique()))

# Filter + Sort
filtered_movies = movies[movies["Genre"] == selected_genre].sort_values(by="Rating", ascending=False)

# Display results
st.write(f"### 🎞️ Top {selected_genre} Movies:")
for _, row in filtered_movies.iterrows():
    with st.container():
        st.markdown(f"""
        <div class="movie-card">
            <img src="{row.Poster}" width="180">
            <div class="movie-title">{row.Title}</div>
            <div>⭐ <span class="movie-rating">{row.Rating}</span> | 🎭 {row.Genre}</div>
        </div>
        """, unsafe_allow_html=True)
