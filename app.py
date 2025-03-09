import streamlit as st
import json
from datetime import datetime

st.set_page_config(
    page_title="Sptofiy JSON Playlist Viewer",
    page_icon="🎶",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# Thank you for using the app. Developed by Nityoday Tekchandani, with the assistance of gemini-2.0-flash-thinking-exp-01-21 AI LLM Model"
    }
)

def load_playlist_data(uploaded_file):
    """Loads playlist data from an uploaded JSON file."""
    try:
        data = json.load(uploaded_file)
        return data
    except json.JSONDecodeError:
        st.error("Error decoding JSON. Please ensure the uploaded file is a valid JSON file.")
        return None
    except Exception as e:
        st.error(f"An error occurred while loading playlist data: {e}")
        return None

def format_date(date_str):
    """Formats a date string from YYYY-MM-DD to DD-MMM-YYYY."""
    try:
        date_object = datetime.strptime(date_str, "%Y-%m-%d")
        formatted_date = date_object.strftime("%d-%b-%Y") # e.g., 03-Jun-2025
        return formatted_date
    except ValueError: # Handle cases where date_str is not in the expected format
        return date_str # Return original string if parsing fails

def main():
    st.title("Spotify Playlist Viewer")

    # State to track if file is uploaded
    if 'file_uploaded' not in st.session_state:
        st.session_state['file_uploaded'] = False

    # File uploader widget (initially visible)
    if not st.session_state['file_uploaded']:
        uploaded_file = st.file_uploader("Upload your Playlist1.json or json file for playlist here", type=["json"], key="file_uploader")

        if uploaded_file is not None:
            playlist_data = load_playlist_data(uploaded_file)
            if playlist_data and 'playlists' in playlist_data and playlist_data['playlists']:
                st.session_state['playlist_data'] = playlist_data
                st.session_state['file_uploaded'] = True
                st.rerun()
            else:
                st.error("No playlists found in the uploaded JSON file or invalid format.")
                return
    else:
        playlist_data = st.session_state['playlist_data']
        uploaded_file = None

    if st.session_state['file_uploaded']:

        playlists = playlist_data['playlists']
        playlists.sort(key=lambda p: len(p['items']), reverse=True)
        playlist_names = [playlist['name'] for playlist in playlists]

        st.sidebar.header("Select Playlist")
        selected_playlist_name = st.sidebar.radio("Choose a playlist:", playlist_names)

        if selected_playlist_name:
            selected_playlist = next((playlist for playlist in playlists if playlist['name'] == selected_playlist_name), None)

            if selected_playlist:
                st.header(selected_playlist['name'])
                # Format lastModifiedDate
                formatted_modified_date = format_date(selected_playlist['lastModifiedDate'])
                st.write(f"Last Modified Date: {formatted_modified_date}")
                st.write(f"Number of Followers: {selected_playlist['numberOfFollowers']}")
                if selected_playlist['description']:
                    st.write(f"Description: {selected_playlist['description']}")
                else:
                    st.write("No description available.")

                st.subheader("Tracks in this Playlist:")

                if selected_playlist['items']:
                    track_data = []
                    for item in selected_playlist['items']:
                        if item['track']:
                            track = item['track']
                            # Format addedDate
                            formatted_added_date = format_date(item['addedDate'])
                            track_info = {
                                "Track Name": track['trackName'],
                                "Artist Name": track['artistName'],
                                "Album Name": track['albumName'],
                                "Spotify URI": track['trackUri'],
                                "Added Date": formatted_added_date # Use formatted date here
                            }
                            track_data.append(track_info)
                    st.dataframe(track_data, width=None, column_config={
                           "Spotify URI": st.column_config.LinkColumn("Spotify URI")
                        },
                        hide_index=True)

                else:
                    st.info("This playlist has no tracks.")
            else:
                st.error("Selected playlist not found in data.")
        else:
            st.info("Please select a playlist from the sidebar to view its details.")

if __name__ == "__main__":
    main()
