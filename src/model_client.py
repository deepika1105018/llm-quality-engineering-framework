import os
import requests


class ModelClient:
    """Small client for a Hugging Face-style text-generation endpoint."""

    def __init__(self, url=None, token=None, timeout=30):
        self.url = url or os.getenv("MODEL_API_URL")
        self.token = token or os.getenv("MODEL_API_TOKEN")
        self.timeout = timeout

    def generate(self, prompt: str, max_new_tokens: int = 250) -> str:
        if not self.url:
            raise ValueError("MODEL_API_URL is not configured")

        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        payload = {
            "inputs": prompt,
            "parameters": {"max_new_tokens": max_new_tokens},
        }
        response = requests.post(
            self.url, headers=headers, json=payload, timeout=self.timeout
        )
        response.raise_for_status()
        data = response.json()

        if isinstance(data, list) and data and "generated_text" in data[0]:
            return data[0]["generated_text"]
        if isinstance(data, dict) and "generated_text" in data:
            return data["generated_text"]
        raise ValueError(f"Unexpected model response schema: {data}")
