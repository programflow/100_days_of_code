from oauth_token_manager import OAuthTokenManager
import requests

manager = OAuthTokenManager(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    refresh_token="YOUR_REFRESH_TOKEN",
    token_url="https://accounts.spotify.com/api/token"
)

access_token = manager.get_access_token()

headers = {
    "Authorization": f"Bearer {access_token}"
}

response = requests.get("https://api.spotify.com/v1/me", headers=headers)
print(response.json())
