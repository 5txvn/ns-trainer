import random

def main():

    number1 = random.randint(10, 100)
    number2 = random.randint(10, 100)

    print(str(number1) + " + " + str(number2) + " = ?")

    answer = input("Answer: ")

    if (str(number1 + number2) == answer):
        print("Correct!")
    else:
        print("Incorrect, the correct answer was " + str(number1 + number2))

    main()

main()