import streamlit as st
import pandas as pd
import urllib.parse
import requests
from typing import Optional
USER_AGENT_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}

def build_placeholder(title: str, secondary: bool = False) -> str:
    text = urllib.parse.quote_plus(title)
    if secondary:
        return f"https://placehold.co/300x450?text={text}"
    return f"https://via.placeholder.com/300x450.png?text={text}"

@st.cache_data(ttl=1800)
def is_url_ok(url: str) -> bool:
    try:
        resp = requests.head(url, allow_redirects=True, timeout=6, headers=USER_AGENT_HEADERS)
        if 200 <= resp.status_code < 300:
            return True
        # Some CDNs don't support HEAD properly; try GET as fallback
        resp = requests.get(url, stream=True, allow_redirects=True, timeout=8, headers=USER_AGENT_HEADERS)
        return 200 <= resp.status_code < 300
    except Exception:
        return False

@st.cache_data(ttl=900)
def can_reach_hosts() -> dict:
    hosts = {
        "tmdb": "https://image.tmdb.org/t/p/w92/9gk7adHYeDvHkCSEqAvQNLV5Uge.jpg",
        "placeholder_primary": "https://via.placeholder.com/1x1.png",
        "placeholder_secondary": "https://placehold.co/1x1.png",
    }
    results = {}
    for key, url in hosts.items():
        results[key] = is_url_ok(url)
    return results

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
    {"Title":"Inception","Genre":"Sci-Fi","Rating":8.8,"Poster":"https://image.tmdb.org/t/p/w500/9gk7adHYeDvHkCSEqAvQNLV5Uge.jpg"},
    {"Title":"The Dark Knight","Genre":"Action","Rating":9.0,"Poster":"https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg"},
    {"Title":"Interstellar","Genre":"Sci-Fi","Rating":8.6,"Poster":"https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg"},
    {"Title":"Avengers: Endgame","Genre":"Action","Rating":8.4,"Poster":"https://image.tmdb.org/t/p/w500/or06FN3Dka5tukK1e9sl16pB3iy.jpg"},
    {"Title":"The Matrix","Genre":"Sci-Fi","Rating":8.7,"Poster":"https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg"},
    {"Title":"Titanic","Genre":"Romance","Rating":7.8,"Poster":"https://image.tmdb.org/t/p/w500/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg"},
    {"Title":"Avatar","Genre":"Sci-Fi","Rating":7.8,"Poster":"https://image.tmdb.org/t/p/w500/6EiRUJpuoeQPghrs3YNktfnqOVh.jpg"},
    {"Title":"Joker","Genre":"Drama","Rating":8.5,"Poster":"https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg"},
    {"Title":"The Shawshank Redemption","Genre":"Drama","Rating":9.3,"Poster":"https://image.tmdb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg"},
    {"Title":"Forrest Gump","Genre":"Drama","Rating":8.8,"Poster":"https://image.tmdb.org/t/p/w500/saHP97rTPS5eLmrLQEcANmKrsFl.jpg"},
    {"Title":"The Godfather","Genre":"Crime","Rating":9.2,"Poster":"https://image.tmdb.org/t/p/w500/rPdtLWNsZmAtoZl9PK7S2wE3qiS.jpg"},
    {"Title":"Pulp Fiction","Genre":"Crime","Rating":8.9,"Poster":"https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg"},
    {"Title":"Parasite","Genre":"Thriller","Rating":8.6,"Poster":"https://image.tmdb.org/t/p/w500/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg"},
    {"Title":"Dune","Genre":"Sci-Fi","Rating":8.3,"Poster":"https://image.tmdb.org/t/p/w500/d5NXSklXo0qyIYkgV94XAgMIckC.jpg"},
    {"Title":"Gladiator","Genre":"Action","Rating":8.5,"Poster":"https://image.tmdb.org/t/p/w500/ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg"},

    # The rest: we include many titles but use placeholder posters to avoid any broken-link issues
    {"Title":"Toy Story","Genre":"Animation","Rating":8.3,"Poster":"https://image.tmdb.org/t/p/w500/uXDfjJbdP4ijW5hWSBrPrlKpxab.jpg"},
    {"Title":"Finding Nemo","Genre":"Animation","Rating":8.1,"Poster":"https://image.tmdb.org/t/p/w500/eHuGQ10FUzK1mdOY69wF5pGgEf5.jpg"},
    {"Title":"Coco","Genre":"Animation","Rating":8.4,"Poster":"https://image.tmdb.org/t/p/w500/gGEsBPAijhVUFoiNpgZXqRVWJt2.jpg"},
    {"Title":"Frozen","Genre":"Animation","Rating":7.4,"Poster":"https://image.tmdb.org/t/p/w500/kgwjIb2JDHRhNk13lmSxiClFjVk.jpg"},
    {"Title":"Inside Out","Genre":"Animation","Rating":8.1,"Poster":"https://image.tmdb.org/t/p/w500/2H1TmgdfNtsKlU9jKdeNyYL5y8T.jpg"},
    {"Title":"Up","Genre":"Animation","Rating":8.2,"Poster":"https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg"},
    {"Title":"The Lion King","Genre":"Animation","Rating":8.5,"Poster":"https://image.tmdb.org/t/p/w500/sKCr78MXSLixwmZ8DyJLrpMsd15.jpg"},
    {"Title":"The Notebook","Genre":"Romance","Rating":7.9,"Poster":"https://upload.wikimedia.org/wikipedia/en/8/86/The_Notebook_poster.jpg"},
    {"Title":"La La Land","Genre":"Romance","Rating":8.0,"Poster":"https://image.tmdb.org/t/p/w500/uDO8zWDhfWwoFdKS4fzkUJt0Rf0.jpg"},
    {"Title":"Fight Club","Genre":"Drama","Rating":8.8,"Poster":"https://image.tmdb.org/t/p/w500/a26cQPRhJPX6GbWfQbvZdrrp9j9.jpg"},
    {"Title":"The Prestige","Genre":"Drama","Rating":8.5,"Poster":"https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg"},
    {"Title":"Memento","Genre":"Thriller","Rating":8.4,"Poster":"https://upload.wikimedia.org/wikipedia/en/c/c7/Memento_poster.jpg"},
    {"Title":"Whiplash","Genre":"Drama","Rating":8.5,"Poster":"https://upload.wikimedia.org/wikipedia/en/0/01/Whiplash_poster.jpg"},
    {"Title":"The Social Network","Genre":"Drama","Rating":7.7,"Poster":"https://image.tmdb.org/t/p/w500/n0ybibhJtQ5icDqTp8eRytcIHJx.jpg"},
    {"Title":"The Silence of the Lambs","Genre":"Thriller","Rating":8.6,"Poster":"https://image.tmdb.org/t/p/w500/rplLJ2hPcOQmkFhTqUte0MkEaO2.jpg"},
    {"Title":"Se7en","Genre":"Thriller","Rating":8.6,"Poster":"https://image.tmdb.org/t/p/w500/69Sns8WoET6CfaYlIkHbla4l7nC.jpg"},
    {"Title":"Gone Girl","Genre":"Thriller","Rating":8.1,"Poster":"https://upload.wikimedia.org/wikipedia/en/0/05/Gone_Girl_Poster.jpg"},
    {"Title":"Knives Out","Genre":"Mystery","Rating":7.9,"Poster":"https://image.tmdb.org/t/p/w500/pThyQovXQrw2m0s9x82twj48Jq4.jpg"},
    {"Title":"Tenet","Genre":"Sci-Fi","Rating":7.5,"Poster":"https://image.tmdb.org/t/p/w500/k68nPLbIST6NP96JmTxmZijEvCA.jpg"},
    {"Title":"The Conjuring","Genre":"Horror","Rating":7.5,"Poster":"https://image.tmdb.org/t/p/w500/wVYREutTvI2tmxr6ujrHT704wGF.jpg"},
    {"Title":"Annabelle","Genre":"Horror","Rating":5.4,"Poster":"https://m.media-amazon.com/images/S/pv-target-images/0e64bca6c68220f986a8e665a2d8f5f8ff60d6b7aed36c033a08cc6798a548c3.jpg"},
    {"Title":"Hereditary","Genre":"Horror","Rating":7.3,"Poster":"https://image.tmdb.org/t/p/w500/lHV8HHlhwNup2VbpiACtlKzaGIQ.jpg"},
    {"Title":"IT","Genre":"Horror","Rating":7.4,"Poster":"https://image.tmdb.org/t/p/w500/9E2y5Q7WlCVNEhP5GiVTjhEhx1o.jpg"},
    {"Title":"Get Out","Genre":"Horror","Rating":7.7,"Poster":"https://upload.wikimedia.org/wikipedia/en/a/a3/Get_Out_poster.png"},
    {"Title":"Nope","Genre":"Horror","Rating":6.8,"Poster":"https://image.tmdb.org/t/p/w500/AcKVlWaNVVVFQwro3nLXqPljcYA.jpg"},
    {"Title":"Us","Genre":"Horror","Rating":6.8,"Poster":"https://image.tmdb.org/t/p/w500/ux2dU1jQ2ACIMShzB3yP93Udpzc.jpg"},
    {"Title":"John Wick","Genre":"Action","Rating":7.4,"Poster":"https://image.tmdb.org/t/p/w500/b9uYMMbm87IBFOq59pppvkkkgNg.jpg"},
    {"Title":"Mad Max: Fury Road","Genre":"Action","Rating":8.1,"Poster":"https://image.tmdb.org/t/p/w500/8tZYtuWezp8JbcsvHYO0O46tFbo.jpg"},
    {"Title":"The Hunger Games","Genre":"Adventure","Rating":7.2,"Poster":"https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg"},
    {"Title":"Divergent","Genre":"Adventure","Rating":6.4,"Poster":"https://tse2.mm.bing.net/th/id/OIP.wFzVhHzcMoHF3JMENk6HngHaLk?pid=Api&P=0&h=180"},
    {"Title":"The Maze Runner","Genre":"Adventure","Rating":6.8,"Poster":"https://image.tmdb.org/t/p/w500/ode14q7WtDugFDp78fo9lCsmay9.jpg"},
    {"Title":"The Flash","Genre":"Action","Rating":5.7,"Poster":"https://image.tmdb.org/t/p/w500/rktDFPbfHfUbArZ6OOOKsXcv0Bm.jpg"},
    {"Title":"Black Panther","Genre":"Action","Rating":7.3,"Poster":"https://image.tmdb.org/t/p/w500/uxzzxijgPIY7slzFvMotPv8wjKA.jpg"},
    {"Title":"Guardians of the Galaxy","Genre":"Action","Rating":8.0,"Poster":"https://image.tmdb.org/t/p/w500/r7vmZjiyZw9rpJMQJdXpjgiCOk9.jpg"},
    {"Title":"Iron Man","Genre":"Action","Rating":7.9,"Poster":"https://image.tmdb.org/t/p/w500/78lPtwv72eTNqFW9COBYI0dWDJa.jpg"},
    {"Title":"Thor: Ragnarok","Genre":"Action","Rating":7.9,"Poster":"https://image.tmdb.org/t/p/w500/rzRwTcFvttcN1ZpX2xv4j3tSdJu.jpg"},
    {"Title":"Captain America: Civil War","Genre":"Action","Rating":7.8,"Poster":"https://image.tmdb.org/t/p/w500/rAGiXaUfPzY7CDEyNKUofk3Kw2e.jpg"},
    {"Title":"Ant-Man","Genre":"Action","Rating":7.3,"Poster":"https://image.tmdb.org/t/p/w500/rS97hUJ1otKTTripGwQ0ujbuIri.jpg"},
    {"Title":"WALL-E","Genre":"Animation","Rating":8.4,"Poster":"https://image.tmdb.org/t/p/w500/hbhFnRzzg6ZDmm8YAmxBnQpQIPh.jpg"},
    {"Title":"Moana","Genre":"Animation","Rating":7.6,"Poster":"https://upload.wikimedia.org/wikipedia/en/2/26/Moana_Teaser_Poster.jpg"},
    {"Title":"Zootopia","Genre":"Animation","Rating":8.0,"Poster":"https://cinemasentries.com/wp-content/uploads/2023/05/Zootopia-Blu-ray.jpg"},
    {"Title":"Encanto","Genre":"Animation","Rating":7.3,"Poster":"https://image.tmdb.org/t/p/w500/4j0PNHkMr5ax3IA8tjtxcmPU3QT.jpg"},
    {"Title":"Braveheart","Genre":"Action","Rating":8.3,"Poster":"https://image.tmdb.org/t/p/w500/or1gBugydmjToAEq7OZY0owwFk.jpg"}
]

# Convert to DataFrame (safe — list length consistent by construction)
movies = pd.DataFrame(movie_dicts)

# ------------------ INTERFACE ------------------
st.markdown('<div class="title">🎥 Movie Recommender System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Black theme, images guaranteed (placeholder used if no poster).</div>', unsafe_allow_html=True)

# Diagnostics for connectivity to image hosts
reach = can_reach_hosts()
if not reach.get("tmdb", True):
    st.warning("Cannot reach TMDb image CDN from this machine. Posters may not load.")
if not reach.get("placeholder_primary", True) and not reach.get("placeholder_secondary", True):
    st.warning("Cannot reach placeholder image services. Generated placeholders may not load.")

# Search + genre filter
col1, col2 = st.columns([3,1])
with col1:
    query = st.text_input("🔎 Search movie title (leave empty to show by genre)", value="").strip()
with col2:
    genre_choice = st.selectbox("🎭 Filter by genre", options=["All"] + sorted(movies["Genre"].unique()))

# Optional: allow disabling URL validation if outbound requests are blocked
validate_urls = st.toggle("Validate poster URLs (disable if behind firewall)", value=True)

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
        # validate URL; fall back to title-specific placeholder(s) if unreachable
        if not poster_url or poster_url == PLACEHOLDER or (validate_urls and not is_url_ok(poster_url)):
            candidate = build_placeholder(row['Title'], secondary=False)
            if not (not validate_urls or is_url_ok(candidate)):
                candidate = build_placeholder(row['Title'], secondary=True)
            poster_url = candidate
        st.image(poster_url, width=180)
        st.markdown(f"**{row['Title']}**")
        st.markdown(f"<div class='meta'>⭐ {row['Rating']} &nbsp;|&nbsp; {row['Genre']}</div>", unsafe_allow_html=True)
