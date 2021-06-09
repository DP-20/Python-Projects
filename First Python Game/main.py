#This is a very simple quest game in python
print("Welcome to this quest game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name, "you are", age, "years old.")

if age >= 18:
    print("You are old enough to play!")
    wantToPlay = input("Do you want to play? ").lower()
    if wantToPlay == "yes":
        print("Lets play!")
        
        print("Ok you start with 20 health")
        
        leftOrRight = input("Do you want to go Left or Right (left/right)?")
        
        if(leftOrRight == "left"):
            print("You won the game!")
        else:
            print("you ran into some wolves and died :(")
    else:
        print("Bye... :(")
    
else:
    print("You are too young to play the game!")