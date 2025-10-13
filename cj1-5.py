# Write a Python program that writes out a table of the function
# sin(x) vs. x, where x is tabulated between 0 and 2 with a thousand
# entries. Follow the basic Python program structure,
# including a main program function.

import numpy as np
from astropy.table import Table

x = np.linspace(0, 2*np.pi, 1000)
y = np.sin(x)
data = Table([x,y], names=["x", "sin(x)"])

def main():
    print(data)

if __name__ == "__main__":
    main()