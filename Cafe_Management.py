#storing the menu in a dictionary

Menu= dict(Pasta=70, Pizza=60, Coffee=50, Salad=40, Juice=30, Chowmein=30, Tea=40)

print("Welcome to Friends Cafe")
print("This is our menu:\nPasta= 70taka\nPizza= 60taka\nCoffee= 50taka\nSalad= 40taka\nJuice= 30taka\nChowmein= 30taka\nTea= 40taka")
print("What would you like to order?")

order_total=0
item1= input("Enter what you want to order: ")
if item1 in Menu:
    order_total += Menu[item1]
    print(f"Your {item1} has been added to the order.")
else:
    print(f"{item1} is yet not available on our menu,please order something else.")
item2=input("Do you want to order anything else? (Yes/No): ")
if item2=="Yes":
    item2=input("Enter another item: ")
    order_total += Menu[item2]
    print(f"Your {item2} has been added to the order.")
else:
    print(f"{item2} is yet not available on our menu,please order something else.")

print(f"Your order's total amount is: ",order_total)


