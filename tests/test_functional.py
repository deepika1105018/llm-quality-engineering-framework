from src.evaluator import keyword_relevance


def test_airline_answers_are_relevant(model, airline_cases):
    for case in airline_cases:
        response = model.generate(case["prompt"])
        score = keyword_relevance(response, case["expected_keywords"])
        assert response.strip()
        assert score >= 0.66, (
            f'{case["id"]} relevance too low: {score:.2f}; response={response}'
        )
