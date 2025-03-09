# Spotify Playlist Viewer (Streamlit App)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://spotify-playlist-json.streamlit.app/) 

## Overview

This Streamlit web application allows you to easily visualize and browse your Spotify playlists directly from your Spotify account data.  It reads a `Playlist1.json` file (exported from your Spotify account data request) and presents your playlists in a user-friendly interface.

## Features

*   **Playlist Listing:** Displays a list of your playlists in the sidebar, sorted by the number of songs (most to least).
*   **View reomved songs:** Displays songs which are no longer available in spotify, for you to add alternative versions.
*   **Playlist Details:** When you select a playlist, the main page shows:
    *   Playlist name
    *   Last Modified Date (formatted as DD-MMM-YYYY)
    *   Number of Followers
    *   Description (if available)
*   **Track List:** Displays a table of tracks within the selected playlist, including:
    *   Track Name
    *   Artist Name
    *   Album Name
    *   Spotify URI (clickable link to open the track on Spotify)
    *   Added Date (formatted as DD-MMM-YYYY)
*   **File Upload:**  Allows you to upload your `Playlist1.json` file directly through the web interface.
*   **Clean UI:**  Uses a list-based playlist selector in the sidebar and displays track data in a wide, readable table.

## How to Use

1.  **Export your Spotify data:** Request your account data from Spotify through your account settings (Privacy Settings or Account Privacy -> Download your data -> Account Data). This will give you a `Playlist1.json` file (among other files) in a zip archive through an email in a few days (typically under 30 days).
2.  **Upload `Playlist1.json`:** In the Streamlit app, use the "Upload your Playlist1.json file" file uploader to select and upload the `Playlist1.json` file from your downloaded Spotify data.
3.  **Select Playlist:** Once the file is loaded, a list of your playlists will appear in the sidebar on the left. Choose a playlist name from the list.
4.  **View Playlist Details:** The main page will update to display the details of the selected playlist, including its tracks in a table format.
5.  **Click Track Links:** Click on the "Spotify URI" links in the track table to open the corresponding track directly in the Spotify web player or app.

## How to Run Locally (For Developers)

If you want to run this app locally for development or testing:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/nityoday/streamlit-spotify-json-playlist-viewer.git
    cd streamlit-spotify-json-playlist-viewer
    ```


2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # Activate the virtual environment:
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows (Command Prompt):
    venv\Scripts\activate.bat
    # On Windows (PowerShell):
    venv\Scripts\Activate.ps1
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit app:**
    ```bash
    streamlit run playlist_viewer.py
    ```

5.  **Open in Browser:** The app will open in your web browser (usually at `http://localhost:8501`).

## Deployment

This app is deployed on [Streamlit Community Cloud](https://streamlit.io/cloud). You can access the live app here:

[https://spotify-playlist-json.streamlit.app/](https://spotify-playlist-json.streamlit.app/) 

## Disclaimer

**This Spotify Playlist Viewer is an independent, personal project and is NOT affiliated with, endorsed by, or officially connected with Spotify AB or any of its subsidiaries or affiliates.**

*   This application is intended for personal, non-commercial use only.
*   It utilizes data that users have personally exported from their Spotify accounts.
* All playlist data processing is performed locally within your web browser (client-side). No playlist data is transmitted to any external servers or saved by this application. Your data remains private on your computer.
*   This project is developed for educational and demonstration purposes to showcase Streamlit and data visualization techniques.
*   All Spotify trademarks, logos, and music track information are the property of Spotify AB and its respective owners.
*   Users are responsible for ensuring their use of this application complies with Spotify's Terms of Service and any applicable laws and regulations.

## Known Issues

* Sort by date in playlist view is inaccurate.

## Credits

*   Built with [Streamlit](https://streamlit.io/)
*   Data from [Spotify](https://www.spotify.com)
*   gemini-2.0-flash-thinking-exp-01-21 on [Google AI Studio](https://aistudio.google.com)
<hr>

***A message from gemini-2.0-flash-thinking-exp-01-21 to the world:**  "May this little app help you rediscover the joy in your music and inspire you to explore your own data in creative ways. Happy listening and happy coding!"*
