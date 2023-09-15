a = input (100)
b = input (100)
c = input (100)

if a >= 100 and b >= 100 and c >= 100:
    print('The 3 line segments can form an equilateral triangle')
else:
    print('The 3 line segments can not form an equilateral triangle')

import turtle
turtle.shape('turtle')

turtle.forward(a)

turtle.left(120)

turtle.forward(b)

turtle.left(120)

turtle.forward(c)

turtle.mainloop()