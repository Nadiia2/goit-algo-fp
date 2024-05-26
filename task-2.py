import turtle
import math

def draw_pythagoras_tree(t, branch_length, level):
    if level == 0:
        return
    t.forward(branch_length)
    t.left(45)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)

    t.right(90)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, level - 1)

    t.left(45)
    t.backward(branch_length)

def main():
    screen = turtle.Screen()
    screen.title("Pythagoras Tree Fractal")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -200) 
    t.pendown()
    t.left(90) 

    level = int(input("Enter the level of recursion: "))
    
    draw_pythagoras_tree(t, 100, level)

    t.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
