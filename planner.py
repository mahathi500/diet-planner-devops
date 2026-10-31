def calculate_plan(data):
    age, height, weight = data["age"], data["height"], data["weight"]
    if not (15 <= age <= 100 and 100 <= height <= 230 and 25 <= weight <= 300):
        raise ValueError("Input outside demo range")
    bmr = 10*weight + 6.25*height - 5*age + (5 if data["gender"] == "male" else -161)
    factor = {"sedentary": 1.2, "light": 1.375, "moderate": 1.55, "active": 1.725}[data["activity"]]
    maintenance = bmr * factor
    adjustment = {"lose": -300, "maintain": 0, "gain": 250}[data["goal"]]
    bmi = weight / ((height/100)**2)
    category = ("Below the usual adult reference range" if bmi < 18.5 else
                "Within the usual adult reference range" if bmi < 25 else
                "Above the usual adult reference range" if bmi < 30 else
                "In a higher adult BMI range")
    meals = [
        ("Breakfast", "Oats with milk or curd, fruit and a handful of nuts"),
        ("Lunch", "Rice or roti, dal, vegetables and curd"),
        ("Snack", "Seasonal fruit, sprouts or roasted chana"),
        ("Dinner", "Roti or rice with paneer, tofu or dal and vegetables")]
    return {"bmi": round(bmi, 1), "bmi_category": category,
            "maintenance_calories": round(maintenance),
            "target_calories": round(maintenance + adjustment),
            "meals": meals}
