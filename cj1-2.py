# 2) Session 2 Prompt: Write a Python that prints the sum of two floating point numbers,
# the difference between two integers, and the product of a floating point number and an
# integer. In each case, have the program print out the data type of the resulting answer.
import math as m
from PIL.DdsImagePlugin import item1
#phi = (1 + m.sqrt(5)) / 2
#Pi = m.pi

f1 = 0.76
f2 = 0.005

i1 = 7
i2 = 4

def calc_nums(a, b, c, d):
    x = a + b
    print(type(x))
    y = c - d
    print(type(y))
    z = a * c
    print(type(z))

def main():
    calc_nums(f1, f2, i1, i2)

if __name__ == '__main__':
    main()





