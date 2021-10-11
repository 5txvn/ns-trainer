import random

def main():
    number = random.randint(0, 30)

    print("What is the " + str(number) + " triangular number?")

    answer = input("Answer: ")

    if answer == str((number * (number + 1)) // 2):
        print("Correct!")
    else:
        print("Incorrect, the correct answer was " + str((number * (number + 1)) // 2))
    
    main()

main()