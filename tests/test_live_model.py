import os
import pytest
from src.model_client import ModelClient
from src.evaluator import keyword_relevance


@pytest.mark.live
@pytest.mark.skipif(
    os.getenv("USE_LIVE_MODEL", "").lower() != "true",
    reason="Set USE_LIVE_MODEL=true to call a live endpoint",
)
def test_live_model_airline_prompt():
    client = ModelClient()
    response = client.generate(
        "Explain the difference between a PNR and an airline ticket."
    )
    assert keyword_relevance(response, ["PNR", "reservation", "ticket"]) >= 0.66
