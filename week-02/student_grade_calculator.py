# Smart Student Grade Calculator

# Collect Student Scores
test_score = float(input("Enter your test score (out of 20): "))
assignment_score = float(input("Enter your assignment score (out of 30): "))
exam_score = float(input("Enter your exam score (out of 50): "))

# Calculate total and average
total_score = test_score + assignment_score + exam_score
average_score = (total_score / 3) * 100

# Display scores
print("\n---- Student Result ----")
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score: .2f}")

# Check if passed or failed
if total_score >= 50:
    print("Status: PASSED")
else:
    print("Status: FAILED")
    
# Check award qualification
if average_score >= 70 and test_score >= 15 and assignment_score >= 25 and exam_score >= 45:
    print("Award Status: QUALIFIES FOR AWARD")
else:
    print("Award Status: DOES NOT QUALIFY FOR AWARD")