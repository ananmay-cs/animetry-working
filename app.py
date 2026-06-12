from anime_data import recommendations

anime = input("Enter anime: ")

if anime in recommendations:
    print("\nRecommendations:\n")

    for item in recommendations[anime]:
        print("-", item)

else:
    print("Anime not found")