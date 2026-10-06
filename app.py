from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load model
model = joblib.load("nutrition_recommendation_model.pkl")
label_encoder = joblib.load("meal_plan_label_encoder.pkl")

# Load dataset for dropdown values
df = pd.read_csv("dataset.csv")

def get_unique_values(column):
    return sorted(df[column].dropna().unique().tolist())

dropdown_values = {
    "Gender": get_unique_values("Gender"),
    "Dietary_Habits": get_unique_values("Dietary_Habits"),
    "Preferred_Cuisine": get_unique_values("Preferred_Cuisine"),
    "Food_Aversions": get_unique_values("Food_Aversions"),
    "Chronic_Disease": get_unique_values("Chronic_Disease")
}

FEATURE_COLUMNS = [
    "Age", "Gender", "Height_cm", "Weight_kg", "BMI",
    "Chronic_Disease", "Blood_Pressure_Systolic",
    "Blood_Pressure_Diastolic", "Cholesterol_Level",
    "Blood_Sugar_Level", "Genetic_Risk_Factor", "Allergies",
    "Daily_Steps", "Exercise_Frequency", "Sleep_Hours",
    "Alcohol_Consumption", "Smoking_Habit", "Dietary_Habits",
    "Caloric_Intake", "Protein_Intake", "Carbohydrate_Intake",
    "Fat_Intake", "Preferred_Cuisine", "Food_Aversions"
]

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    nutrition = None
    explanation = None

    if request.method == "POST":
        data = {}

        numeric_cols = [
            "Age", "Height_cm", "Weight_kg", "BMI",
            "Blood_Pressure_Systolic", "Blood_Pressure_Diastolic",
            "Cholesterol_Level", "Blood_Sugar_Level",
            "Daily_Steps", "Exercise_Frequency", "Sleep_Hours",
            "Caloric_Intake", "Protein_Intake",
            "Carbohydrate_Intake", "Fat_Intake"
        ]

        for col in FEATURE_COLUMNS:
            value = request.form.get(col)

            if col in numeric_cols:
                value = float(value) if value else 0.0
            else:
                value = value if value else "Unknown"

            data[col] = value

        input_df = pd.DataFrame([data])
        pred = model.predict(input_df)[0]
        prediction = label_encoder.inverse_transform([pred])[0]

        nutrition = {
            "calories": data["Caloric_Intake"],
            "protein": data["Protein_Intake"],
            "carbs": data["Carbohydrate_Intake"],
            "fat": data["Fat_Intake"]
        }

        explanation = (
            f"The recommended meal plan is **{prediction}**. "
            f"This recommendation considers your BMI ({data['BMI']}), "
            f"chronic condition ({data['Chronic_Disease']}), and lifestyle habits. "
            f"Balanced protein helps muscle maintenance, while controlled carbs and fats "
            f"support metabolic health."
        )

    return render_template(
        "index.html",
        prediction=prediction,
        nutrition=nutrition,
        explanation=explanation,
        form_data=request.form,
        dropdowns=dropdown_values
    )

if __name__ == "__main__":
    app.run(debug=True)
