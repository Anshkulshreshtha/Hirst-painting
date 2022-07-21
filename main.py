# import colorgram
#
#
# rgb_colors = []
# colors = colorgram.extract('hirst pic.jpg', 30)
#
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)


import random
import turtle as t

t.colormode(255)
ak = t.Turtle()
ak.speed("fastest")
ak.penup()
ak.hideturtle()
color_list = [(200, 167, 110), (237, 241, 246), (144, 74, 52), (169, 152, 45), (58, 92, 119), (224, 203, 131), (136, 162, 180), (131, 34, 26), (51, 117, 89), (199, 94, 72), (143, 25, 30), (18, 97, 74), (69, 47, 40), (173, 146, 153), (150, 177, 152), (131, 70, 74), (56, 43, 46), (237, 174, 163), (184, 88, 94), (38, 58, 71), (28, 82, 89), (182, 204, 178), (242, 156, 160), (93, 144, 124), (20, 66, 57), (36, 65, 96), (108, 125, 154)]

ak.setheading(225)
ak.forward(300)
ak.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    ak.dot(20, random.choice(color_list))
    ak.forward(50)

    if dot_count % 10 == 0:
        ak.setheading(90)
        ak.forward(50)
        ak.setheading(180)
        ak.forward(500)
        ak.setheading(0)

ak.setheading(90)

screen = t.Screen()
screen.exitonclick()
