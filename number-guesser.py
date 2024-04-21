import random

print("\t\t\tWelcome Number Guessing Game")
print("You Will Get 5 Changes to Guess the Correct Numbner\nDon't Worry I will give hints to guess the correct ans")


low = 1
high = 50
attempt = 0
correct_answer = random.randrange(low,high)

while True:
    
    if attempt >= 5:
        print("\nYou LOSE")
        print(f"Correct Number : {correct_answer}")
        choice = input("\n\nDo you want to play again ?\n1. YES\t2. NO -> ")
        if choice == "1":
            correct_answer = random.randrange(low,high)
            attempt = 0
        elif choice == "2":
           exit ()
    

    elif attempt < 5:
        num = int(input("Enter Number: "))
        attempt += 1
        if num == correct_answer:
            print("\nYou Sucessfully Guess The Number")
            print(f"Correct Number : {correct_answer}")
            print(f"You Take {attempt} changes")
            choice = input("\n\nDo you want to play again ?\n1. YES\t2. NO -> ")
            if choice == "1":
                correct_answer = random.randrange(low,high)
                attempt = 0
            elif choice == "2":
                exit ()
        else:
            if attempt <= 4:
                if num > correct_answer:
                    print("Correct Number is smaller !")
                    print(f"Attempt {attempt} | Left {5-attempt}")
                elif num < correct_answer:
                    print("Correct Number is greater !")
                    print(f"Attempt {attempt} | Left {5-attempt}")


