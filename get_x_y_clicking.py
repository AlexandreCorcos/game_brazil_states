import turtle

screen = turtle.Screen()
image = "brazil_states_blank.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_click(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click)
turtle.mainloop()

screen.exitonclick()