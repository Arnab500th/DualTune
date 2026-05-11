import os
import json
import base64
from ytmusicapi import YTMusic, OAuthCredentials

# Decode oauth.json from base64 secret at runtime
oauth_b64 = os.environ.get("YT_OAUTH_JSON")
if oauth_b64:
    oauth_b64 = oauth_b64.strip().lstrip('\ufeff')  # strip BOM + whitespace
    with open("oauth.json", "wb") as f:
        f.write(base64.b64decode(oauth_b64))

yt = YTMusic(
    "oauth.json",
    oauth_credentials=OAuthCredentials(
        client_id=os.environ["YT_CLIENT_ID"],
        client_secret=os.environ["YT_CLIENT_SECRET"],
    ),
)

if __name__ == "__main__":
    print("✅ YT Music authenticated successfully.")
    playlists = yt.get_library_playlists(limit=5)
    print(f"Found {len(playlists)} playlists:")
    for p in playlists:
        print(f"  - {p['title']} (id: {p['playlistId']})")