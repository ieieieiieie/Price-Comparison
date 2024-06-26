# A function which lets me write code that can pause the program for a moment (time.sleep() fucntion)
import time 

# list prompt
list = []
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
        print()
        break
        
    # This error message will print and loop you back to the input section if you enter any letters or symbols (except decimal points) in your budget input
    except:
        print("Sorry, whatever you have entered contains an invalid syntax.")
        print()
        print("if your input contains any letters or symbols excluding decimal points, then you have received this error message.") 
        time.sleep(1)     


# Functions

# Item Characteristics Selector | Completed 03/05/2024 Version 2 | Written by William McArthur

def i_name(question):
# defines the item name

    # loops this function to check for errors
    while True:
        name = input(question)
        # name input prompt

        # checks if the entry contains only letters
        if name.isalpha():
            return name
            #return and store the user's entry as the name variable
        
        # the error message that is printed if your entry is not only letters
        else:
            print("Please enter an item name without symbols or numbers.")


def i_weight(question):
# defines the item weight

    while True:
    # loops this function to check for errors

        try:
            weight = float(input(question))
            # weight input prompt, only takes numbers & decimal points
            return weight
            # return and store the entered value as the weight variable
        
        # the error message that is printed if your entry contains invalid characters
        except:
            print("Sorry, you need to enter a number or a decimal number. Anything that is not either of those will result in an error.")

    
def w_unit(question):
# defines the weight unit

    while True:
    # loops this function to check for errors
        unit = input(question.lower())
        # weight input prompt, only takes g or kg

        if unit == "kg":
            return unit
        # sets the unit type to kg

        if unit == "g":
            return unit
        # sets the unit type to g

# ~~~DIVIDER~~~

# Unit Cost Calculator | Completed 10/05/2024 Version 2 | Written by William McArthur

def i_cost(question):
# defines the item cost 

    while True:
    # loops this function to check for errors

        try:
            item_cost = float(input(question))
            return item_cost
            # prompt for item cost, stores the value 

        # error message
        except:
            print("please enter a value without letters or symbols (except decimal points)")

# Main Routines

# item name input
while True:
    
    name = i_name("List your item name here: ")
    print("excellent.")
    time.sleep(2)

    # item weight input
    weight = i_weight("List your item weight here: ")
    print("excellent.")
    time.sleep(2)

    # weight unit input
    unit = w_unit("Is your weight in kg or g? (please list the unit and not the full word) ")
    print("excellent.")
    time.sleep(2)

    # kg to g converter
    if unit == "kg":
        kg = weight 

    # store the weight as a seperate variable
    if unit == "g":
        kg = weight / 1000

    print("weight = {}kg".format(kg))
    # weight display

    # ~~~DIVIDER~~~

    # item cost input, formats it later
    item_cost = i_cost("What is your item's cost? ")
    formatted_ic = "${:.2f}".format(item_cost)

    # unit cost formula in code form
    unit_cost = item_cost / kg

    # prints the formatted currency
    print(formatted_ic)
    time.sleep(2)

    # prints the unit cost
    print("unit cost: ${:.2f}".format(unit_cost))

    # prompt for making another item
    answer = input("would you like to make another item? y / n: ").lower()
    product= []
    
    # loops the item creation
    if answer == "no" or answer == "n":
        
        # add the itme name and unit cost to the list
        product.append(name)
        product.append(unit_cost)
        list.append(product)
        break
    
    # breaks the loop
    elif answer == "yes" or answer == "y":
        print("okay")
        product.append(name)
        product.append(unit_cost)
        list.append(product)
        time.sleep(2)
        print()

# sorts the list properly
sorted_list=sorted(list, key=lambda x: x[1])

# prints the list and the cheapest items
print(sorted_list)
time.sleep(1)
print()
# the cheapest item
print("{} is the most efficient item to buy within budget".format(sorted_list[0]))
time.sleep(1)
# the second cheapest item
print("{} is also a good alternative if you don't like the first option".format(sorted_list[1]))