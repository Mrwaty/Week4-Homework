
from Calculator_functions import addition_ceil, division_ceil, multiplication_ceil, subtraction_ceil
import sys

print("""
      For addition please enter '1'
      For subtraction please enter '2'
      For multiplication please enter '3'
      For division please enter '4'
      For quit please enter 'Q'
      """)

while True:
    my_choice=["1", "2", "3", "4", "Q"]

    try:
        choice= str(input("Choose an operation:"))

        if choice== "1":
            num1= float(input("Enter the first number: "))
            num2= float(input("Enter the second number: "))
            print(addition_ceil(num1,num2))

        elif choice== "2":
            num1= float(input("Enter the first number: "))
            num2= float(input("Enter the second number: "))
            print(subtraction_ceil(num1,num2))

        elif choice== "3":
            num1= float(input("Enter the first number: "))
            num2= float(input("Enter the second number: "))
            print(multiplication_ceil(num1,num2))

        elif choice== "4":
            num1= float(input("Enter the first number: "))
            num2= float(input("Enter the second number: "))
            print(division_ceil(num1,num2))
        
        elif choice=="Q" or choice=="q":
            quit()
        
        else:
            print("You have entered incorrectly. Try again")
    except:
        x=str(sys.exc_info()[0])
        print(x.split("'")[1], "Try again!")

  """
  General Information:
I want to use a program which can calculate basic mathematical operations.

Acceptance Criteria:
* The calculator must support the Addition, Subtraction, Multiplication and Division operations.
* All operations must be in a different module as method.
* Operations must define with two float numbers as parametres.
* Use math.ceil() for all results.
* Create a menu to choose an operation.
* User can choose invalid options, so you must handle all possible error. (Use try except :))
* Inform user what type of error occured (TypError, ValueError etc.)
* This process must continue until user want to quit from calculator.
  
  """
