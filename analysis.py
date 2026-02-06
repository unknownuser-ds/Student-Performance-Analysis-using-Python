import pandas as pd

# Load data
data = pd.read_csv("student_marks.csv")

# Create Total and Average columns
data['Total'] = data['Maths'] + data['Physics'] + data['Chemistry']
data['Average'] = data['Total'] / 3

# Find topper
topper = data.loc[data['Total'].idxmax()]

# Sort students by total marks
sorted_students = data.sort_values(by='Total', ascending=False)

# Print class summary
print("\n📊 CLASS SUMMARY")
print("----------------")
print(f"Average Maths: {data['Maths'].mean():.2f}")
print(f"Average Physics: {data['Physics'].mean():.2f}")
print(f"Average Chemistry: {data['Chemistry'].mean():.2f}")

print("\n🏆 TOPPER")
print("---------")
print(f"Name: {topper['Name']}")
print(f"Total Marks: {topper['Total']}")
print(f"Average: {topper['Average']:.2f}")

# Save ranked results
sorted_students.to_csv("ranked_students.csv", index=False)

print("\n✅ Ranked student list saved as 'ranked_students.csv'")
