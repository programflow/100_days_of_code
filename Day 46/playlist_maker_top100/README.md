# 🎵 Billboard to Spotify Playlist Converter

This Python script scrapes the Billboard Hot 100 for a user-specified date and creates a private Spotify playlist with the corresponding songs (if available).

## 📦 Features

- Scrapes Billboard.com Hot 100 chart using `requests` and `BeautifulSoup`
- Searches each track in Spotify using `spotipy`
- Creates a private playlist and populates it with found tracks
- Filters out unavailable or ambiguous entries

## 🔧 Requirements

- Python 3.10+
- Spotify Developer credentials
- `.env` file with:
  ```env
  SPOTIFY_CLIENT_ID=your_client_id
  SPOTIFY_CLIENT_SECRET=your_client_secret
  ```

## 📌 Setup Instructions

1. Clone the repo and create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Set up your `.env` file.

3. Run the script and enter a date like `2000-08-12` when prompted:
   ```bash
   python main.py
   ```

## 📎 Example Output

- Playlist created on Spotify with title: `2000-08-12 Billboard 100`
- Logs skipped songs with clear reasons

## 🛠️ Tech Stack

- `requests`
- `beautifulsoup4`
- `spotipy`
- `python-dotenv`

## 💡 Future Enhancements

- Add fuzzy matching for song titles
- Include song preview links
- Web version with Flask

---

## 🧾 Checklist Sync (Thursday GitHub Maintenance)

| Task                                 | Status |
|--------------------------------------|--------|
| Add proper README.md                 | ✅     |
| Organize folder structure (`src/`)   | ✅/Optional |
| Push updates with commit message     | ✅     |