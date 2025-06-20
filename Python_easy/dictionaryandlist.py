'''You are given a dictionary where the keys are names and the values are lists of scores. Your task is to:

Print the scores of the student named "Alice".

Add a new score 85 to Alice's list of scores.

Print the updated dictionary.'''

student_scores = {
    "Alice": [90, 95, 88],
    "Bob": [78, 82, 80],
    "Charlie": [92, 89, 94]
}

# Your code here

Alice_scores=student_scores["Alice"]
print(Alice_scores)

student_scores["Alice"].append(85)
print(student_scores)
