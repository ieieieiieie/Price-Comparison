while True:

    try:
        i_cost = float(input("what is your items cost: "))
        cost = "${:.2f}".format(i_cost)

        print(cost)

        weight = 5

        unit_cost = i_cost / weight
        formatted_unit_cost = "${:.2f}".format(unit_cost)

        print("unit cost = {}".format(formatted_unit_cost))
        break
    except:
        print("you have entered an invalid value, please only enter numbers & decimal points.")
