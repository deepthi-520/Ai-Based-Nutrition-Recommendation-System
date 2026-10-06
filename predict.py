import tkinter as tk
from tkinter import messagebox
import pandas as pd
import joblib

model = joblib.load("nutrition_recommendation_model.pkl")
label_encoder = joblib.load("meal_plan_label_encoder.pkl")

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

DEFAULT_VALUES = {
    "Age": "28",
    "Gender": "Other",
    "Height_cm": "164",
    "Weight_kg": "93",
    "BMI": "34.58",
    "Chronic_Disease": "Diabetes",
    "Blood_Pressure_Systolic": "104",
    "Blood_Pressure_Diastolic": "100",
    "Cholesterol_Level": "187",
    "Blood_Sugar_Level": "232",
    "Genetic_Risk_Factor": "No",
    "Allergies": "Nut Allergy",
    "Daily_Steps": "7328",
    "Exercise_Frequency": "2",
    "Sleep_Hours": "9.5",
    "Alcohol_Consumption": "No",
    "Smoking_Habit": "No",
    "Dietary_Habits": "Keto",
    "Caloric_Intake": "1769",
    "Protein_Intake": "111",
    "Carbohydrate_Intake": "102",
    "Fat_Intake": "50",
    "Preferred_Cuisine": "Asian",
    "Food_Aversions": "Salty"
}

root = tk.Tk()
root.title("AI Nutrition Recommendation System")
root.geometry("800x700")

canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
container = tk.Frame(canvas)

container.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=container, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

form_frame = tk.Frame(container)
form_frame.pack(padx=10, pady=10, fill="x")

mid = len(FEATURE_COLUMNS) // 2
LEFT_COLS = FEATURE_COLUMNS[:mid]
RIGHT_COLS = FEATURE_COLUMNS[mid:]

left_frame = tk.Frame(form_frame)
right_frame = tk.Frame(form_frame)

left_frame.grid(row=0, column=0, padx=10, sticky="n")
right_frame.grid(row=0, column=1, padx=10, sticky="n")

entries = {}

def create_fields(frame, columns):
    for col in columns:
        row = tk.Frame(frame)
        row.pack(fill="x", pady=4)

        label = tk.Label(row, text=col, width=25, anchor="w")
        label.pack(side="left")

        entry = tk.Entry(row)
        entry.pack(side="right", fill="x", expand=True)

        if col in DEFAULT_VALUES:
            entry.insert(0, DEFAULT_VALUES[col])

        entries[col] = entry

create_fields(left_frame, LEFT_COLS)
create_fields(right_frame, RIGHT_COLS)

def predict_meal_plan():
    try:
        data = {}

        for col, entry in entries.items():
            val = entry.get().strip()
            if val == "":
                messagebox.showerror("Input Error", f"Enter value for {col}")
                return

            if col in [
                "Age", "Height_cm", "Weight_kg", "BMI",
                "Blood_Pressure_Systolic", "Blood_Pressure_Diastolic",
                "Cholesterol_Level", "Blood_Sugar_Level",
                "Daily_Steps", "Exercise_Frequency",
                "Caloric_Intake", "Protein_Intake",
                "Carbohydrate_Intake", "Fat_Intake"
            ]:
                val = float(val)

            data[col] = val

        input_df = pd.DataFrame([data])
        pred = model.predict(input_df)[0]
        result = label_encoder.inverse_transform([pred])[0]

        messagebox.showinfo(
            "Prediction Result",
            f"Recommended Meal Plan:\n\n{result}"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))

submit_btn = tk.Button(
    container,
    text="Submit / Predict Meal Plan",
    command=predict_meal_plan,
    bg="green",
    fg="white",
    height=2,
    width=30
)
submit_btn.pack(pady=20)

root.mainloop()
