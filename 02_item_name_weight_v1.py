item = input("What is the item you're looking for called? ")

weight = float(input("input a weight: "))
unit = input("kg or g: ".lower())

if unit == "kg":
    g = weight * 1000

elif unit == "g":
    g = weight

print(g)