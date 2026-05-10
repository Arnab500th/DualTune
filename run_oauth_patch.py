# run_oauth_patch.py  — run once locally
from ytmusicapi.auth.oauth.credentials import OAuthCredentials
from ytmusicapi.auth.oauth.token import RefreshingToken
import requests, json

CLIENT_ID = ""
CLIENT_SECRET = ""

creds = OAuthCredentials(CLIENT_ID, CLIENT_SECRET)
code = creds.get_code()
print(f"Go to: https://www.google.com/device?user_code={code['user_code']}")
input("Press Enter after login...")

raw = creds.token_from_code(code["device_code"])
raw.pop("refresh_token_expires_in", None)   # strip the bad key
token = RefreshingToken(credentials=creds, **raw)
token.store_token("oauth.json")
print("oauth.json written.")