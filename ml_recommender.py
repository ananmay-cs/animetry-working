from anime_db import anime_db
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

anime_names = list(anime_db.keys())

genre_strings = [
    " ".join(anime_db[anime]["genres"])
    for anime in anime_names
]

vectorizer = TfidfVectorizer()

genre_matrix = vectorizer.fit_transform(genre_strings)

similarity_matrix = cosine_similarity(genre_matrix)


def recommend(anime_name, top_n=3):

    if anime_name not in anime_db:
        return []

    anime_index = anime_names.index(anime_name)

    similarity_scores = list(
        enumerate(similarity_matrix[anime_index])
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for index, score in similarity_scores[1:top_n + 1]:
        recommendations.append(anime_names[index])

    return recommendations