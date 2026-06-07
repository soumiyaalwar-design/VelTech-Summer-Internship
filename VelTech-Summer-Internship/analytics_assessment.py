import pandas as pd
# Create DataFrame
data = {
    'Candidate': ['Rahul', 'Priya', 'Ravi', 'Gowtham', 'Soumiya'],
    'A': [70, 68, 90, 45, 67],
    'B': [65, 88, 54, 78, 95],
    'C': [77, 63, 89, 96, 66],
    'D': [45, 66, 70, 67, 89],
    'E': [90, 99, 98, 89, 79]
}
df = pd.DataFrame(data)

# Question 1
highest_B = df.loc[df['B'].idxmax(), 'Candidate']
highest_B_marks = df['B'].max()
print("Highest scorer in Subject B:")
print(highest_B, "-", highest_B_marks)

# Question 2
avg_C = df['C'].mean()
print("\nAverage marks in Subject C:")
print(round(avg_C, 2))

# Question 3
df['Total'] = df[['A', 'B', 'C', 'D', 'E']].sum(axis=1)
df['Percentage'] = (df['Total'] / 500) * 100
highest_percentage = df.loc[df['Percentage'].idxmax()]
print("\nHighest Percentage:")
print(highest_percentage['Candidate'],
      "-", round(highest_percentage['Percentage'], 2), "%")

# Question 4
subjects = ['A', 'B', 'C', 'D', 'E']
df['Top4_Total'] = df[subjects].apply(
    lambda row: sum(sorted(row, reverse=True)[:4]),
    axis=1
)
df['Top4_Percentage'] = (df['Top4_Total'] / 400) * 100
highest_top4 = df.loc[df['Top4_Percentage'].idxmax()]
print("\nHighest Percentage considering Top 4 Subjects:")
print(highest_top4['Candidate'],
      "-", round(highest_top4['Top4_Percentage'], 2), "%")
