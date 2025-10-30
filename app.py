import streamlit as st
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(page_title="🎬 Movie Recommender", page_icon="🍿", layout="centered")

# -----------------------------
# Styling
# -----------------------------
st.markdown("""
    <style>
    body { background: linear-gradient(135deg, #0f1724, #243b55); color: #eef2ff; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .title { font-size: 40px; font-weight: 800; text-align: center; color: #FFD166; margin-bottom: 10px; }
    .subtitle { text-align:center; color:#cfe8ff; margin-bottom:30px; }
    .movie-card { display:flex; gap:16px; align-items:center; background: rgba(255,255,255,0.04); padding:14px; border-radius:12px; margin-bottom:14px; box-shadow: 0 6px 18px rgba(2,6,23,0.6); }
    .movie-title { font-size:20px; font-weight:700; color:#9be7ff; margin-bottom:6px; }
    .movie-meta { color:#ffd899; font-weight:600; }
    img.poster { border-radius:8px; box-shadow: 0 6px 18px rgba(0,0,0,0.6); }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Dataset (50 movies) - all lists same length
# -----------------------------
titles = [
"Inception","Titanic","Avengers: Endgame","The Dark Knight","La La Land",
"The Conjuring","Interstellar","Frozen","Parasite","Dune",
"Gladiator","Avatar","The Notebook","Joker","Toy Story",
"Finding Nemo","Doctor Strange","Black Panther","Up","Inside Out",
"Shutter Island","Us","The Matrix","Coco","The Lion King",
"Pulp Fiction","Fight Club","Forrest Gump","The Shawshank Redemption","The Godfather",
"Avengers: Infinity War","Spider-Man: No Way Home","The Batman","Guardians of the Galaxy","Iron Man",
"Thor: Ragnarok","Captain America: Civil War","Ant-Man","WALL-E","Moana",
"Zootopia","Encanto","Cinderella","Mulan","Beauty and the Beast",
"The Nun","Annabelle","Hereditary","IT","Get Out"
]

genres = [
"Sci-Fi","Romance","Action","Action","Romance",
"Horror","Sci-Fi","Animation","Thriller","Sci-Fi",
"Action","Sci-Fi","Romance","Drama","Animation",
"Animation","Action","Action","Animation","Animation",
"Thriller","Horror","Sci-Fi","Animation","Animation",
"Crime","Drama","Drama","Drama","Crime",
"Action","Action","Action","Action","Action",
"Action","Action","Action","Animation","Animation",
"Animation","Animation","Animation","Animation","Animation",
"Horror","Horror","Horror","Horror","Thriller"
]

ratings = [
8.8,7.8,8.4,9.0,8.0,
7.5,8.6,7.4,8.6,8.3,
8.5,7.8,7.9,8.5,8.3,
8.2,7.5,7.3,8.2,8.1,
8.1,6.9,8.7,8.4,8.5,
8.9,8.8,8.8,9.3,9.2,
8.4,8.3,8.1,8.0,7.9,
7.8,7.6,7.5,8.4,8.1,
8.0,7.9,7.5,7.4,7.3,
6.8,7.2,7.3,8.0,7.7
]

posters = [
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
"https://m.media-amazon.com/images/I/81Y6rrnOkpL._AC_SY679_.jpg",
"https://m.media-amazon.com/images/I/71y5xF3Q2VL._AC_SY679_.jpg",
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
"https://m.media-amazon.com/images/I/81k0w4w2BML._AC_SY679_.jpg"
]

# build dataframe (all lists same length)
movies = pd.DataFrame({"Title": titles, "Genre": genres, "Rating": ratings, "Poster": posters})

# -----------------------------
# App UI
# -----------------------------
st.markdown("<div class='title'>🎥 Movie Recommender System 🍿</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Pick a genre below — results are sorted by rating.</div>", unsafe_allow_html=True)

# Controls: genre selection
selected_genre = st.selectbox("Select Genre", options=sorted(movies["Genre"].unique()))

# Filter & sort
filtered = movies[movies["Genre"] == selected_genre].sort_values(by="Rating", ascending=False)

# Show count and top results
st.markdown(f"**Showing {len(filtered)} {selected_genre} movies (sorted by rating):**")

# Display each movie as a card
for _, row in filtered.iterrows():
    st.markdown(f"""
    <div class="movie-card">
        <img class="poster" src="{row.Poster}" width="110" />
        <div>
            <div class="movie-title">{row.Title}</div>
            <div style="margin-top:6px;">
                <span class="movie-meta">⭐ {row.Rating} &nbsp;|&nbsp; 🎭 {row.Genre}</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
