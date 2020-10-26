import turtle
import time


def drawRectangle(gab):
    gab.goto(0, 0)
    gab.pensize(3)
    gab.pendown()
    gab.forward(300)
    gab.left(90)
    gab.forward(250)
    gab.left(90)
    gab.forward(600)
    gab.left(90)
    gab.forward(250)
    gab.left(90)
    gab.forward(600)
    gab.left(90)

    gab.penup()
    gab.home()

    gab.goto(0, 60)
    gab.pendown()
    gab.dot(20)
    gab.penup()
    gab.goto(0, 170)
    gab.pendown()
    gab.dot(20)

    gab.penup()
    gab.goto(0, -50)
    gab.right(90)

    fonte1 = ("Comic Sans", 20, "italic")
    gab.write("Relógio Oficial", False, "center", fonte1)
    gab.forward(40)

    fonte2 = ("Comic Sans", 20, "normal")
    gab.write("do", False, "center", fonte2)
    gab.forward(50)

    fonte3 = ("Comic Sans", 30, "bold")
    gab.write("BIA", False, "center", fonte3)
    gab.left(90)


def drawDigit1(gab, d1, font):
    gab.goto(-280, 0)
    gab.write(int(d1), False, "left", font)


def drawDigit2(gab, d2, font):
    gab.goto(-170, 0)
    gab.write(int(d2), False, "left", font)


def drawDigit3(gab, d3, font):
    gab.goto(170, 0)
    gab.write(int(d3), False, "right", font)


def drawDigit4(gab, d4, font):
    gab.goto(280, 0)
    gab.write(int(d4), False, "right", font)


def drawSeconds(gab, sec, font):
    gab.goto(210, -10)
    gab.write(int(sec), False, "left", font)


def main():
    theWindow = turtle.Screen()
    theWindow.bgcolor("lightgreen")
    turtle.title("Relógio")

    gab = turtle.Turtle()
    gab.speed(0)
    gab.pen()
    gab.hideturtle()
    drawRectangle(gab)

    currentTime = time.strftime('%H:%M:%S', time.localtime())
    d1 = int(currentTime.split(':')[0]) / 10
    d2 = int(currentTime.split(':')[0]) % 10
    d3 = int(currentTime.split(':')[1]) / 10
    d4 = int(currentTime.split(':')[1]) % 10
    sec = int(currentTime.split(':')[2])

    font = ("Comic Sans", 160, "normal")
    font1 = ("Comic Sans", 40, "normal")

    drawDigit1(gab, d1, font)
    drawDigit2(gab, d2, font)
    drawDigit3(gab, d3, font)
    drawDigit4(gab, d4, font)
    drawSeconds(gab, sec, font1)

    while True:
        time.sleep(1)
        gab.undo()
        currentTime = time.strftime('%H:%M:%S', time.localtime())
        sec = int(currentTime.split(':')[2])
        drawSeconds(gab, sec, font1)

        if sec == 0:
            currentTime = time.strftime('%H:%M:%S', time.localtime())
            d1 = int(currentTime.split(':')[0]) / 10
            d2 = int(currentTime.split(':')[0]) % 10
            d3 = int(currentTime.split(':')[1]) / 10
            d4 = int(currentTime.split(':')[1]) % 10

            gab.clear()
            drawRectangle(gab)
            drawDigit1(gab, d1, font)
            drawDigit2(gab, d2, font)
            drawDigit3(gab, d3, font)
            drawDigit4(gab, d4, font)
            drawSeconds(gab, sec, font1)

    theWindow.mainloop()


if __name__ == '__main__':
    main()
