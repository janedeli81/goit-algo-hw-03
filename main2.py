import turtle

def koch_snowflake(turtle, iterations, length):
    if iterations == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        koch_snowflake(turtle, iterations-1, length)
        turtle.left(60)
        koch_snowflake(turtle, iterations-1, length)
        turtle.right(120)
        koch_snowflake(turtle, iterations-1, length)
        turtle.left(60)
        koch_snowflake(turtle, iterations-1, length)

def draw_snowflake():
    window = turtle.Screen()
    window.bgcolor("sky blue")

    snowflake = turtle.Turtle()
    snowflake.speed(0)
    snowflake.color("white")

    # Встановіть рівень рекурсії тут
    recursion_level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))

    # Початкова позиція
    snowflake.penup()
    snowflake.goto(-150, 90)
    snowflake.pendown()

    for i in range(3):
        koch_snowflake(snowflake, recursion_level, 300)
        snowflake.right(120)

    window.mainloop()

if __name__ == "__main__":
    draw_snowflake()
