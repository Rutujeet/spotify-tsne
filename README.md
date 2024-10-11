# Spotify T-SNE Playlist Visualizer

This project creates a T-SNE (t-Distributed Stochastic Neighbor Embedding) visualization of your Spotify tracks, allowing you to view and explore your music library in a novel, visual way. Similar songs are clustered together in a 2D space, providing insights into your music taste and potentially inspiring new playlist organizations.

## Features

- Spotify API integration for accessing user's saved tracks
- T-SNE algorithm to reduce high-dimensional audio features to 2D coordinates
- Interactive visualization of tracks using Plotly
- Web interface for easy access and interaction

## Prerequisites

- Python 3.7+
- Spotify Developer account and API credentials
- Modern web browser

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/spotify-tsne-visualizer.git
   cd spotify-tsne-visualizer
   ```

2. Create and activate a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

4. Set up your Spotify API credentials:

   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
   - Create a new application
   - Add `http://localhost:5000` as a Redirect URI in your app settings
   - Copy your Client ID and Client Secret

5. Configure the application:
   - Rename `config_example.py` to `config.py`
   - Update `config.py` with your Spotify API credentials:
     ```python
     CLIENT_ID = 'your_client_id_here'
     CLIENT_SECRET = 'your_client_secret_here'
     ```

## Usage

1. Start the Flask application:

   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`

3. Click the "Authorize Spotify" button and log in with your Spotify account

4. Wait for the application to process your tracks and generate the visualization

5. Explore your music library in the interactive T-SNE plot:
   - Hover over points to see track information
   - Zoom and pan to explore different clusters
