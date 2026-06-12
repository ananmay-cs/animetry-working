from anime_db import anime_db
from ml_recommender import recommend

anime_lookup = {
    anime.lower(): anime
    for anime in anime_db
}

user_input = input("Enter anime: ").strip().lower()

if user_input in anime_lookup:

    anime = anime_lookup[user_input]

    print(f"\nRating: {anime_db[anime]['rating']}")

    print("\nGenres:")

    for genre in anime_db[anime]["genres"]:
        print("-", genre)

    print("\nML Recommendations:")

    recommendations = recommend(anime)

    for anime_name, score in recommendations:
        print(f"- {anime_name} ({score}% match)")

else:

    print("\nAnime not found.")

    print("\nAvailable anime:")

    for anime in sorted(anime_db.keys()):
        print("-", anime)