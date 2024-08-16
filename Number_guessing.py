import random

def game():
    random_numbers = (2, 100, 3, 11, 50, 70, 90, 80, 77, 53, 67, 78, 20, 0, 95)
    number_to_guess = random.choice(random_numbers)  
    a = int(input(f"Enter the number you guess from {random_numbers}: "))
    
    if a == number_to_guess:
        print(f"Congrats! You chose the right number, {a}.")
        print(random.choice(random_numbers))
    elif a > number_to_guess:
        print("The guess is high.")
        print(f"The number is {random.choice(random_numbers)}")
    elif a < number_to_guess:
        print("The guess is low.")
        print(f"The number is {random.choice(random_numbers)}")
    else:
        print("Invalid entry.")
        print(f"The number is {random.choice(random_numbers)}")

while True:
    game()
    again = input("Do you want to try again? (y/n): ").lower()
    if again != "y":
        break
