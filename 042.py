"""Problem 042: Scholarship Eligibility : Determine eligibility based on marks, attendance, and family income."""

marks = float(input("Enter marks percentage: "))
attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter annual family income: "))
# Example criteria because the sheet does not specify exact thresholds.
if marks >= 85 and attendance >= 75 and income <= 250000:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")
