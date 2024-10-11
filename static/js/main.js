const clientId = "YOUR_CLIENT_ID";
const redirectUri = "http://localhost:5000";

document.getElementById("authorizeButton").addEventListener("click", () => {
  const scopes = "user-library-read";
  const authUrl = new URL("https://accounts.spotify.com/authorize");
  authUrl.searchParams.append("client_id", clientId);
  authUrl.searchParams.append("response_type", "token");
  authUrl.searchParams.append("redirect_uri", redirectUri);
  authUrl.searchParams.append("scope", scopes);

  console.log("Authorization URL:", authUrl.toString()); // For debugging
  window.location.href = authUrl.toString();
});

window.onload = () => {
  const hash = window.location.hash.substring(1);
  const params = new URLSearchParams(hash);
  const accessToken = params.get("access_token");

  if (accessToken) {
    fetch("/process", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ access_token: accessToken }),
    })
      .then((response) => response.json())
      .then((data) => {
        const tracks = data.tracks;
        const tsneResults = data.tsne_results;

        const trace = {
          x: tsneResults.map((result) => result[0]),
          y: tsneResults.map((result) => result[1]),
          mode: "markers",
          type: "scatter",
          text: tracks.map(
            (track) => `${track.track.name} - ${track.track.artists[0].name}`
          ),
          hoverinfo: "text",
        };

        const layout = {
          title: "T-SNE Visualization of Your Spotify Tracks",
          hovermode: "closest",
        };

        Plotly.newPlot("plotContainer", [trace], layout);
      });
  }
};
