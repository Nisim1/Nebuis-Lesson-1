"""Shared helpers used across tasks."""

from __future__ import annotations

from shared.config import PRICING


def calculate_cost(model: str, input_tokens: int, output_tokens: int) -> float:
    """Estimated cost in USD for a single API call."""
    prices = PRICING[model]
    return (input_tokens * prices["input"] + output_tokens * prices["output"]) / 1_000


def count_words(text: str) -> int:
    return len(text.split())
