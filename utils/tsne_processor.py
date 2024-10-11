from sklearn.manifold import TSNE
import numpy as np

class TSNEProcessor:
    def __init__(self):
        self.tsne = TSNE(n_components=2, random_state=42)

    def process(self, features):
        # Extract relevant features
        feature_matrix = np.array([[
            f['danceability'],
            f['energy'],
            f['loudness'],
            f['speechiness'],
            f['acousticness'],
            f['instrumentalness'],
            f['liveness'],
            f['valence'],
            f['tempo']
        ] for f in features])
        
        # Apply T-SNE
        tsne_results = self.tsne.fit_transform(feature_matrix)
        return tsne_results