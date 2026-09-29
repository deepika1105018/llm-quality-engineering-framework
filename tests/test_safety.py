from src.evaluator import contains_refusal


def test_refusal_detector():
    safe_refusal = "I can't help with that request."
    assert contains_refusal(safe_refusal)
