# 📊 Data Analysis Project: Custom Dataset & Titanic Dataset

## 🧾 Overview

This project demonstrates fundamental data analysis skills using **Python (Pandas)**. It is divided into two main parts:

* **Part 1:** Creating a custom dataset using a dictionary
* **Part 2:** Performing real-world data analysis on the Titanic Dataset Kaggle YasserH

The project covers data creation, exploration, cleaning, analysis, and insights.

---

# 🧩 Part 1: Custom Dataset Creation

## 🎯 Objective

To build a structured dataset manually using a Python dictionary and convert it into a Pandas DataFrame.

## 🛠️ Tasks Performed

* Created a dataset with:

  * **5 columns (features)**: Name, Age, Gender, Score, Department
  * **15 rows (records)**
* Assigned a **custom index** (ID_1 to ID_15)
* Converted dictionary → Pandas DataFrame

## 📌 Key Concepts Used

* `pd.DataFrame()`
* Custom indexing
* Structured data representation

---

# 🚢 Part 2: Titanic Dataset Analysis

## 🎯 Objective

To perform real-world data analysis including:

* Data exploration
* Data cleaning
* Group-based analysis

## 📂 Dataset

* Source: Kaggle
* File used: `Titanic-Dataset.csv`

---

## 🔍 Step 1: Data Exploration

Performed initial inspection using:

* `.head()` → Preview dataset
* `.info()` → Data types & missing values
* `.describe()` → Statistical summary

---

## 🧹 Step 2: Data Cleaning

Handled missing values and inconsistencies:

* **Age column** → filled with median
* **Embarked column** → filled with mode
* **Cabin column** → dropped due to excessive missing values
* Removed duplicate rows

✅ Result: Clean and consistent dataset ready for analysis

---

## 📊 Step 3: Data Analysis

### Survival Rate by Gender

Used `groupby()` to analyze survival patterns:

* Grouped data by `Sex`
* Calculated mean of `Survived`

### 📌 Key Finding:

* **Females had a significantly higher survival rate than males**

---

# 🧠 Insights

* **Gender Impact:**
  Females were more likely to survive than males

* **Data Quality:**
  Handling missing values improved analysis accuracy

* **Real-world relevance:**
  Demonstrates how data cleaning and grouping reveal meaningful patterns

---

# ⚙️ Tools & Technologies

* Python
* Pandas

---

# ✅ Conclusion

This project successfully demonstrates:

* Creating structured datasets
* Cleaning real-world data
* Performing meaningful analysis using Pandas

It highlights the importance of preprocessing and exploratory data analysis in data science workflows.

---

# 🚀 Future Improvements

* Add data visualization (Matplotlib / Seaborn)
* Perform machine learning predictions
* Expand analysis with more features

---
