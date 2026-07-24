# 🎬 Content-Based Movie Recommender System

A Content-Based Movie Recommendation System built using Python, Scikit-Learn, Pandas, and Streamlit. The application recommends top 5 similar movies based on metadata similarity and dynamically fetches movie posters using the OMDb API.

---

## 📌 Project Overview

This project uses the **TMDB 5000 Movie Dataset** to analyze movie metadata (genres, keywords, overview descriptions) and compute similarity scores between movies using **Cosine Similarity**. When a user selects a movie, the system finds the 5 closest matching titles and displays them along with their official posters.

---

## 🛠️ How It Works

1. **Feature Extraction**:
   - Metadata columns (`genres`, `keywords`, `overview`) are extracted from the dataset.
   - String representations of list attributes are parsed using `ast.literal_eval`.
   - Spaces within tags are removed to avoid mixing distinct terms (e.g., `Science Fiction` -> `ScienceFiction`).
   - A single unified `tags` column is created per movie.

2. **Vectorization (Bag of Words)**:
   - `CountVectorizer` converts textual tags into numerical feature vectors.
   - Retains top **5,000** most frequent words while removing standard English stop words.

3. **Similarity Calculation**:
   - **Cosine Similarity** measures the angular similarity between movie vectors:
     $$\text{Cosine Similarity}(A, B) = \frac{A \cdot B}{\|A\| \|B\|}$$
   - Pre-computed similarity matrix is saved as compressed `.pkl.gz` files (`movies.pkl.gz` and `similar.pkl.gz`) for fast web application performance.

4. **Web Interface & Poster Fetching**:
   - Built with **Streamlit** for an interactive dropdown & card display.
   - Dynamically fetches official movie posters using the **OMDb API** search.

---

## 📁 Repository Structure

```text
├── app.py                  # Streamlit web application
├── movie.ipynb             # Jupyter Notebook (Data Processing & Model Training)
├── requirements.txt        # Python dependency list
├── movies.pkl.gz           # Compressed processed DataFrame pickle
├── similar.pkl.gz          # Compressed similarity matrix pickle
├── tmdb_5000_movies.csv    # Original TMDB Movies dataset
├── tmdb_5000_credits.csv   # Original TMDB Credits dataset
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

Ensure you have **Python 3.9+** installed on your system.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/prakash-knight/Movie-recommender.git
   cd Movie-recommender
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

4. **View in Browser**:
   Open `http://localhost:8501` in your browser.

---

## 💻 Tech Stack

- **Language**: Python 3.9
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn (`CountVectorizer`, `cosine_similarity`)
- **Web Framework**: Streamlit
- **API**: OMDb API (Movie Posters)

---

## 🌐 Deployment

To deploy on **Streamlit Community Cloud**:
1. Push this repository to GitHub.
2. Sign in to [share.streamlit.io](https://share.streamlit.io/).
3. Connect your GitHub repository (`prakash-knight/Movie-recommender`) and set Main file path to `app.py`.
4. Click **Deploy**!

---

## 📜 License

This project is open-source and available under the MIT License.
