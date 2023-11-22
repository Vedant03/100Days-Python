bill = input("Enter the bill:\n")
people = input("Enter the number of people to share it:\n")
tip_amount=input("Enter the tip %: ")

individual_contro = (int(bill)/int(people) + (int(tip_amount)/100)*int(bill))
print(individual_contro)