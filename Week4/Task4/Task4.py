import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Defining the number of rows
num_of_rows = 200

# Generating same random data
np.random.seed(10)

# Generating random data
subject = np.random.choice(["Maths", "Computer", "English", "Urdu", "Science"], num_of_rows)
score = np.random.randint(0, 100, num_of_rows)
total_marks = 100

# Generating dataset
exam_data = pd.DataFrame({
    'Student ID': [f'ID{i}' for i in range(1, num_of_rows + 1)],
    'Name': [f'Name{i}' for i in range(1, num_of_rows + 1)],
    'Subject': subject,
    'Score': score,
    'Total Marks': total_marks
})

# Displays the exam data
print(exam_data.head(10))

# Converting score column to array
score_array = exam_data['Score'].to_numpy()
score_mean = np.mean(score_array)
score_median = np.median(score_array)
score_std_dev = np.std(score_array)

# Displays the mean, median and standard deviation of the scores
print("Mean of the score: ", score_mean)
print("Median of the score: ", score_median)
print("Standard Deviation of the score: ", score_std_dev)
# Filtering the data by exam score
filtered_data = exam_data[exam_data['Score'] > 80]
total_students = len(filtered_data)

# Displays the number of students who achieved a score above 80%
print("Number of students who achieved score above 80%: ", total_students)

# Grouping the data by subjects
avg_score = exam_data.groupby('Subject')['Score'].mean()

# Displays the average score of the subjects
print("Average score of the subjects: \n", avg_score)

# Plotting a histogram to show the distribution of scores
plt.figure(figsize=(10, 6))
plt.hist(exam_data['Score'], bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.title('Distribution of Scores Across All Students', fontsize=16)
plt.xlabel('Scores', fontsize=12)
plt.ylabel('Number of Students', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()

# Plotting a bar chart to compare the average scores across different subjects
plt.figure(figsize=(10, 6))
avg_score.plot(kind='bar', color='orange', edgecolor='black')
plt.title('Average Scores by Subject', fontsize=16)
plt.xlabel('Subject', fontsize=12)
plt.ylabel('Average Score', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
