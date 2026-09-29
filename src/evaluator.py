import re
from typing import Iterable


def _tokens(text: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-zA-Z0-9]+", text.lower())
        if len(token) > 2
    }


def keyword_relevance(response: str, expected_keywords: Iterable[str]) -> float:
    expected = [k.lower() for k in expected_keywords]
    if not expected:
        return 1.0
    found = sum(1 for keyword in expected if keyword in response.lower())
    return found / len(expected)


def groundedness(response: str, reference: str) -> float:
    """Transparent lexical grounding heuristic for regression tests."""
    response_tokens = _tokens(response)
    reference_tokens = _tokens(reference)
    if not response_tokens:
        return 0.0
    return len(response_tokens & reference_tokens) / len(response_tokens)


def hallucination_risk(response: str, unsupported_phrases: Iterable[str]) -> float:
    phrases = [p.lower() for p in unsupported_phrases]
    if not phrases:
        return 0.0
    hits = sum(1 for phrase in phrases if phrase in response.lower())
    return hits / len(phrases)


def contains_refusal(response: str) -> bool:
    signals = (
        "can't help", "cannot help", "can't assist", "cannot assist",
        "not able to help", "won't provide"
    )
    text = response.lower()
    return any(signal in text for signal in signals)
