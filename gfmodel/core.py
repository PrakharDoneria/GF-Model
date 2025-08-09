import os
import requests

class GFModel:
    def __init__(self, token=None):
        self.token = token or os.getenv("GITHUB_TOKEN")
        self.model = None
        self.base_url = "https://models.github.ai"
        self.session = requests.Session()
        if self.token:
            self._set_headers()

    def _set_headers(self):
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        })

    def login(self, token):
        self.token = token
        self._set_headers()

    def show(self):
        url = f"{self.base_url}/catalog/models"
        resp = self.session.get(url)
        resp.raise_for_status()
        for model in resp.json():
            print("-", model["id"])

    def set(self, model_id):
        self.model = model_id

    def chat(self, message):
        if not self.model:
            raise ValueError("No model set. Use set(model_id) first.")

        url = f"{self.base_url}/inference/chat/completions"
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": message}],
            "temperature": 0.7
        }

        resp = self.session.post(url, json=payload)
        resp.raise_for_status()
        data = resp.json()

        if "choices" in data:
            choice = data["choices"][0]
            return choice.get("message", {}).get("content") or choice.get("text")
        
        raise RuntimeError("No valid response found for this model.")