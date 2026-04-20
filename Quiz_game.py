questions = ("How many planets are there in our solar system?: ", 
            "What's the hottest planet in our solar system?: ",
            "What's the biggest planet in our solar system?: ",
            "What's the name of the probe sent into space in 1977?: ",
            "What planet is known as 'The Red Planet'?: ")
options = (("A. 5", "B. 6", "C. 7", "D. 8"),
           ("A. Mars", "B. Jupiter", "C. Venus", "D. Neptune"),
           ("A. Jupiter", "B. Saturn", "C. Europa", "D. Pandora"),
           ("A. Voyager 2", "B. Cassini-Huygens", "C. Mariner 10", "D. Voyager 1"),
           ("A. Venus", "B. Mars", "C. Earth", "D. Jupiter"))
answers = ("D", "C", "A", "D", "B")
score = 0
question_num = 0

for question in questions:
    print("-----------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    for answer in answers[question_num]:
        b=(input("Answer: ")).upper()
        if b == answer:
            score+=10
            print()
            print("Correct!")
        else:
            print("Incorrect!")
            print(f"{answer} is the correct answer!")
    question_num+=1
    print()

print("--------------------")
print(f"Total score: {score}points")