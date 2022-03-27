# import turtle
# timmy = turtle.Turtle()

### CHECK NOTEBOOK FOR OPP NOTES ##
# Check t of a module to know all the attributes & methods of an object
# https://docs.python.org/3/library/turtle.html
import turtle
from turtle import Turtle, Screen
timmy = Turtle()
# Another method/function? for this object is to change the shape, colour
timmy.shape("turtle")
timmy.color("orange")
timmy.forward(100)

print(timmy)

# Screen is another class in Turtle module
# It represents the window in which the turtle shows up

my_screen = Screen()
# Now we can tap into pne of the screen's properties
print(my_screen.canvheight)
# my_screen = object, canvheight = attribute associated with the screen
#when you the program you will see the canvas height (300) printed

# Objects also have methods (i.e. things that it can do)
my_screen.exitonclick()
# Allows us to continue running the screen until we click the screen

# Right click prettytable to see its implementation
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align["Pokemon Name"] = "l"
# table.align["Type"] = "l"
table.align = "l"
print(table)



