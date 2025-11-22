import sys

# Check if 5 marks are provided
if len(sys.argv) != 6:
    print("Usage: python program.py mark1 mark2 mark3 mark4 mark5")
    sys.exit(1)

# Accept marks from command-line arguments
marks = [float(arg) for arg in sys.argv[1:6]]

# Calculate average
average = sum(marks) / len(marks)

# Determine grade
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "Fail"

# Print results
print("\n--- Result ---")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
