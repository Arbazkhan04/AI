import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#generating number of rows
num_of_rows = 300

#generating repeated data
np.random.seed(10)

#generating data for dataset
names = np.random.choice(["Aleena","Amina","Aqsa","Iqra","Sumbal","Merub","Mirha","Tehreem","Zaima","Hoorain",
                          "Mursal","Mushaf","Wali","Abdullah","Ghani","Abu trab","Irfana","Khushi","Ayesha","Arbaz"], size=num_of_rows)
department = np.random.choice(["Mathematics","IT","CS","Sociology","SE"], size=num_of_rows)
salary = np.random.randint(30000,120000, size=num_of_rows)
years_of_exp = np.random.randint(1,25, size=num_of_rows)

#generating dataset
Employee_data = pd.DataFrame({
    'Employee ID': [f'{i}' for i in range(1,num_of_rows+1)],
    'Names': names,
    'Department': department,
    'Salary': salary,
    'Years of Experience': years_of_exp
})

#displays the dataset
print(Employee_data.head(10))

#converting salary column to array
salary_array = Employee_data['Salary'].to_numpy()
avg_salary = int(np.mean(salary_array))
mini_salary = np.min(salary_array)
max_salary = np.max(salary_array)

print("Average Salary: ", avg_salary)
print("Minimum Salary: ", mini_salary)
print("Maximum Salary: ", max_salary)

#filtering the data on the basis of salary and years of experience
filtered_data = Employee_data[(Employee_data['Years of Experience'] > 5) & (Employee_data['Salary'] > avg_salary)]

#displays the filtered data
print(filtered_data[:10])

#grouping the data by department
mean_salary_department = Employee_data.groupby('Department')['Salary'].mean()

#displays the mean salary for each department
print("Mean Salary for each Department: \n", mean_salary_department)

# Bar plot showing average salary by department
plt.figure(figsize=(10, 6))
mean_salary_department.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Average Salary by Department', fontsize=16)
plt.xlabel('Department', fontsize=12)
plt.ylabel('Average Salary', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Line plot for salary distribution by years of experience
plt.figure(figsize=(10, 6))
Employee_data_sorted = Employee_data.sort_values(by='Years of Experience')
plt.plot(Employee_data_sorted['Years of Experience'], Employee_data_sorted['Salary'], marker='o', color='green', linestyle='-', markersize=5)
plt.title('Salary Distribution by Years of Experience', fontsize=16)
plt.xlabel('Years of Experience', fontsize=12)
plt.ylabel('Salary', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()

