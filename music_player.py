import urllib.request
import urllib.parse
import re  # The Regex tool for searching text
import webbrowser
import random

# 1. Your customized dictionary
EMOTION_MUSIC_MAP = {
    "Stressed": "relaxing lo-fi chill bollywood beats",
    "Calm": "acoustic nature music",
    "Happy": "upbeat workout bollywood music",
    "Sad": "uplifting motivational songs",
    "Workout": "Gym music",
}


def play_music_for_emotion(detected_emotion):
    """
    Searches YouTube silently, finds the top videos,
    picks one randomly, and auto-plays it!
    """
    search_query = EMOTION_MUSIC_MAP.get(detected_emotion, "lofi girl radio")

    print(f"🎵 Backend received emotion: {detected_emotion}")
    print(f"🔍 Finding a random song for: '{search_query}'...")

    # 2. Format the search query for the URL (e.g., replaces spaces with +)
    encoded_query = urllib.parse.quote_plus(search_query)
    search_url = (
        f"https://www.youtube.com/results?search_query={encoded_query}&sp=EgQQARgC"
    )

    try:
        # 3. Visit YouTube and read the background code of the search page
        html_content = urllib.request.urlopen(search_url)

        # 4. Use Regex (re) to find all the video IDs in that code
        # Every YouTube video ID is exactly 11 characters long
        video_ids = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())

        # 5. If we found videos, pick a random one from the top 5!
        if video_ids:
            # We slice the list [:5] to only pick from the most relevant top 5 results
            top_results = video_ids[:50]
            chosen_id = random.choice(top_results)

            # Create the final auto-play link
            final_url = f"https://www.youtube.com/watch?v={chosen_id}"

            print("🎲 Found videos! Playing a random one now...")
            print(f"🌐 Opening: {final_url}")

            # 6. Open the browser to auto-play!
            webbrowser.open(final_url)
        else:
            print("❌ Couldn't find any videos.")

    except Exception as e:
        print(f"⚠️ Oops! Something went wrong: {e}")


# --- FOR TESTING ONLY ---
if __name__ == "__main__":
    print("Testing the clever music player...")
    # Run this multiple times, it will play a different song each time!
    play_music_for_emotion("Stressed")
