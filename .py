questions = [
    {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    {
        "question": "Who is the president of the United States?",
        "answer": "Joe Biden"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "answer": "Jupiter"
    }
]

def run_quiz():
    score = 0
    for question in questions:
        user_answer = input(question["question"] + " ")
        if user_answer.lower() == question["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print("Sorry, the correct answer is " + question["answer"])
    print("Your final score is " + str(score))

run_quiz()
