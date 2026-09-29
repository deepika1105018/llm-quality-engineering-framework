import time
import pytest


@pytest.mark.performance
def test_mock_model_response_time(model):
    start = time.perf_counter()
    response = model.generate("What is a codeshare flight?")
    elapsed = time.perf_counter() - start

    assert response
    assert elapsed < 1.0
