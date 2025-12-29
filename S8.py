# =====================================
# Chapter 8 - File Handling in Python
# =====================================


# -------------------------------------
# Example 1: Reading a file
# -------------------------------------
f = open("demofile.txt", "w")
f.write("Hello!\nWelcome to demofile.txt\nGood luck!")
f.close()

f = open("demofile.txt")
print(f.read())
f.close()


# -------------------------------------
# Example 2: Reading file with path
# -------------------------------------
# f = open("D:\\myfiles\\welcome.txt")
# print(f.read())


# -------------------------------------
# Example 3: Using with (recommended)
# -------------------------------------
with open("demofile.txt") as f:
    print(f.read())


# -------------------------------------
# Example 4: Read one line
# -------------------------------------
f = open("demofile.txt")
print(f.readline())
f.close()


# -------------------------------------
# Example 5: Read file line by line
# -------------------------------------
f = open("demofile.txt")
for line in f:
    print(line.strip())
f.close()


# -------------------------------------
# Example 6: Read specific number of characters
# -------------------------------------
with open("demofile.txt") as f:
    print(f.read(5))


# -------------------------------------
# Example 7: Write to file (append)
# -------------------------------------
with open("demofile.txt", "a") as f:
    f.write("\nNow the file has more content.")

with open("demofile.txt") as f:
    print(f.read())


# -------------------------------------
# Example 8: Overwrite file content
# -------------------------------------
with open("demofile.txt", "w") as f:
    f.write("Woops! Content overwritten.")

with open("demofile.txt") as f:
    print(f.read())


# -------------------------------------
# Example 9: Create new file
# -------------------------------------
f = open("myfile.txt", "w")
f.write("This is a new file.")
f.close()


# -------------------------------------
# Example 10: Delete a file safely
# -------------------------------------
import os

if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("File does not exist")


# -------------------------------------
# Example 11: try / except
# -------------------------------------
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")


# -------------------------------------
# Example 12: try / except / else
# -------------------------------------
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")


# -------------------------------------
# Example 13: try / except / finally
# -------------------------------------
try:
    print(y)
except:
    print("Something went wrong")
finally:
    print("try/except finished")


# -------------------------------------
# Example 14: Math functions
# -------------------------------------
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)

print(abs(-7.25))
print(pow(4, 3))


# -------------------------------------
# Example 15: Math module
# -------------------------------------
import math

print(math.sqrt(64))
print(math.ceil(1.4))
print(math.floor(1.4))


# -------------------------------------
# Example 16: Date and time
# -------------------------------------
import datetime

now = datetime.datetime.now()
print(now)


# -------------------------------------
# Example 17: Date formatting
# -------------------------------------
from datetime import datetime

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.strftime("%B %Y"))
print(now.strftime("%A %I:%M %p"))

