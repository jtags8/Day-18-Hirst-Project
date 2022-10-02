# import colorgram
import random
import turtle as t
t.colormode(255)
turt = t.Turtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


# 10x10 rows of spots
# 20 in size
# spaced by 50 spaces
#
# rgb_colors = []
# colors = colorgram.extract('nick_foles_td.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(74, 93, 132), (103, 113, 51), (25, 30, 44), (218, 217, 212), (34, 29, 18), (133, 145, 75), (126, 145, 171), (169, 167, 145), (40, 57, 103), (12, 16, 13), (73, 85, 29), (223, 224, 228), (100, 124, 163), (39, 19, 23), (225, 227, 226), (223, 219, 221), (165, 158, 162), (101, 91, 96), (195, 196, 178), (89, 97, 89), (159, 163, 161), (106, 42, 34), (107, 37, 45), (182, 190, 204), (55, 73, 45), (172, 113, 89), (44, 69, 80), (197, 188, 192), (135, 123, 128), (202, 188, 183)]
turt.speed("fastest")
turt.penup()
turt.hideturtle()
x_cor = -250
y_cor = -250
turt.setposition(x_cor,y_cor)
for _ in range(100):
    turt.color(random_color())
    turt.dot(20)
    turt.forward(50)
    if turt.xcor() == 250:
        turt.setx(-250)
        y_cor += 50
        turt.sety(y_cor)



screen = t.Screen()
screen.exitonclick()