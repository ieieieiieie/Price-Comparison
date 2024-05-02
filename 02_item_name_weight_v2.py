def i_name(question):

    while True:
        name = input(question)

        if name.isalpha():
            return name
        
        else:
            print("Please enter an item name without symbols or numbers.")


def i_weight(question):

    while True:

        try:
            weight = float(input(question))
            return weight

        
        except:
            print("Sorry, you need to enter a number or a decimal number. Anything that is not either of those will result in an error.")

    
def w_unit(question):
    
    while True:
        unit = input(question.lower())

        if unit == "kg":
            return unit

        if unit == "g":
            return unit

#main routines

name = i_name("List your item name here: ")
print("excellent.")

weight = i_weight("List your item weight here: ")
print("excellent.")

unit = w_unit("Is your weight in kg or g? (please list the unit and not the full word) ")
print("excellent.")

if unit == "kg":
    g = weight * 1000

if unit == "g":
    g = weight

print("weight = {}g".format(g))