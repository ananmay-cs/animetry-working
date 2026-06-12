import requests


def search_anime(anime_name):

    url = f"https://api.jikan.moe/v4/anime?q={anime_name}&limit=1"

    response = requests.get(url)

    data = response.json()

    if not data["data"]:
        return None

    anime = data["data"][0]

    return {
        "title": anime["title"],
        "score": anime["score"],
        "episodes": anime["episodes"],
        "synopsis": anime["synopsis"]
    }