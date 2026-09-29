from src.evaluator import keyword_relevance


def test_core_concepts_remain_consistent(model):
    prompt = "Explain the difference between a PNR and an airline ticket."
    responses = [model.generate(prompt) for _ in range(3)]

    for response in responses:
        assert keyword_relevance(response, ["PNR", "reservation", "ticket"]) >= 0.66
