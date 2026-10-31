import pytest
from planner import calculate_plan

sample = {"age": 22, "height": 165, "weight": 60, "gender": "female",
          "activity": "moderate", "goal": "maintain"}

def test_calculates_bmi_and_calories():
    result = calculate_plan(sample)
    assert result["bmi"] > 0
    assert result["target_calories"] > 0

def test_returns_four_meals():
    assert len(calculate_plan(sample)["meals"]) == 4

def test_weight_loss_target_is_lower():
    maintain = calculate_plan(sample)
    lose = calculate_plan({**sample, "goal": "lose"})
    assert lose["target_calories"] < maintain["target_calories"]

def test_rejects_invalid_height():
    with pytest.raises(ValueError):
        calculate_plan({**sample, "height": 20})
