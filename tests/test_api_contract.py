import pytest
from src.model_client import ModelClient


def test_client_requires_endpoint(monkeypatch):
    monkeypatch.delenv("MODEL_API_URL", raising=False)
    client = ModelClient(url=None)
    with pytest.raises(ValueError, match="MODEL_API_URL"):
        client.generate("Hello")
