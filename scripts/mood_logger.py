# mood_logger.py

import datetime

def save_mood_entry(mood, reflection, affirmation):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"""---\nDate: {timestamp}
Mood: {mood}
Reflection: {reflection}
Affirmation: {affirmation}
"""
    with open("moodlogs/mood_log.txt", "a") as file:
        file.write(entry)

# Example usage
if __name__ == "__main__":
    mood = input("Mood (emoji): ")
    reflection = input("Reflection: ")
    affirmation = input("Affirmation: ")
    save_mood_entry(mood, reflection, affirmation)
    print("🌿 Entry saved successfully.")
