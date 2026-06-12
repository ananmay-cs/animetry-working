from anime_db import anime_db
from ml_recommender import recommend

anime = input("Enter anime: ")

if anime in anime_db:

    print(f"\nRating: {anime_db[anime]['rating']}")

    print("\nGenres:")

    for genre in anime_db[anime]["genres"]:
        print("-", genre)

    print("\nML Recommendations:")

    recommendations = recommend(anime)

    for item in recommendations:
        print("-", item)

else:
    print("Anime not found")