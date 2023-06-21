import random
def get_level():
    while True:
        try:
            level = int(input("Enter level 1, 2, 3:"))
        except ValueError:
            continue
        if level < 1 or level > 3:
            print("Error: Invalid input.")
            continue
        break
    print("")
    return level

def get_question_num():
    while True:
        try:
            questions = int(input("Enter number of questions to ask: 3 to 10: "))
        except ValueError:
            continue
        if questions < 3 or questions > 10:
            print("Error: Invalid input.")
            continue
        break
    print("")
    return questions

def ask_question(num1, num2, attempt):
    answer = input(f"{num1} + {num2} = ")
    if answer == str(num1+num2):
        print("Correct!\n")
        return True
    if attempt == 3:
        print(f"wrong!\nCorrect answer: {num1} + {num2} = {num1+num2}\n")
        return False
    print("Wrong!\n")
    return ask_question(num1, num2, attempt+1)

def main():
    level = get_level()
    questions = get_question_num()
    start = 0
    stop = 0
    correct = 0
    for i in range(questions):
        if level == 1:
            start = 0
            stop = 9
        elif level == 2:
            start = 10
            stop = 99
        elif level == 3:
            start = 100
            stop = 999
        num1 = random.randint(start, stop)
        num2 = random.randint(start, stop)
        if ask_question(num1, num2, 1):
            correct += 1
    print(f"You got {correct} out of {questions} correct: {(correct/questions*100):.2f}%")
main()
