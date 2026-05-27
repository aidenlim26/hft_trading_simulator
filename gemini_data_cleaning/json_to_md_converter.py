import json
import os
import re
import html
from datetime import datetime

# ==========================================
# ⚙️ SETTINGS
# ==========================================
# 1. Update this date to filter out old data
START_DATE = "2026-05-15"

# 2. Update this to match your specific export day for the folder name
EXPORT_DATE_WAYPOINT = "2026-05-27"

# 3. Path updated to your specific programming_roadmap project folder
BASE_PATH = os.path.expanduser("~/Library/Mobile Documents/com~apple~CloudDocs/programming_roadmap/gemini_data_cleaning")

INPUT_FILE = os.path.join(BASE_PATH, 'MyActivity.json')

# Path updated to match your screenshot hierarchy inside your project folder
OUTPUT_DIR = os.path.join(BASE_PATH, "Chat Logs", EXPORT_DATE_WAYPOINT)
# ==========================================

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def clean_content(text):
    if not text: return ""
    text = html.unescape(text)
    text = re.sub(r'<(/?strong|b)>', '**', text)
    text = re.sub(r'<.*?>', '', text)
    return text.strip()

def sanitize_filename(filename):
    filename = filename.replace('\n', ' ').replace('\r', '')
    return re.sub(r'[\\/*?:"<>|]', '', filename).strip()

try:
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"❌ Error: 'MyActivity.json' not found in: {BASE_PATH}")
    exit()

print(f"Extracting items after {START_DATE} into waypoint: {EXPORT_DATE_WAYPOINT}")

new_count = 0
skip_count = 0

for entry in data:
    timestamp_raw = entry.get('time', '2000-01-01T00:00:00.000Z')
    
    if timestamp_raw[:10] >= START_DATE:
        try:
            prompt = entry.get('title', 'Untitled').replace('Prompted ', '')
            safe_title = sanitize_filename(prompt)[:50]
            
            # Filename keeps the original message date for sorting
            filename = f"{timestamp_raw[:10]}_{safe_title}.md"

            ai_responses = [clean_content(item['html']) for item in entry.get('safeHtmlItem', []) if 'html' in item]
            full_response = "\n\n---\n\n".join(ai_responses)

            with open(os.path.join(OUTPUT_DIR, filename), 'w', encoding='utf-8') as f:
                f.write(f"---\ndate: {timestamp_raw}\ntags: #GeminiExport\n---\n\n")
                f.write(f"# {prompt}\n\n{full_response}")
            
            new_count += 1
        except Exception as e:
            print(f"Error: {e}")
    else:
        skip_count += 1

print(f"\n--- Waypoint Created ---")
print(f"Folder: {OUTPUT_DIR}")
print(f"Files Created: {new_count}")
print(f"Items Skipped: {skip_count}")