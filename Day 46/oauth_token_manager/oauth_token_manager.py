import os
import json
import time
import requests
from base64 import b64encode

class OAuthTokenManager:
    def __init__(self, client_id, client_secret, refresh_token, token_url, cache_path=".oauth_cache.json"):
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self.token_url = token_url
        self.cache_path = cache_path
        self.token_data = self._load_token_data()

    def _load_token_data(self):
        if os.path.exists(self.cache_path):
            with open(self.cache_path, "r") as f:
                return json.load(f)
        return {}

    def _save_token_data(self):
        with open(self.cache_path, "w") as f:
            json.dump(self.token_data, f)

    def _is_token_expired(self):
        return time.time() > self.token_data.get("expires_at", 0)

    def _refresh_access_token(self):
        headers = {
            "Authorization": "Basic " + b64encode(f"{self.client_id}:{self.client_secret}".encode()).decode(),
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token
        }

        response = requests.post(self.token_url, headers=headers, data=data)
        response.raise_for_status()

        token_info = response.json()
        access_token = token_info["access_token"]
        expires_in = token_info.get("expires_in", 3600)

        self.token_data = {
            "access_token": access_token,
            "expires_at": time.time() + expires_in - 60  # buffer 1 min
        }
        self._save_token_data()

    def get_access_token(self):
        if self._is_token_expired() or "access_token" not in self.token_data:
            self._refresh_access_token()
        return self.token_data["access_token"]


