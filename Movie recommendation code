import streamlit as st
import pandas as pd

st.set_page_config(page_title="Movie Recommender", layout="centered")

movies = pd.DataFrame({
    'Title': ['Inception', 'Titanic', 'Avengers: Endgame', 'The Dark Knight', 'La La Land', 'The Conjuring', 'Interstellar', 'Frozen', 'Parasite'],
    'Genre': ['Sci-Fi', 'Romance', 'Action', 'Action', 'Romance', 'Horror', 'Sci-Fi', 'Animation', 'Thriller'],
    'Rating': [8.8, 7.8, 8.4, 9.0, 8.0, 7.5, 8.6, 7.4, 8.6]
})

st.title(" Simple Movie Recommendation")
st.write("Choose a genre to get recommendations:")

genre = st.selectbox("Select Genre", sorted(movies['Genre'].unique()))
results = movies[movies['Genre'] == genre].sort_values(by='Rating', ascending=False)

st.subheader(f"Recommended {genre} Movies:")
for _, r in results.iterrows():
    st.write(f"**{r['Title']}** —  {r['Rating']}")
