# export_tool.py

def export_log_txt():
    try:
        with open("moodlogs/mood_log.txt", "r") as source:
            content = source.read()
        with open("moodlogs/mood_log_export.txt", "w") as export:
            export.write(content)
        print("📄 Log exported to 'mood_log_export.txt'")
    except FileNotFoundError:
        print("⚠️ No log file found to export.")

if __name__ == "__main__":
    export_log_txt()
