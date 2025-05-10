import random #Inmporting the random module to generate random numbers
win_count = 0 # Variable to keep track of wins
total_count = 0 # Variable to keep track of total attempts
random_number = 0 # Variable to store the random number

print("🎮Welcome to the Guess the Number game!")
def check_guess():
    global win_count, total_count, random_number
    if win_count <=10:
        random_number = random.randint(1,10)
    else:
        random_number = random.randint(11,20)
    
    try:
        user_input = int(input("Guess a number between 1 and 10: "))
    except ValueError:
        print("❌Invalid input. Please enter a number.")
        check_guess()
        return
    if user_input==random_number:
        print("🎉Congratulations! You guessed the number.")
        win_count += 1
        total_count += 1
        print(f"📊Your score is {win_count}/{total_count}")
        
        check_guess()
    else:
        print(f"❌You guessed wrong. Correct number was {random_number}")
        total_count += 1
        print(f"📊Your score is {win_count}/{total_count}") 
        
        check_guess()
check_guess()