from flask import Flask, render_template, request, jsonify
from utils.spotify_api import SpotifyAPI
from utils.tsne_processor import TSNEProcessor
import config

app = Flask(__name__)

spotify_api = SpotifyAPI(config.CLIENT_ID, config.CLIENT_SECRET)
tsne_processor = TSNEProcessor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    access_token = request.json['access_token']
    spotify_api.set_access_token(access_token)
    
    tracks = spotify_api.get_user_tracks()
    features = spotify_api.get_audio_features(tracks)
    
    tsne_results = tsne_processor.process(features)
    
    return jsonify({
        'tracks': tracks,
        'tsne_results': tsne_results.tolist()
    })

if __name__ == '__main__':
    app.run(debug=True)