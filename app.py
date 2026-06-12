from anime_db import anime_db
from ml_recommender import recommend
from anime_api import search_anime

anime_lookup = {
    anime.lower(): anime
    for anime in anime_db
}

user_input = input("Enter anime: ").strip()

api_data = search_anime(user_input)

if api_data:

    print(f"\nTitle: {api_data['title']}")
    print(f"Rating: {api_data['score']}")
    print(f"Episodes: {api_data['episodes']}")

    print("\nSynopsis:")
    print(api_data['synopsis'][:300] + "...")

else:
    print("Could not fetch online data.")

if user_input.lower() in anime_lookup:

    anime = anime_lookup[user_input.lower()]

    print("\nML Recommendations:")

    recommendations = recommend(anime)

    for anime_name, score in recommendations:
        print(f"- {anime_name} ({score}% match)")