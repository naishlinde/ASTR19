#3) Session 3 Prompt: Write a Python program that defines a function f(x) that returns x**3 + 8.
# In the main function of the program, call f(x) with x = 9 and print the result.
# Use an if statement that executes if the result is larger than 27 and prints “YAY!”.



def f(x):
    y = x**3 + 8
    print(y)
    if y > 27:
        print('YAY!')

a = 9

def main():
    f(a)

if __name__ == '__main__':
    main()




