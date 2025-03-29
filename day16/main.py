# from turtle import Turtle,Screen
# #my_screen = Screen()
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# timmy.right(360)
# timmy.backward(100)
# timmy.circle(100)
# #print(my_screen.canvheight)
# #my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = 'l'


print(table)