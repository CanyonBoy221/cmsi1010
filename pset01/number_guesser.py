
import random #imports the random function

#Thinks of a random number
random_number = random.randint(1, 1000)

def print_correct_guess():
    print("You just got lucky, your not even that smart")

def print_wrong_guess():
    print("ERRRRR Wrong, stupid, git better at guessing. Try again")

def print_higher():
    print("The number is higher")

def print_lower():
    print("The number is lower")

guess_count = 0
    
def print_guess_count():
    print("This is how many tries it took you")
    print(guess_count)

#Print function to ask user to guess the number
print("Hello human, I have thought of a random number, can you guess it?")
print("You can type 'exit' or 'bye' to leave the program")

keep_going = True
while keep_going:
    response = input()
    if response == "exit": #If response is exit then the program ends
        print("I didnt want you to guess anyway.")
        keep_going = False
    
    elif response == "bye": #If response is bye then the program ends
        print("Goodbye!")
        keep_going = False

    elif not response.isdigit(): #Checks if response has any non numbers
        print("Idk what you mean brochacho") #If there are letters it prints this

    elif int(response) == random_number: #If the response is a correct guess 
        print_correct_guess() 
        guess_count += 1
        print_guess_count
        random_number = random.randint(1, 1000) #Generates another number
        print_guess_count()
        guess_count = 0 #Resets guess_count to 0
        

    else:
        guess = int(response) #If the response does not equal the random number
        print_wrong_guess()
        if guess > random_number:
            print_lower() #Tells me if the number is lower
            guess_count += 1 #Adds one to guess count
        elif guess < random_number:
            print_higher() #Tells me the number is higher
            guess_count += 1 #Adds one to guess count