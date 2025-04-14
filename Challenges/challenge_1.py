"""Challenge 1: Even or Odd

Problem: Write a function that takes a number as input and returns whether the number is even or odd.
"""

def even_or_odd():
    x = int(input("Input the integer number: "))
    y = x % 2
    if y == 0:
        print(f"The number {x} is even.")
    else:
        print(f"The number {x} is odd.")

even_or_odd()
