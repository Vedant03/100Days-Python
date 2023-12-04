import random

#Generate random intergers between starting number and last number
print(random.randint(1,5))

#generate random float numbers between 0 and 1 where 1 is exclusive
print(random.random())

#Comment use of list

list1 = ['Angela', 'Angel2', 'Angel3', 'Angel4', "Angela"]
print(list1)

#append the element at the end of the list  
list1.append("angel5")
print(list1)

#similar to append
list1.extend("a")
print(list1)

#provides the how many times the item was repeated in the list
print(list1.count("Angela"))

#provides the index at which this word is present
print(list1.index("Angela"))

list1.sort()
print(list1)

list1.pop()
print(list1)


