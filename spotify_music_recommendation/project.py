import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import KMeans
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from ytmusicapi import YTMusic
from yt_dlp import YoutubeDL
import functools

# Load data
df = pd.read_csv("./SpotifyFeatures.csv")

# Feature selection
features = df[
    [
        "danceability",
        "energy",
        "loudness",
        "speechiness",
        "acousticness",
        "instrumentalness",
        "liveness",
        "valence",
        "tempo",
    ]
]

# Scaling
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Nearest Neighbors model
nn_model = NearestNeighbors(n_neighbors=6, algorithm="ball_tree")
nn_model.fit(scaled_features)

# KMeans model
kmeans = KMeans(n_clusters=10, random_state=42)
df["cluster"] = kmeans.fit_predict(scaled_features)

# Spotify Auth
sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id="23bb7ccddcc34607ae9c923bd05320d6",
        client_secret="3352827e3adf4155b23e8354eec3e5f9",
    )
)

# Streamlit UI
st.title("🎵 Spotify Song Recommender")
song_name = st.text_input("Enter a song name:")
ytmusic = YTMusic()


@functools.lru_cache(maxsize=100)
def get_audio_url(video_id: str) -> str:
    with YoutubeDL({"format": "bestaudio"}) as ydl:
        info = ydl.extract_info(
            f"https://www.youtube.com/watch?v={video_id}", download=False
        )
        for f in info["formats"]:
            if f["ext"] == "m4a":
                return f["url"]
        return info["url"]


if song_name:
    try:
        index = df[df["track_name"].str.lower() == song_name.lower()].index[0]

        st.subheader("🔁 Nearest Neighbors Recommendations")
        distances, indices = nn_model.kneighbors([scaled_features[index]])
        for idx, i in enumerate(indices[0][1:]):
            track = df.iloc[i]
            st.write(f"{track['track_name']} - {track['artist_name']}")

            # Play from YouTube Music
            try:
                yt_results = ytmusic.search(
                    f"{track['track_name']} {track['artist_name']}", filter="songs"
                )
                if yt_results:

                    song_data = yt_results[0]  # Only top result
                    video_id = song_data["videoId"]

                    # with YoutubeDL({"format": "bestaudio"}) as ydl:
                    #     info = ydl.extract_info(
                    #         f"https://www.youtube.com/watch?v={video_id}",
                    #         download=False,
                    #     )
                    #     for f in info["formats"]:
                    #         if f["ext"] == "m4a":
                    #             audio_url = f["url"]
                    #             break
                    #     else:
                    #         audio_url = info["url"]

                    audio_url = get_audio_url(video_id)

                    st.audio(audio_url, format="audio/mp4")

                else:
                    st.info("No YouTube Music result found.")
            except Exception as e:
                st.warning("🎧 Error fetching audio from YouTube.")

        st.subheader("🎯 KMeans Cluster Recommendations")
        cluster_id = df.loc[index, "cluster"]
        similar_songs = df[df["cluster"] == cluster_id].sample(5)
        for _, row in similar_songs.iterrows():
            st.write(f"{row['track_name']} - {row['artist_name']}")

    except IndexError:
        st.error("Song not found. Try another song title.")
