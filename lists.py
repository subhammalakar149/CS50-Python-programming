# finding the average of numbers using a list
"""
scores = [72, 73, 33]

average = sum(scores)/len(scores)
print(f"The average is : {average}")

"""

scores = []
for i in range(3):
    score = int(input("Scores: "))
    scores.append(score)

average = sum(scores)/len(scores)
print(f"The average is: {average}")
