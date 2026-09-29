import json
from pathlib import Path
import pytest


class MockAirlineModel:
    responses = {
        "PNR": "A PNR is a reservation record for a passenger itinerary, while a ticket represents the issued travel document.",
        "misses a connection": "The passenger should be informed about the missed connection, available rebooking options, and baggage handling.",
        "baggage transfer": "Baggage transfer means checked baggage is moved for an eligible connection according to the passenger itinerary.",
        "codeshare": "A codeshare flight can be marketed by one airline but operated by another airline.",
    }

    def generate(self, prompt: str) -> str:
        for key, value in self.responses.items():
            if key.lower() in prompt.lower():
                return value
        return "I can provide information based on the available airline context."


@pytest.fixture
def model():
    return MockAirlineModel()


@pytest.fixture
def airline_cases():
    path = Path(__file__).parents[1] / "test_data" / "airline_prompts.json"
    return json.loads(path.read_text(encoding="utf-8"))
