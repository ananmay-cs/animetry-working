from anime_db import anime_db
from anime_api import search_anime
from ml_recommender import recommend

anime_lookup = {
    anime.lower(): anime
    for anime in anime_db
}

print("\n🎌 Welcome to Animetry")
print("-" * 40)

while True:

    query = input(
        "\nEnter an anime (or 'quit'): "
    ).strip()

    if query.lower() == "quit":
        print("\nThanks for using Animetry! 👋")
        break

    anime_data = search_anime(query)

    if not anime_data:
        print("\n❌ Anime not found.")
        continue

    print("\n" + "=" * 50)
    print(f"🎌 {anime_data['title']}")
    print("=" * 50)

    print(f"⭐ Rating: {anime_data['score']}")
    print(f"📺 Episodes: {anime_data['episodes']}")

    print("\n📖 Synopsis:")

    synopsis = anime_data.get("synopsis")

    if synopsis:
        print(synopsis[:300] + "...")
    else:
        print("No synopsis available.")

    anime_name = anime_lookup.get(query.lower())

    if anime_name:

        print("\n🤖 Recommended For You")

        recommendations = recommend(anime_name)

        for rec in recommendations:
            print(
                f"- {rec['title']} "
                f"({rec['similarity']}% match)"
            )

    else:
        print(
            "\n⚠️ No ML recommendations available yet "
            "for this anime."
        )