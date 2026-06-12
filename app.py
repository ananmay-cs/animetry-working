from anime_db import anime_db

anime = input("Enter anime: ")

if anime in anime_db:

    print(f"\nRating: {anime_db[anime]['rating']}")

    print("\nGenres:")

    for genre in anime_db[anime]["genres"]:
        print("-", genre)

    print("\nRecommendations:")

    for rec in anime_db[anime]["recommendations"]:
        print("-", rec)

else:
    print("Anime not found")