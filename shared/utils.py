"""Shared helpers used across tasks."""

from __future__ import annotations

from shared.config import PRICING


def calculate_cost(model: str, input_tokens: int, output_tokens: int) -> float:
    """Estimated cost in USD for a single API call."""
    prices = PRICING[model]
    return (input_tokens * prices["input"] + output_tokens * prices["output"]) / 1_000


def count_words(text: str) -> int:
    return len(text.split())


def rate_latency(latency_ms: float) -> str:
    if latency_ms <= 2000:
        return "good"
    if latency_ms <= 5000:
        return "ok"
    return "bad"


def rate_cost(cost_usd: float) -> str:
    if cost_usd <= 0.001:
        return "good"
    if cost_usd <= 0.005:
        return "ok"
    return "bad"


def rate_length(text: str) -> str:
    wc = len(text.split())
    if 50 <= wc <= 90:
        return "good"
    if 40 <= wc <= 110:
        return "ok"
    return "bad"


def build_user_message(row) -> str:
    return (
        f"Product: {row['product_name']}\n"
        f"Attributes: {row['Product_attribute_list']}\n"
        f"Material: {row['material']}\n"
        f"Warranty: {row['warranty']}"
    )
