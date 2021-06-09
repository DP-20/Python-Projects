''' This is a file that will contian
a simple program that does turtle races.
User will have the option to choose the 
number of turtles'''
import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'pink', 'cyan', 'black', 'purple', 'brown']


#This is a function to get the amount of turtles that will be raced
def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers! (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Invalid input!! Enter a number from (2-10)!")
            continue
        
        if 2 <= racers <= 10:
            return racers
        else:
            print("The number you entered is out of range! Please enter a number in range (2-10)!")


''' This method has all the function needed to make the turtle race'''
def race(colors):
    turtles = create_turtles(colors)
    
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)
            
            x,y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]
    

''' This method is used to create the turtles for the race'''
def create_turtles(colors):
    turtles = []
    spacingX = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingX, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
        
    return turtles

''' This is the start of setting up the turtle screen '''
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')

racers = get_number_of_racers()
init_turtle()

#Setting up the turtle colors
random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
print( "The winner is the turtle with color:", winner)
time.sleep(5)

