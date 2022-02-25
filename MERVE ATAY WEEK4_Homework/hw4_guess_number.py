import random, time, datetime

print("You must specify a range of numbers!")
A=int(input("Starting: "))
B=int(input("Finishing: "))
start_time= datetime.datetime.now()
selected_by_computer= random.randrange(A,B)

i=0
while True:
    
    #print(selected_by_computer)
    selected_by_user= int(input("Guess the number: "))

    if selected_by_computer == selected_by_user:
        end_time=datetime.datetime.now()
        guess_time= end_time-start_time
        print("Congratulations! You guessed right!")
        print(f"Guess Time is {guess_time}")
        i+=1
        print(f"You guessed right in your {i}th choice!")
        break
    elif selected_by_computer < selected_by_user:
        print("Wrong! Your number is too high. ")
        i+=1
    elif selected_by_computer > selected_by_user:
        print("Wrong! Your number is too low. ")
        i+=1
    else:
        print("Enter a number in the range!")
