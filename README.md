# 🎬 Content-Based Movie Recommender System

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://movie-recommender-udhf4psqmtpy63nqkhxvdf.streamlit.app/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/prakash-knight/Movie-recommender)

A high-performance Content-Based Movie Recommendation System built using Python, Scikit-Learn, Pandas, and Streamlit. The application recommends top 5 similar movies based on metadata similarity (genres, keywords, and plot summaries) and dynamically fetches official movie posters using the OMDb API.

🔗 **Live Web Application**: [https://movie-recommender-udhf4psqmtpy63nqkhxvdf.streamlit.app/](https://movie-recommender-udhf4psqmtpy63nqkhxvdf.streamlit.app/)

---

## 📌 Project Overview

This system analyzes the **TMDB 5000 Movie Dataset** to build an interactive recommendation engine:
- **Feature Processing**: Combines genres, keywords, and plot overviews into a unified text feature vector (`tags`).
- **Vectorization**: Uses `CountVectorizer` (Bag-of-Words) with top **5,000** features excluding English stop words.
- **Similarity Computation**: Measures angular distance between movie feature vectors using **Cosine Similarity**:
  $$\text{Cosine Similarity}(A, B) = \frac{A \cdot B}{\|A\| \|B\|}$$
- **Latency Optimization**: Pre-computes and compresses $4,800 \times 4,800$ similarity matrices into gzipped pickles (`similar.pkl.gz` & `movies.pkl.gz`) to achieve sub-**150ms** inference latency.
- **Dynamic Poster Integration**: Fetches high-resolution movie posters in real time using the **OMDb REST API**.

---

## 🚀 Live Demo

Access the deployed application on Streamlit Cloud:

👉 **[Launch Movie Recommender App](https://movie-recommender-udhf4psqmtpy63nqkhxvdf.streamlit.app/)**

---

## 📁 Repository Structure

```text
├── app.py                  # Streamlit web application & OMDb API integration
├── movie.ipynb             # Refactored Jupyter Notebook (Data Processing & Model Training)
├── requirements.txt        # Python dependency specifications
├── setup.sh                # Streamlit setup configuration script
├── procfile                # Deployment procfile configuration
├── movies.pkl.gz           # Compressed processed DataFrame pickle
├── similar.pkl.gz          # Compressed 4800x4800 similarity matrix pickle
└── README.md               # Project documentation
```

---

## 🛠️ Tech Stack & Tools

- **Core Language**: Python 3.9+
- **Data Engineering**: Pandas, NumPy
- **Machine Learning**: Scikit-Learn (`CountVectorizer`, `cosine_similarity`)
- **Web App & UI**: Streamlit Framework
- **API**: OMDb REST API (Movie Posters)
- **Serialization & Compression**: Pickle, Gzip

---

## ⚙️ Local Setup & Running

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/prakash-knight/Movie-recommender.git
   cd Movie-recommender
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Streamlit Application**:
   ```bash
   streamlit run app.py
   ```

4. **Open in Browser**:
   Navigate to `http://localhost:8501` to use the app locally.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
