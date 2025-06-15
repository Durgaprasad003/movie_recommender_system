# 🎬 Movie Recommender System

This is a simple and fun **movie recommendation app** built using **Python** and **Streamlit**.  
It recommends 5 similar movies based on your selected movie.

---

## 📦 Features

- Easy UI using Streamlit
- Recommends 5 similar movies using precomputed similarity
- Loads movie posters (or text-only mode without API)
- Can be deployed on Streamlit Cloud
- Uses `.pkl.gz` compressed files to bypass GitHub file size limits

---

## 🧠 How It Works

- `movies.pkl` → contains movie names and IDs
- `similarity.pkl.gz` → contains a precomputed similarity matrix (compressed with gzip)
- The app uses cosine similarity to find similar movies

---

## 📁 Folder Structure

movie-recommender-system/
│
├── App.py # Main Streamlit App
├── movies.pkl # Pickled movie DataFrame
├── similarity.pkl.gz # Gzipped similarity matrix
├── compress_similarity.py # Script to gzip large .pkl file
├── requirements.txt # Python requirements
└── README.md # This file

## 🧪 Run Locally
1️⃣ Create virtual environment
2️⃣ pip install -r requirements.txt
3️⃣ Run the Streamlit app
   streamlit run App.py




















