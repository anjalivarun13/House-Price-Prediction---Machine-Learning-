## 🏠 House Price Prediction Model

This project predicts house prices using **Machine Learning Regression Models**.  
After evaluating multiple models (Linear, Lasso, Ridge), the **Ridge Regression model** performed the best and was selected as the final model.  
The model is saved using **pickle**, and a simple **Flask web app** is used to deliver real-time predictions.

---

## 🖼️ Website Preview

### **Before Prediction**
![Website Before](images/before.png)

### **After Prediction**
![Website After](images/after.png)

---

## 📊 Dataset Overview

### **Original Dataset Columns**
- `area_type`
- `availability`
- `location`
- `size`
- `society`
- `total_sqft`
- `bath`
- `balcony`
- `price`

### **Cleaned Dataset Columns**
- `location`
- `total_sqft`
- `bath`
- `price`
- `bhk`

---

## 🧹 Data Cleaning & Preprocessing

The dataset required multiple cleaning and transformation steps to improve accuracy and model performance.

---

### ✔ Dropped Unnecessary Columns and null values

These columns were removed as they do not add predictive value:

- **area_type** → Too many categories, low price impact  
- **availability** → Irrelevant for price prediction  
- **society** → Excessive unique values + many missing entries  
- **balcony** → Very weak correlation with price  

Removing these reduced noise and improved model accuracy.

---

### ✔ Extracted BHK From Size Column

The `size` column contained mixed text values like:

- "2 BHK"
- "4 Bedroom"
- "3 BHK"

To standardize:

- Removed `"BHK"` and `"Bedroom"`
- Extracted only the numeric value
- Saved in a new column `bhk`

This allows the model to learn properly from bedroom count.

---

### ✔ Location Cleanup

- The dataset originally had **1294 unique locations**.
- Locations that appeared **less than 10 times** were grouped into a single category **"others"**.
- This reduces sparse categories and improves model performance.

---

## 🧠 Machine Learning Models

Three regression models were trained:

| Model              | R² Score |
|-------------------|----------|
| **Linear Regression** | 0.8251977016 |
| **Lasso Regression**  | 0.8146894751 |
| **Ridge Regression**  | **0.8252348502** |

➡ **Final Model Used:** **Ridge Regression**  
Saved using **pickle** for deployment with Flask.

---

## 🖥️ Project Structure

    ├── static/
    │ ├── style.css
    ├── templates/
    │ ├── index.html
    ├── models/
    │ ├── house_price_ridge_model.pkl
    ├── data/
    │ ├── raw_dataset.csv
    │ ├── cleaned_dataset.csv
    ├── House Price Analysis.ipynb
    ├── application.py
    ├── README.md

---

## 🚀 Flask Web Application

The Flask app serves a clean interface to make predictions based on user inputs.

### **How It Works**
    1. User enters house details  
    2. Flask collects and validates the input  
    3. Pickle model loads Ridge Regression  
    4. Prediction is calculated  
    5. Output is shown on the webpage

### ▶ Run the Application

    python app.py

### Now open:

    http://127.0.0.1:5000

## 📦 Installation
1️⃣ Clone the Repository

    git clone https://github.com/your-username/house-price-prediction.git
    cd house-price-prediction

2️⃣ Install Dependencies

    pip install -r requirements.txt 

3️⃣ Run the Flask App

    python app.py

## 🧪 Example Prediction Input

    Location: Whitefield
    Total Sqft: 1200
    BHK: 3
    Bath: 2

### Output Example
    Predicted Price: ₹78.64 Lakhs

### ✅ Conclusion

This project demonstrates how machine learning can effectively predict house prices using well-cleaned data and regression models. Proper feature engineering, handling of outliers, and model selection resulted in a reliable and accurate prediction system that reflects real housing market patterns.

### 👩‍💻 Author

Anjali Varun

🔗 LinkedIn |🔗 GitHub