#Print in python
print("Hello World")

#Print in python on next line using \n 
print("Hello World\nWhat's up")

#Concatenation of string
print("Concat "+ "the " + "String")

#Getting input from the user in console
vars=input("What is your name: \n")
print(vars)

##Length of the string
print(len(vars))

##We can directly get an element from a string since string acts like an array
print(vars[2])
print(vars[2:len(vars)])

##Reverse a string using negative indices
print(vars[::-1])

##Format in string
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))


myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

##Day 1 project 
print("Hello, This is band generator\n")
user_name=input("Enter your name: \n")
user_pet=input("Enter the name of the pet\n")
print("Band name is " + user_name + user_pet)