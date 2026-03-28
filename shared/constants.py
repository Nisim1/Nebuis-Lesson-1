"""Rubric definitions and scoring logic for Assignment 1."""

from __future__ import annotations

from typing import Literal

Rating = Literal["good", "ok", "bad"]

CRITERIA: list[str] = [
    "Fluency",
    "Grammar",
    "Tone",
    "Length",
    "Grounding",
    "Latency",
    "Cost",
]

JUDGE_CRITERIA: list[str] = ["Fluency", "Grammar", "Tone", "Length", "Grounding"]
PROGRAMMATIC_CRITERIA: list[str] = ["Latency", "Cost"]

RUBRIC: dict[str, dict[str, str]] = {
    "Fluency": {
        "good": (
            "Reads naturally with smooth sentence flow; no awkward phrasing. "
            "A native speaker would find nothing jarring."
        ),
        "ok": (
            "Minor awkwardness — 1–2 clunky phrases — but the text is still "
            "easy to understand overall."
        ),
        "bad": (
            "Choppy, hard to follow, or incoherent sentences. The reader has "
            "to re-read to understand the meaning."
        ),
    },
    "Grammar": {
        "good": "Zero spelling or punctuation errors.",
        "ok": (
            "1–2 minor errors (e.g., a missing comma or minor typo) that do "
            "not change meaning or impede understanding."
        ),
        "bad": (
            "3 or more errors, OR any error that changes meaning or "
            "significantly impedes comprehension."
        ),
    },
    "Tone": {
        "good": (
            "Friendly, persuasive, and professionally credible sales voice "
            "maintained consistently throughout the description."
        ),
        "ok": (
            "Mostly appropriate tone but inconsistent in places — e.g., "
            "shifts between overly formal and casual, or slightly too "
            "aggressive in one sentence."
        ),
        "bad": (
            "Wrong tone entirely — robotic, overly aggressive, sarcastic, "
            "or unprofessional. Does not sound like a product listing."
        ),
    },
    "Length": {
        "good": "50–90 words (inclusive).",
        "ok": "40–49 words OR 91–110 words.",
        "bad": "Fewer than 40 words OR more than 110 words.",
    },
    "Grounding": {
        "good": (
            "Every claim in the description is directly supported by the "
            "provided product information (name, attributes, material, "
            "warranty). No fabricated details."
        ),
        "ok": (
            "Contains minor extrapolation that is reasonable and plausible "
            "but not explicitly stated in the input data (e.g., calling a "
            "wooden table 'eco-friendly')."
        ),
        "bad": (
            "Contains fabricated features, specifications, or claims that "
            "are not present in — and cannot be reasonably inferred from — "
            "the provided product information."
        ),
    },
    "Latency": {
        "good": "≤ 2 seconds per API call (end-to-end).",
        "ok": "Between 2 and 5 seconds per API call.",
        "bad": "More than 5 seconds per API call.",
    },
    "Cost": {
        "good": "≤ $0.001 per API call.",
        "ok": "Between $0.001 and $0.005 per API call.",
        "bad": "More than $0.005 per API call.",
    },
}

SYSTEM_PROMPT = """You are an e-commerce copywriter. Write a persuasive product description.

Rules:
- Length: exactly 50 to 90 words. Count carefully.
- Use ONLY the product information provided. Do not invent features, specs, or claims.
- Tone: friendly, confident, and professional. Write as if for a product listing page.
- Highlight key features and materials that matter to buyers.
- Mention the warranty naturally if it adds value.
- Do not include headings, bullet points, or markdown. Output only the description text."""

# If any of these is "bad", the description auto-fails.
GO_NO_GO_CRITERIA: list[str] = ["Grounding", "Length"]

MIN_GOOD_COUNT: int = 4  # at least this many "good" to pass
MAX_BAD_COUNT: int = 1   # at most this many "bad" to pass


def final_score(ratings: dict[str, Rating]) -> str:
    """Return 'pass' or 'fail' for a single product description."""
    for criterion in GO_NO_GO_CRITERIA:
        if ratings.get(criterion) == "bad":
            return "fail"

    count_good = sum(1 for v in ratings.values() if v == "good")
    count_bad = sum(1 for v in ratings.values() if v == "bad")

    if count_good >= MIN_GOOD_COUNT and count_bad <= MAX_BAD_COUNT:
        return "pass"

    return "fail"
