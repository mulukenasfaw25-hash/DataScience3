import pandas as pd

# =========================
# Load Dataset
# =========================
df = pd.read_csv("Titanic-Dataset.csv")

# =========================
# STEP 1: EXPLORATION
# =========================
print("===== HEAD =====")
print(df.head())

print("\n===== INFO =====")
print(df.info())

print("\n===== DESCRIBE =====")
print(df.describe())

# =========================
# STEP 2: DATA CLEANING
# =========================

# Handle missing values

# Age → median
df['Age'].fillna(df['Age'].median(), inplace=True)

# Embarked → mode
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Cabin → drop
df.drop(columns=['Cabin'], inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

print("\n===== AFTER CLEANING =====")
print(df.isnull().sum())   # check missing values

# =========================
# STEP 3: DATA ANALYSIS
# =========================

# Survival rate by gender
survival_gender = df.groupby('Sex')['Survived'].mean()

print("\n===== SURVIVAL RATE BY GENDER =====")
print(survival_gender)