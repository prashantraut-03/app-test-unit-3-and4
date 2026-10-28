import pandas as pd

data = {
    "Name": ["Rahul", "Amit", "Priya", "Sneha"],
    "Department": ["IT", "HR", "IT", "HR"],
    "Salary": [30000, 25000, 40000, 35000]
}

df = pd.DataFrame(data)

print("Employee Details:")
print(df)

print("\nAverage Salary by Department:")
print(df.groupby("Department")["Salary"].mean())
