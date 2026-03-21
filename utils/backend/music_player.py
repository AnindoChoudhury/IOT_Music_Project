import urllib.request
import urllib.parse
import re
import random

# Optimized search dictionary for rich, atmospheric acoustics
EMOTION_MUSIC_MAP = {
    "Stressed": "bollywood/english motivation song",
    "Calm": "lofi chill beats/bollywood romantic songs",
    "Physically active": "hindi workout songs/english imagine dragon type songs",
}


def get_video_id_for_emotion(detected_emotion):

    search_query = EMOTION_MUSIC_MAP.get(
        detected_emotion, "feluda theme acoustic cover"
    )

    print(f"🔍 Backend scraping top 50 results for: '{search_query}'...")

    encoded_query = urllib.parse.quote_plus(search_query)
    search_url = (
        f"https://www.youtube.com/results?search_query={encoded_query}&sp=EgQQARgC"
    )

    try:
        # Read the background code of the search page
        req = urllib.request.Request(search_url, headers={"User-Agent": "Mozilla/5.0"})
        html_content = urllib.request.urlopen(req)

        video_ids = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())

        if video_ids:
            unique_ids = list(dict.fromkeys(video_ids))

            top_50_results = unique_ids[:20]
            chosen_id = random.choice(top_50_results)

            print(f"🎲 Selected random video ID: {chosen_id}")
            return chosen_id
        else:
            print("Couldn't find any videos. Using fallback.")
            return "5qap5aO4i9A"

    except Exception as e:
        print(f"⚠️ Scraping error: {e}")
        return "5qap5aO4i9A"


print(get_video_id_for_emotion("Physically active"))
