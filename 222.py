import turtle

# Настройка экрана
screen = turtle.Screen()
screen.title("Зайчик")
screen.bgcolor("lightblue")

# Создаю черепашку для рисования
bunny = turtle.Turtle()
bunny.speed(5)  # Средняя скорость рисования
bunny.pensize(3)

# Функция для рисования круга
def draw_circle(t, color, radius, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Рисую туловище (серый овал)
bunny.penup()
bunny.goto(0, -100)
bunny.pendown()
bunny.color("gray")
bunny.begin_fill()
bunny.circle(60, 90)  # Четверть круга
bunny.circle(120, 180)  # Полукруг
bunny.circle(60, 90)  # Четверть круга
bunny.end_fill()

# Рисую голову
draw_circle(bunny, "gray", 40, 0, 20)

# Рисую уши
# Левое ухо
bunny.penup()
bunny.goto(-20, 60)
bunny.pendown()
bunny.color("gray")
bunny.begin_fill()
bunny.setheading(60)
bunny.circle(40, 120)  # Внешняя часть уха
bunny.goto(-20, 60)
bunny.end_fill()

# Правое ухо
bunny.penup()
bunny.goto(20, 60)
bunny.pendown()
bunny.begin_fill()
bunny.setheading(120)
bunny.circle(-40, 120)  # Внешняя часть уха
bunny.goto(20, 60)
bunny.end_fill()

# Внутренняя часть ушей
draw_circle(bunny, "pink", 15, -15, 80)
draw_circle(bunny, "pink", 15, 15, 80)

# Рисую глаза
draw_circle(bunny, "black", 5, -15, 40)
draw_circle(bunny, "black", 5, 15, 40)

# Рисую нос
bunny.penup()
bunny.goto(0, 30)
bunny.pendown()
bunny.color("pink")
bunny.begin_fill()
bunny.goto(-5, 20)
bunny.goto(5, 20)
bunny.goto(0, 30)
bunny.end_fill()

# Рисую рот
bunny.penup()
bunny.goto(0, 20)
bunny.pendown()
bunny.right(90)
bunny.circle(10, 180)  # Улыбка

# Рисую передние лапки
bunny.penup()
bunny.goto(-30, -40)
bunny.pendown()
bunny.color("gray")
bunny.begin_fill()
bunny.circle(15)
bunny.end_fill()

bunny.penup()
bunny.goto(30, -40)
bunny.pendown()
bunny.begin_fill()
bunny.circle(15)
bunny.end_fill()

# Рисую задние лапки
bunny.penup()
bunny.goto(-50, -100)
bunny.pendown()
bunny.begin_fill()
bunny.circle(20)
bunny.end_fill()

bunny.penup()
bunny.goto(50, -100)
bunny.pendown()
bunny.begin_fill()
bunny.circle(20)
bunny.end_fill()

# Рисую хвост (маленький круг)
draw_circle(bunny, "white", 10, 0, -120)

# Скрываю черепашку
bunny.hideturtle()

# Завершение программы
turtle.done()
