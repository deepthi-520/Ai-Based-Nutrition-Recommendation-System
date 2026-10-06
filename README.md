# AI-Based Nutrition Recommendation System

## 📌 Overview

The **AI-Based Nutrition Recommendation System** is a machine learning-based web application that provides personalized nutrition and meal recommendations based on individual health and lifestyle information.

The system analyzes user details such as **age, height, weight, BMI, lifestyle habits, and health conditions** and uses a machine learning model to recommend a suitable meal plan.

This project is developed as an academic project to demonstrate the use of **Artificial Intelligence, Machine Learning, Python, Flask, Pandas, NumPy, and Scikit-learn** in personalized nutrition recommendation.

---

## 🎯 Objectives

The main objectives of the project are:

* To provide personalized nutrition recommendations.
* To analyze individual health and lifestyle information.
* To recommend suitable meal plans based on user information.
* To use machine learning for nutrition recommendation.
* To provide an easy-to-use web interface.
* To support personalized diet planning.
* To allow recommendations to be updated when user information changes.

---

## ✨ Features

* 👤 User health information input
* 📊 BMI-based analysis
* 🧠 Machine learning-based recommendation
* 🥗 Personalized meal plan recommendation
* 🌐 Web-based user interface
* ⚡ Fast prediction
* 🔄 Recommendations based on updated user information
* 📱 Potential for future mobile application integration

---

## 🤖 Machine Learning Algorithm

### Gradient Boosting Classifier

The project uses a **Gradient Boosting Classifier** for generating nutrition recommendations.

Gradient Boosting combines multiple decision trees to improve prediction performance. Each new tree attempts to correct the errors made by the previous trees.

### Why Gradient Boosting?

Gradient Boosting is suitable for this project because:

* It can handle complex relationships between input features.
* It combines multiple decision trees.
* It improves predictions by learning from previous errors.
* It can work with different types of health-related input data.

---

## 🔄 Project Methodology

The project follows the following steps:

### 1. Data Collection

The system uses a dataset containing information required for generating nutrition recommendations.

### 2. Data Preprocessing

The collected data is processed and prepared for machine learning.

This includes:

* Handling input data
* Preparing features
* Encoding categorical information
* Preparing data for model training

### 3. Model Training

The processed dataset is used to train the **Gradient Boosting Classifier**.

The trained model is saved and used later for prediction.

### 4. Prediction

When a user enters their health information, the trained model analyzes the input and predicts a suitable meal plan.

### 5. Web Application

The Flask web application provides an interface through which users can enter their information and view the recommended meal plan.

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Gradient Boosting Classifier

### Data Processing

* Pandas
* NumPy

### Web Framework

* Flask

### Frontend

* HTML
* CSS

### Development Tools

* Visual Studio Code
* Jupyter Notebook

---

## 📁 Project Structure

```text
Ai-Based-Nutrition-Recommendation-System/
│
├── app.py
├── train.py
├── predict.py
├── dataset.csv
├── nutrition_recommendation_model.pkl
├── meal_plan_label_encoder.pkl
├── requirements.txt
├── ppt nutrition.pptx
│
├── static/
│   └── style.css
│
└── templates/
    └── index.html
```

---

## 📄 File Description

| File                                 | Description                                          |
| ------------------------------------ | ---------------------------------------------------- |
| `app.py`                             | Flask application that runs the web interface        |
| `train.py`                           | Used for training the machine learning model         |
| `predict.py`                         | Used for making predictions                          |
| `dataset.csv`                        | Dataset used for the nutrition recommendation system |
| `nutrition_recommendation_model.pkl` | Trained machine learning model                       |
| `meal_plan_label_encoder.pkl`        | Label encoder used for meal plan prediction          |
| `requirements.txt`                   | Python dependencies required for the project         |
| `static/style.css`                   | CSS file for styling the web application             |
| `templates/index.html`               | HTML page for the user interface                     |
| `ppt nutrition.pptx`                 | Project presentation                                 |

---

## ⚙️ Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/deepthi-520/Ai-Based-Nutrition-Recommendation-System.git
```

### Step 2: Open the Project Folder

```bash
cd Ai-Based-Nutrition-Recommendation-System
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Step 5: Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

After installing the required packages, run:

```bash
python app.py
```

The Flask application will start.

Open the local URL displayed in the terminal in your web browser.

---

## 🔁 System Workflow

The system works according to the following workflow:

```text
User
  ↓
Enter Health Information
  ↓
Data Processing
  ↓
Machine Learning Model
  ↓
Health Data Analysis
  ↓
Meal Plan Prediction
  ↓
Personalized Nutrition Recommendation
  ↓
Display Result
```

---

## 👤 User Input

The system considers user information such as:

* Age
* Height
* Weight
* BMI
* Lifestyle habits
* Health conditions

This information is processed by the system before generating the recommendation.

---

## 🥗 Nutrition Recommendation

After processing the user's information, the machine learning model predicts a suitable meal plan.

The purpose is to provide a more personalized recommendation instead of providing the same diet plan to every user.

For example:

* Users interested in weight management may require different meal recommendations.
* Users with specific health conditions may require different food recommendations.
* Users with different lifestyles may receive different recommendations.

---

## 🌐 Web Application

The project provides a simple web interface where users can:

1. Enter their personal information.
2. Provide health-related information.
3. Submit the information.
4. Get a personalized meal plan recommendation.

---

## ✅ Advantages

The proposed system provides the following advantages:

* **Personalized Recommendations**
  Recommendations are based on individual user information.

* **Machine Learning Based**
  Uses a machine learning model to generate predictions.

* **Easy to Use**
  Provides a simple web interface.

* **Real-Time Recommendations**
  The system can generate a recommendation based on the information entered by the user.

* **Scalable**
  The system can potentially support recommendations for many users.

---

## 🏥 Applications

The system can be applied in several areas:

### Healthcare

Hospitals and healthcare organizations can use personalized nutrition systems to support diet planning.

### Fitness and Wellness

Fitness and wellness platforms can use personalized meal recommendations.

### Diet Planning

The system can assist users in planning their diet according to their health information.

### Personal Health Management

Users can use the system as a tool for understanding personalized nutrition recommendations.

### Health Applications

The system can potentially be integrated into health and fitness mobile applications.

---

## ⚠️ Limitations

* The system depends on the quality of the dataset.
* Recommendations are limited by the information available in the training data.
* The system should not replace professional medical or dietary advice.
* More extensive real-world health data could improve the system.
* The current system is primarily implemented as a web application.

---

## 🚀 Future Scope

The project can be enhanced in the future by adding:

* Deep learning models
* Integration with fitness bands
* Integration with smartwatches
* Real-time health monitoring
* Mobile application support
* User feedback systems
* More comprehensive health datasets
* More personalized recommendations

---

## 📚 Project References

The project report references research and resources related to:

* Artificial Intelligence in nutrition
* Personalized nutrition recommendation
* Machine learning-based diet planning
* AI-based health applications

---

## 👩‍💻 Team Members

**Department:** Computer Science and Engineering

### Team

* A. Bhavya
* J. Vaishnavi
* B. Deepthi
* E. Shirisha

### Project Guide

**Dr. N. Sreelatha, M.Tech**
Associate Professor

---

## 📌 Conclusion

The **AI-Based Nutrition Recommendation System** demonstrates how Artificial Intelligence and Machine Learning can be applied to personalized nutrition planning.

By analyzing user information such as age, height, weight, BMI, lifestyle habits, and health conditions, the system provides a suitable meal plan recommendation.

The project combines **Python, Flask, Pandas, NumPy, and Scikit-learn** to create a machine learning-based web application.

The system can be further improved by integrating deep learning, wearable devices, real-time health monitoring, mobile applications, and user feedback.

---

## ⚠️ Disclaimer

This project is developed for **academic and educational purposes**.

The recommendations generated by this system should not be considered professional medical or dietary advice. Users should consult a qualified healthcare professional or registered dietitian for medical or personalized dietary decisions.

---

## 🔗 GitHub Repository

[AI-Based Nutrition Recommendation System](https://github.com/deepthi-520/Ai-Based-Nutrition-Recommendation-System)
