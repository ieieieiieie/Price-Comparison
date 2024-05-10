def i_cost(question):

    while True:

        try:
            item_cost = float(input(question))
            return item_cost
        
        except:
            print("please enter a value without letters or symbols (except decimal points)")

item_cost = i_cost("What is your item's cost? ")
formatted_ic = "${:.2f}".format(item_cost)
weight = float(input("weight: "))

unit_cost = item_cost / weight

print("unit cost: {}".format(unit_cost))