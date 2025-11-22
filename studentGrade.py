import sys


if len(sys.argv) != 6:
    print("Usage: python program.py mark1 mark2 mark3 mark4 mark5")
    sys.exit(1)
script_name=sys.argv[0]
mark1=sys.argv[1]
mark2=sys.argv[2]
mark3=sys.argv[2]
mark4=sys.argv[2]
mark5=sys.argv[2]

average = mark1+mark2+mark3+mark4+mark5/5


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


print("\n--- Result ---")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")


