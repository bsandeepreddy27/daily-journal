import os
import random
import requests
from datetime import datetime

JOURNAL_DIR = "journal_entries"
LOG_FILE = "DAILY_LOG.md"

quotes = [
    "Learning never exhausts the mind.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "First, solve the problem. Then, write the code.",
    "Experience is the name everyone gives to their mistakes.",
    "Knowledge is power."
]

def get_weather():
    try:
        response = requests.get("https://wttr.in/?format=3")
        return response.text.strip()
    except:
        return "Weather data unavailable"

def get_word_of_day():
    try:
        response = requests.get("https://random-word-api.herokuapp.com/word")
        return response.json()[0]
    except:
        return "inspiration"

def add_entry():
    if not os.path.exists(JOURNAL_DIR):
        os.makedirs(JOURNAL_DIR)

    # Date and timestamp
    now = datetime.now()
    today = now.strftime("%Y-%m-%d")
    timestamp = now.strftime("%H:%M:%S")
    filename = os.path.join(JOURNAL_DIR, f"{today}_{now.strftime('%H-%M-%S')}.txt")

    entry = f"""
📅 Date: {today}
⏰ Time: {timestamp}
🌦 Weather: {get_weather()}
📚 Word of the Day: {get_word_of_day()}
💡 Quote: {random.choice(quotes)}
    """.strip()

    # Save to individual file
    with open(filename, "w") as f:
        f.write(entry + "\n")

    # Update DAILY_LOG.md
    with open(LOG_FILE, "w") as f:
        f.write(f"# 📓 Daily Journal Log\n\n")
        f.write(f"## Latest Entry\n\n{entry}\n")
        f.write(f"\n👉 Check all entries in [journal_entries/](./journal_entries)\n")

    print(f"✅ Auto-entry saved: {filename}")


if __name__ == "__main__":
    add_entry()
