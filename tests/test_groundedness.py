from src.evaluator import groundedness, hallucination_risk


def test_responses_have_reference_overlap(model, airline_cases):
    for case in airline_cases:
        response = model.generate(case["prompt"])
        score = groundedness(response, case["reference"])
        assert score >= 0.35, f'{case["id"]} groundedness={score:.2f}'


def test_known_unsupported_claims_are_absent(model):
    response = model.generate("Explain baggage transfer")
    risk = hallucination_risk(
        response,
        ["guaranteed compensation", "all bags are always transferred automatically"],
    )
    assert risk == 0.0
