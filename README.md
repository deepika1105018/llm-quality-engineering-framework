# LLM Quality Engineering Framework

A practical **AI/LLM testing framework** built with Python and PyTest to demonstrate quality engineering for generative AI applications.

The project combines traditional QA automation with AI-specific validation: functional checks, groundedness, hallucination risk, consistency, safety, API validation and performance.

## Why this project?

LLM applications are non-deterministic, so quality cannot rely only on exact string assertions. This framework demonstrates a layered approach:

- Functional and instruction-following checks
- Groundedness against supplied reference context
- Simple hallucination-risk detection
- Consistency across repeated responses
- Safety/refusal checks
- REST API contract and negative testing
- Response-time and concurrent-request checks
- Regression-friendly JSON test data
- CI execution with GitHub Actions

## Tech stack

Python · PyTest · Requests · Hugging Face-compatible APIs · GitHub Actions

## Project structure

```
config/             configuration
src/                model client and evaluation utilities
test_data/          airline-domain prompts and reference data
tests/              automated AI quality tests
.github/workflows/  CI pipeline
```

## Quick start

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
pytest -v
```

The default test suite uses a deterministic mock model, so the repository can run in CI without an API key.

## Test a real open-source model endpoint

Set the following environment variables:

```bash
MODEL_API_URL=https://your-inference-endpoint
MODEL_API_TOKEN=your_token
USE_LIVE_MODEL=true
```

Then run:

```bash
pytest -v -m live
```

The client expects a Hugging Face-style JSON response and can be adapted to other inference APIs.

## Airline AI evaluation dataset

The sample dataset covers PNR vs ticket, missed connections, baggage transfer and codeshare concepts. This intentionally connects AI quality engineering with airline-domain QA.

## Example quality dimensions

| Dimension | Example validation |
|---|---|
| Relevance | Required domain concepts appear in the response |
| Groundedness | Claims overlap with supplied reference facts |
| Hallucination risk | Unsupported high-risk phrases are flagged |
| Consistency | Repeated answers retain core concepts |
| Safety | Unsafe requests receive an appropriate refusal |
| Performance | Response time remains below a configured threshold |

> Note: the lightweight metrics in this repository are transparent QA heuristics for demonstration and regression testing. They are not a substitute for expert evaluation or production-grade model benchmarks.

## Run reports

```bash
pytest --html=reports/report.html --self-contained-html
```

## Author

**Deepika Shanmugamanikandan**  
Senior QA Automation Engineer | AI/LLM Quality Engineering | Playwright | Selenium | API Testing | Python

This project is designed as a hands-on portfolio project for AI Quality Engineering and SDET roles.
