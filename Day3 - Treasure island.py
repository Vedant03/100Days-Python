#Day3 - Treasure island
direction = input("Enter the direction to go -east or west: \n")
swim_or_wait = input("Enter whether you want to swim or wait \n")
door_colour = input("Enter the door colour that you want to enter\n")

if (direction.lower() == "east"):
    print("First step successful")
    if(swim_or_wait.lower() =="swim"):
        print("2nd step successful")
        if(door_colour.lower() =="yellow"):
            print("You are winner")
        else:
            print("Game Over")
    else:
        print("Game over")
else:
    print("Game over")