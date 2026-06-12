from anime_db import anime_db
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

anime_names = list(anime_db.keys())

genres = [
    " ".join(anime_db[anime]["genres"])
    for anime in anime_names
]

vectorizer = TfidfVectorizer()
genre_matrix = vectorizer.fit_transform(genres)

similarity_matrix = cosine_similarity(genre_matrix)


def recommend(anime_name, top_n=5):

    if anime_name not in anime_db:
        return []

    anime_index = anime_names.index(anime_name)

    similarities = list(
        enumerate(similarity_matrix[anime_index])
    )

    similarities.sort(
        key=lambda item: item[1],
        reverse=True
    )

    recommendations = []

    for index, score in similarities[1:top_n + 1]:

        recommendations.append({
            "title": anime_names[index],
            "similarity": round(score * 100, 1)
        })

    return recommendations