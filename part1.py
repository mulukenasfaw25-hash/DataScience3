import pandas as pd

# Create dictionary
data = {
    "Name": ["Alem", "Bini", "Chala", "Dani", "Eden",
             "Fikir", "Girma", "Hana", "Ibrahim", "Jemal",
             "Kebede", "Liya", "Mahi", "Nati", "Oli"],
    
    "Age": [20, 22, 19, 21, 23, 24, 22, 20, 25, 23, 21, 22, 24, 23, 20],
    
    "Gender": ["F", "F", "M", "M", "F", "F", "M", "F", "M", "M", "M", "F", "F", "M", "F"],
    
    "Score": [85, 90, 78, 88, 92, 95, 80, 87, 76, 84, 79, 91, 89, 82, 86],
    
    "Department": ["IT", "CS", "Math", "IT", "CS", "Math", "IT", "CS", "Math", "IT",
                   "CS", "Math", "IT", "CS", "Math"]
}

# Custom index
index_labels = [f"ID_{i}" for i in range(1, 16)]

df_custom = pd.DataFrame(data, index=index_labels)

print(df_custom)