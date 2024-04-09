while True:

    try:
        budget = float(input("input a budget: "))   
        currency = "${:.2f}".format(budget)

        print(currency)
        break
    except:
        print("Sorry, whatever you have entered contains an invalid syntax.")
        print()
        print("if your input contains any letters or symbols excluding decimal points, then you have received this error message.")        