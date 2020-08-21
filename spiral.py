import turtle
turtle.bgcolor("WHITE")
window = turtle.Screen()
turtle.pencolor("GREEN")
def draw_spiral(radius):
    original_xcor = turtle.xcor()
    original_ycor = turtle.ycor()
    speed = 10
    while True:
        turtle.forward(speed)
        turtle.left(10)
        speed += 0.1
        
        if turtle.distance(original_xcor, original_ycor) > radius:
            break
draw_spiral(600)
window.exitonclick()
