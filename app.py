# app.py
import streamlit as st
import pandas as pd

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="🎬 Movie Recommender", page_icon="🍿", layout="wide")

# ------------------ STYLES (BLACK BACKGROUND) ------------------
st.markdown(
    """
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    .title { text-align:center; color:#FFD166; font-size:34px; font-weight:700; margin-bottom:6px; }
    .subtitle { text-align:center; color:#bfbfbf; margin-bottom:20px; }
    .card { background: #111111; padding:10px; border-radius:10px; text-align:center; }
    .meta { color:#FFD166; font-weight:600; margin-top:6px; }
    img.poster { border-radius:8px; box-shadow: 0 6px 18px rgba(0,0,0,0.6); }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------ MOVIE DATA (list of dicts, safe) ------------------
# NOTE: For many movies we use a placeholder poster to guarantee images always show.
PLACEHOLDER = "https://via.placeholder.com/300x450.png?text=No+Image"

movie_dicts = [
    # Popular titles with TMDb poster (reliable)
    {"Title":"Inception","Genre":"Sci-Fi","Rating":8.8,"Poster":"https://image.tmdb.org/t/p/w500/qmDpIHrmpJINaRKAfWQfftjCdyi.jpg"},
    {"Title":"The Dark Knight","Genre":"Action","Rating":9.0,"Poster":"https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg"},
    {"Title":"Interstellar","Genre":"Sci-Fi","Rating":8.6,"Poster":"https://image.tmdb.org/t/p/w500/nBNZadXqJSdt05SHLqgT0HuC5Gm.jpg"},
    {"Title":"Avengers: Endgame","Genre":"Action","Rating":8.4,"Poster":"https://image.tmdb.org/t/p/w500/or06FN3Dka5tukK1e9sl16pB3iy.jpg"},
    {"Title":"The Matrix","Genre":"Sci-Fi","Rating":8.7,"Poster":"https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg"},
    {"Title":"Titanic","Genre":"Romance","Rating":7.8,"Poster":"https://image.tmdb.org/t/p/w500/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg"},
    {"Title":"Avatar","Genre":"Sci-Fi","Rating":7.8,"Poster":"https://image.tmdb.org/t/p/w500/6EiRUJpuoeQPghrs3YNktfnqOVh.jpg"},
    {"Title":"Joker","Genre":"Drama","Rating":8.5,"Poster":"https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg"},
    {"Title":"The Shawshank Redemption","Genre":"Drama","Rating":9.3,"Poster":"https://image.tmdb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg"},
    {"Title":"Forrest Gump","Genre":"Drama","Rating":8.8,"Poster":"https://image.tmdb.org/t/p/w500/saHP97rTPS5eLmrLQEcANmKrsFl.jpg"},
    {"Title":"The Godfather","Genre":"Crime","Rating":9.2,"Poster":"https://image.tmdb.org/t/p/w500/rPdtLWNsZmAtoZl9PK7S2wE3qiS.jpg"},
    {"Title":"Pulp Fiction","Genre":"Crime","Rating":8.9,"Poster":"https://i.pinimg.com/originals/b3/4d/d7/b34dd71e2389ed3a37af5d7b7e9fedb2.jpg"},
    {"Title":"Parasite","Genre":"Thriller","Rating":8.6,"Poster":"https://image.tmdb.org/t/p/w500/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg"},
    {"Title":"Dune","Genre":"Sci-Fi","Rating":8.3,"Poster":"https://image.tmdb.org/t/p/w500/d5NXSklXo0qyIYkgV94XAgMIckC.jpg"},
    {"Title":"Gladiator","Genre":"Action","Rating":8.5,"Poster":"https://image.tmdb.org/t/p/w500/ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg"},

    # The rest: we include many titles but use placeholder posters to avoid any broken-link issues
    {"Title":"Toy Story","Genre":"Animation","Rating":8.3,"Poster":PLACEHOLDER},
    {"Title":"Finding Nemo","Genre":"Animation","Rating":8.1,"Poster":PLACEHOLDER},
    {"Title":"Coco","Genre":"Animation","Rating":8.4,"Poster":PLACEHOLDER},
    {"Title":"Frozen","Genre":"Animation","Rating":7.4,"Poster":PLACEHOLDER},
    {"Title":"Inside Out","Genre":"Animation","Rating":8.1,"Poster":PLACEHOLDER},
    {"Title":"Up","Genre":"Animation","Rating":8.2,"Poster":PLACEHOLDER},
    {"Title":"The Lion King","Genre":"Animation","Rating":8.5,"Poster":PLACEHOLDER},
    {"Title":"The Notebook","Genre":"Romance","Rating":7.9,"Poster":PLACEHOLDER},
    {"Title":"La La Land","Genre":"Romance","Rating":8.0,"Poster":PLACEHOLDER},
    {"Title":"Fight Club","Genre":"Drama","Rating":8.8,"Poster":PLACEHOLDER},
    {"Title":"The Prestige","Genre":"Drama","Rating":8.5,"Poster":PLACEHOLDER},
    {"Title":"Memento","Genre":"Thriller","Rating":8.4,"Poster":PLACEHOLDER},
    {"Title":"Whiplash","Genre":"Drama","Rating":8.5,"Poster":PLACEHOLDER},
    {"Title":"The Social Network","Genre":"Drama","Rating":7.7,"Poster":PLACEHOLDER},
    {"Title":"The Silence of the Lambs","Genre":"Thriller","Rating":8.6,"Poster":PLACEHOLDER},
    {"Title":"Se7en","Genre":"Thriller","Rating":8.6,"Poster":PLACEHOLDER},
    {"Title":"Gone Girl","Genre":"Thriller","Rating":8.1,"Poster":PLACEHOLDER},
    {"Title":"Knives Out","Genre":"Mystery","Rating":7.9,"Poster":PLACEHOLDER},
    {"Title":"Tenet","Genre":"Sci-Fi","Rating":7.5,"Poster":PLACEHOLDER},
    {"Title":"The Conjuring","Genre":"Horror","Rating":7.5,"Poster":PLACEHOLDER},
    {"Title":"Annabelle","Genre":"Horror","Rating":5.4,"Poster":PLACEHOLDER},
    {"Title":"Hereditary","Genre":"Horror","Rating":7.3,"Poster":PLACEHOLDER},
    {"Title":"IT","Genre":"Horror","Rating":7.4,"Poster":PLACEHOLDER},
    {"Title":"Get Out","Genre":"Horror","Rating":7.7,"Poster":PLACEHOLDER},
    {"Title":"Nope","Genre":"Horror","Rating":6.8,"Poster":PLACEHOLDER},
    {"Title":"Us","Genre":"Horror","Rating":6.8,"Poster":PLACEHOLDER},
    {"Title":"John Wick","Genre":"Action","Rating":7.4,"Poster":PLACEHOLDER},
    {"Title":"Mad Max: Fury Road","Genre":"Action","Rating":8.1,"Poster":PLACEHOLDER},
    {"Title":"The Hunger Games","Genre":"Adventure","Rating":7.2,"Poster":PLACEHOLDER},
    {"Title":"Divergent","Genre":"Adventure","Rating":6.4,"Poster":PLACEHOLDER},
    {"Title":"The Maze Runner","Genre":"Adventure","Rating":6.8,"Poster":PLACEHOLDER},
    {"Title":"The Flash","Genre":"Action","Rating":5.7,"Poster":PLACEHOLDER},
    {"Title":"Black Panther","Genre":"Action","Rating":7.3,"Poster":PLACEHOLDER},
    {"Title":"Guardians of the Galaxy","Genre":"Action","Rating":8.0,"Poster":PLACEHOLDER},
    {"Title":"Iron Man","Genre":"Action","Rating":7.9,"Poster":PLACEHOLDER},
    {"Title":"Thor: Ragnarok","Genre":"Action","Rating":7.9,"Poster":PLACEHOLDER},
    {"Title":"Captain America: Civil War","Genre":"Action","Rating":7.8,"Poster":PLACEHOLDER},
    {"Title":"Ant-Man","Genre":"Action","Rating":7.3,"Poster":PLACEHOLDER},
    {"Title":"WALL-E","Genre":"Animation","Rating":8.4,"Poster":PLACEHOLDER},
    {"Title":"Moana","Genre":"Animation","Rating":7.6,"Poster":PLACEHOLDER},
    {"Title":"Zootopia","Genre":"Animation","Rating":8.0,"Poster":PLACEHOLDER},
    {"Title":"Encanto","Genre":"Animation","Rating":7.3,"Poster":PLACEHOLDER},
    {"Title":"Braveheart","Genre":"Action","Rating":8.3,"Poster":PLACEHOLDER}
]

# Convert to DataFrame (safe — list length consistent by construction)
movies = pd.DataFrame(movie_dicts)

# ------------------ INTERFACE ------------------
st.markdown('<div class="title">🎥 Movie Recommender System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Black theme, images guaranteed (placeholder used if no poster).</div>', unsafe_allow_html=True)

# Search + genre filter
col1, col2 = st.columns([3,1])
with col1:
    query = st.text_input("🔎 Search movie title (leave empty to show by genre)", value="").strip()
with col2:
    genre_choice = st.selectbox("🎭 Filter by genre", options=["All"] + sorted(movies["Genre"].unique()))

# Filter data
df = movies.copy()
if genre_choice != "All":
    df = df[df["Genre"] == genre_choice]
if query:
    df = df[df["Title"].str.contains(query, case=False, na=False)]

# Sort by rating desc
df = df.sort_values(by="Rating", ascending=False).reset_index(drop=True)

st.markdown(f"**Showing {len(df)} results**")

# Display in responsive grid (4 columns)
cols = st.columns(4)
for idx, row in df.iterrows():
    c = cols[idx % 4]
    with c:
        poster_url = row["Poster"] if row["Poster"] else PLACEHOLDER
        # use image element + fallback alt text
        st.image(poster_url, width=180)
        st.markdown(f"**{row['Title']}**")
        st.markdown(f"<div class='meta'>⭐ {row['Rating']} &nbsp;|&nbsp; {row['Genre']}</div>", unsafe_allow_html=True)
