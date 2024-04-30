# A function which lets me write code that can pause the program for a moment (time.sleep() fucntion)
import time 


# Budget Selector | Completed 10/04/2024 Version 2 | Written By William McArthur
while True:
# ^ This fucntion loops the code 

    # This initates the user's budget input
    try:
        # This prompts you to input a float (a decimal number)
        budget = float(input("input a budget: "))   
        # This variable stores the budget variable as formatted currency
        currency = "${:.2f}".format(budget)

        # This prints the stored currency variable
        print(currency)
        # This breaks the while loop
        time.sleep(1)
        break
        
    # This error message will print and loop you back to the input section if you enter any letters or symbols (except decimal points) in your budget input
    except:
        print("Sorry, whatever you have entered contains an invalid syntax.")
        print()
        print("if your input contains any letters or symbols excluding decimal points, then you have received this error message.") 
        time.sleep(1)     


# Functions



# Main Routines


