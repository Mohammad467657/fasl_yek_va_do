# ---------- Example 1: List ----------
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)

# ---------- Example 2: Integer Array ----------
import array

arr = array.array('i', [1, 2, 3, 4])
arr.append(5)
arr[1] = 10
print(arr)

# ---------- Example 3: List vs Array ----------
lst = [1, 2, 3]
lst.append(4)
print("LIST =", lst)

import array
arr = array.array('i', [1, 2, 3])
arr.append(4)
print(arr)

# ---------- Example 4: User Input (Name) ----------
print("Enter your name:")
name = input()
print(f"Hello {name}")

# ---------- Example 5: Multiple Inputs ----------
name = input("Enter your name: ")
fav1 = input("What is your favorite animal: ")
fav2 = input("What is your favorite color: ")
fav3 = input("What is your favorite number: ")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")

# ---------- Example 6: Number Input & Square Root ----------
import math

x = input("Enter a number: ")
y = math.sqrt(float(x))
print(f"The square root of {x} is {y}")

# ---------- Example 7: Input Validation with try/except ----------
y = True
while y:
    x = input("Enter a number: ")
    try:
        x = float(x)
        y = False
    except:
        print("Wrong input, please try again.")

print("Thank you!")

# ---------- Example 8: try / except with NameError ----------
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# ---------- Example 9: try / except / else ----------
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# ---------- Example 10: try / except / finally ----------
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The try/except is finished")

# ---------- Example 11: min & max ----------
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)

# ---------- Example 12: abs & pow ----------
x = abs(-7.25)
print(x)

x = pow(4, 3)
print(x)

# ---------- Example 13: math.sqrt ----------
import math
x = math.sqrt(64)
print(x)

# ---------- Example 14: math.ceil & math.floor ----------
import math
x = math.ceil(1.4)
y = math.floor(1.4)
print(x)
print(y)
