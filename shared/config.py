"""Project-wide configuration."""

from __future__ import annotations

import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ACADEMY_ROOT = PROJECT_ROOT.parent
DATASET_PATH = ACADEMY_ROOT / "Assignment_01_product_dataset.xlsx"
OUTPUT_EXCEL = PROJECT_ROOT / "task_3" / "assignment_01.xlsx"

NEBIUS_API_KEY = os.environ.get("NEBIUS_API_KEY", "")
NEBIUS_BASE_URL = "https://api.tokenfactory.nebius.com/v1/"

GENERATION_MODEL = os.environ.get("NEBIUS_GENERATION_MODEL_ID", "google/gemma-2-9b-it")
JUDGE_MODEL = os.environ.get("NEBIUS_JUDGE_MODEL_ID", "meta-llama/Meta-Llama-3.1-8B-Instruct")

# USD per 1K tokens — update if pricing changes
PRICING: dict[str, dict[str, float]] = {
    GENERATION_MODEL: {"input": 0.0002, "output": 0.0002},
    JUDGE_MODEL: {"input": 0.0002, "output": 0.0002},
}
