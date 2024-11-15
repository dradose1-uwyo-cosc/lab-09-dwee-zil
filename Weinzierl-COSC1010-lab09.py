# Mak Weinzierl
# UWYO COSC 1010
# November 14, 2024
# Lab 09
# Lab Section: 12
# Sources: Classes lecture, Functions lecture

# Classes
# For this assignment, you will be creating two classes:
# One for Pizza
# One for a Pizzeria

# You will be creating a Pizza class. It should have the following attributes:
# - Size
# - Sauce
# - Toppings, which should be a list
# You need to create one method that corresponds with each of the above attributes
# which returns the corresponding attribute, just the value.
# For the size and toppings attributes, you will need to have a method to set them.
# - For Size, ensure it is an int > 10 (inches)
#   - If it is not, default to a 10" pizza (you can store ten). These checks should occur in init as well.
# - For toppings, you will need to add the toppings.
#   - This method needs to be able to handle multiple values.
#   - Append all elements to the list.
# Create a method that returns the amount of toppings.
# In your __init__() method, you should take in size and sauce as parameters.
# - Sauce should have a default value of red.
# - Size will not have a default value; use the parameter with the same safety checks defined above (you can use the set method).
# Within __init__(), you will need to:
# - Assign the parameter for size to a size attribute.
# - Assign the parameter for sauce to the attribute.
# - Create the toppings attribute, starting off as a list only holding cheese.

class Pizza: 
    """A class to describe a pizza"""
    def __init__(self, size, sauce = "red"):
        """Initialize attributes of the pizza"""
        self.setSize(size)
        self.sauce = sauce
        self.toppings = ["cheese"]
    def getSauce(self):
        """Return the sauce of the pizza"""
        return self.sauce
    def setSize(self, size):
        """Set the size of the pizza"""
        if not size.isnumeric() or int(size) < 10:
            self.size = 10
        else:
            self.size = int(size)
    def getSize(self):
        """Return the size of the pizza"""
        return self.size
    def addToppings(self, toppings):
        """Add toppings to the pizza"""
        for topping in toppings:
            self.toppings.append(topping)
    def getToppings(self):
        """Return the toppings of the pizza"""
        return self.toppings
    def getAmountOfToppings(self):
        """Return the amount of toppings on the pizza"""
        return len(self.toppings)

# You will be creating a Pizzeria class with the following attributes:
# - orders, the number of orders placed. Should start at 0.
# - price_per_topping, a static value for the price per topping of 0.30.
# - price_per_inch, a static value of 0.60 to denote how much the pizza cost per inch of diameter.
# - pizzas, a list of all the pizzas with the last ordered being the last in the list.
# You will need the following methods:
# - __init__()
#   - This one does not need to take in any extra parameters.
#   - It should create and set the attributes defined above.
# - placeOrder():
#   - This method will allow a customer to order a pizza.
#     - Which will increment the number of orders.
#   - It will need to create a pizza object.
#   - You will need to prompt the user for:
#     - the size
#     - the sauce, tell the user if nothing is entered it will default to red sauce (check for an empty string).
#     - all the toppings the user wants, ending prompting on an empty string.
#     - Implementation of this is left to you; you can, for example:
#       - have a while loop and append new entries to a list
#       - have the user separate all toppings by a space and turn that into a list.
#   - Upon completion, create the pizza object and store it in the list.
# - getPrice()
#   - You will need to determine the price of the pizza.
#   - This will be (pizza.getSize() * price_per_inch) + pizza.getAmountOfToppings() * price_per_topping.
#   - You will have to retrieve the pizza from the pizza list.
# - getReceipt()
#   - Creates a receipt of the current pizza.
#   - Show the sauce, size, and toppings.
#   - Show the price for the size.
#   - The price for the toppings.
#   - The total price.
# - getNumberOfOrders()
#   - This will simply return the number of orders.

class Pizzeria:
    """A class to describe a pizzeria"""
    def __init__(self):
        """Initialize the attributes of the pizzeria"""
        self.orders = 0
        self.price_per_topping = 0.30
        self.price_per_inch = 0.60
        self.pizzas = []
    def placeOrder(self):
        """Places an order for a pizza"""
        self.orders += 1
        size = input("Enter the size of your pizza here (the default size is 10 inches): ")
        sauce = input("Enter the sauce for your pizza here (the default sauce is red): ")
        if sauce == "":
            sauce = "red"
        toppings = []
        while True:
            topping = input("Enter the toppings for your pizza here, one at a time. Enter a blank topping to stop: ")
            if topping == "":
                break
            else: 
                toppings.append(topping)
        current_pizza = Pizza(size, sauce)
        current_pizza.addToppings(toppings)
        self.pizzas.append(current_pizza)
    def getPrice(self, current_pizza):
        """Returns the price of the current pizza"""
        return current_pizza.getSize() * self.price_per_inch + current_pizza.getAmountOfToppings() * self.price_per_topping
    def getReceipt(self, current_pizza):
        """Returns a receipt for the current pizza"""
        receipt = f"\nYour pizza was {current_pizza.getSize()} inches with {current_pizza.getSauce()} sauce,"
        for i in range(0,len(current_pizza.getToppings()) - 1):
            receipt += f"\n{current_pizza.getToppings()[i]},"
        receipt += f"\nand {current_pizza.getToppings()[len(current_pizza.getToppings()) - 1]}."
        receipt += f"\nThe price for your toppings was: ${current_pizza.getAmountOfToppings() * self.price_per_topping}"
        receipt += f"\nThe total price for your pizza was: ${self.getPrice(current_pizza)}"
        return receipt
    def getNumberOfOrders(self):
        """Returns the number of orders"""
        return self.orders

# - Declare your pizzeria object.
# - Enter a while loop to ask if the user wants to order a pizza.
# - Exit on the word `exit`.
# - Call the placeOrder() method with your class instance.
# - After the order is placed, call the getReceipt() method.
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.

# Example output:
"""
Would you like to place an order? exit to exit
yes
Please enter the size of pizza, as a whole number. The smallest size is 10
20
What kind of sauce would you like?
Leave blank for red sauce
garlic
Please enter the toppings you would like, leave blank when done
pepperoni
bacon

You ordered a 20" pizza with garlic sauce and the following toppings:
                                                                  cheese
                                                                  pepperoni
                                                                  bacon
You ordered a 20" pizza for 12.0
You had 3 topping(s) for $0.8999999999999999
Your total price is $12.9

Would you like to place an order? exit to exit
"""

my_pizzeria = Pizzeria()
while True:
    question = input("Would you like to order a pizza? Enter 'exit' to exit. ")
    if question.lower() == "exit":
        print(f"{my_pizzeria.getNumberOfOrders()} pizzas have been ordered.")
        break
    else:
        my_pizzeria.placeOrder()
        print(f"{my_pizzeria.getReceipt(my_pizzeria.pizzas[-1])}\n")