import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("Current Directory:")
print(os.getcwd())

print("\nFiles in Project Folder:")
print(os.listdir())

print("\nFiles in Data Folder:")
print(os.listdir("data"))

# Load Dataset
df = pd.read_csv("data/employee_salary_dataset.csv")

# Display First Rows
print("FIRST 5 ROWS")
print(df.head())

# Dataset Information
print("\nDATASET INFORMATION")
print(df.info())

# Missing Values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Statistical Summary
print("\nSTATISTICAL SUMMARY")
print(df.describe())

# Salary Statistics
print("\nSALARY ANALYSIS")
print("Average Salary:", round(df["Monthly_Salary"].mean(), 2))
print("Maximum Salary:", df["Monthly_Salary"].max())
print("Minimum Salary:", df["Monthly_Salary"].min())
print("Median Salary:", df["Monthly_Salary"].median())

# Department-wise Average Salary
print("\nAVERAGE SALARY BY DEPARTMENT")
print(df.groupby("Department")["Monthly_Salary"].mean())

# Gender-wise Average Salary
print("\nAVERAGE SALARY BY GENDER")
print(df.groupby("Gender")["Monthly_Salary"].mean())

# -------------------------
# BAR CHART
# -------------------------

avg_salary_department = (
    df.groupby("Department")["Monthly_Salary"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12,6))

bars = plt.bar(
    avg_salary_department.index,
    avg_salary_department.values,
    edgecolor="black"
)

plt.title("Average Monthly Salary by Department", fontsize=18, fontweight="bold")
plt.xlabel("Department", fontsize=12)
plt.ylabel("Average Salary (₹)", fontsize=12)

plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.5)

for bar in bars:
    y = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        y,
        f"{int(y):,}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig("images/bar_chart.png", dpi=300)
plt.close()

# -------------------------
# SCATTER PLOT
# -------------------------

plt.figure(figsize=(12,7))

sns.scatterplot(
    data=df,
    x="Experience_Years",
    y="Monthly_Salary",
    hue="Department",
    size="Age",
    sizes=(50,300)
)

plt.title(
    "Experience vs Salary by Department",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel("Years of Experience")
plt.ylabel("Monthly Salary (₹)")

plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("images/scatter_plot.png", dpi=300)
plt.close()

# -------------------------
# HEATMAP
# -------------------------

numeric_data = df.select_dtypes(include="number")

numeric_data = df.select_dtypes(include="number")

plt.figure(figsize=(10,8))

sns.heatmap(
    numeric_data.corr(),
    annot=True,
    fmt=".2f",
    linewidths=1,
    square=True,
    cmap="RdYlBu"
)

plt.title(
    "Employee Salary Correlation Matrix",
    fontsize=18,
    fontweight="bold"
)

plt.tight_layout()
plt.savefig("images/heatmap.png", dpi=300)
plt.close()

# -------------------------
# GENDER DISTRIBUTION
# -------------------------

gender_count = df["Gender"].value_counts()

plt.figure(figsize=(8,8))

plt.pie(
    gender_count,
    labels=gender_count.index,
    autopct="%1.1f%%",
    wedgeprops={"width":0.4}
)

plt.title(
    "Gender Distribution",
    fontsize=18,
    fontweight="bold"
)

plt.savefig("images/gender_distribution.png", dpi=300)
plt.close()

# -------------------------
# SALARY DISTRIBUTION
# -------------------------

plt.figure(figsize=(12,6))

sns.histplot(
    df["Monthly_Salary"],
    bins=10,
    kde=True
)

plt.title(
    "Salary Distribution",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel("Monthly Salary (₹)")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("images/salary_distribution.png", dpi=300)
plt.close()


print("\nPROJECT COMPLETED SUCCESSFULLY")
print("All charts created successfully:")