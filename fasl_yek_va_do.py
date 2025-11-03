print("Hello, World!")
# در محیط تعاملی (>>>)
print("Hello, World!")
if 5 > 2:
    print("Five is greater than two!")
if 5 > 2:
    print("Five is greater than two!")
x = 5
y = "Hello, World!"
print(x)
print(y)
# This is a comment
print("Hello, World!")

# توضیح در انتهای خط
print("Hello, World!")  # This is a comment

# چند خطی با علامت #
# This is a comment
# written in
# more than one line
print("Hello, World!")

# جلوگیری از اجرا:
#print("Hello, World!")
print("Cheers, Mate!")

# چند خطی با """ (Docstring)
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")
x = 5
y = "John"
print(x)
print(y)

x = 4   # int
x = "Sally"   # str
print(x)
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)
x = 5
y = "John"
print(type(x))
print(type(y))
x = "John"
x = 'John'
print(x)
a = 4
A = "Sally"
print(a)
print(A)
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
# Camel Case
myVariableName = "John"

# Pascal Case
MyVariableName = "John"

# Snake Case
my_variable_name = "John"
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
x = y = z = "Orange"
print(x)
print(y)
print(z)
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python is awesome"
print(x)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

# خطا در ترکیب رشته و عدد:
# x = 5
# y = "John"
# print(x + y)

x = 5
y = "John"
print(x, y)
# مثال ۱: متغیر سراسری
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

# مثال ۲: متغیر محلی و سراسری با نام یکسان
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()
print("Python is " + x)

# مثال ۳: استفاده از global
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)
x = 5
name = "Ali"
is_student = True
pi = 3.14
myvar = "Reza"
my_var = "Sara"
_myVar = "Omid"
var2 = 20
MYVAR = "Python"
print('Hello', 'World')
x = 'awesome'

def myfunc():
    x = 'fantastic'

myfunc()

print('Python is ' + x)
x = 5
print(type(x))
x = "Hello World"
print(x)
print(type(x))

x = 20
print(x)
print(type(x))

x = ["apple", "banana", "cherry"]
print(x)
print(type(x))

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
x = str("Hello World")
print(x)
print(type(x))

x = int(20)
print(x)
print(type(x))

x = list(("apple", "banana", "cherry"))
print(x)
print(type(x))

x = bool(5)
print(x)
print(type(x))
x = 1     # int
y = 2.8   # float
z = 1j    # complex

print(type(x))
print(type(y))
print(type(z))
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))

x = 3 + 5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))
x = float(1)
y = int(2.8)
z = complex(1)
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))
x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)

x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)

x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)
print("Hello")
print('Hello')

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
a = "Hello, World!"
print(a[1])
for x in "banana":
    print(x)
a = "Hello, World!"
print(len(a))
txt = "The best things in life are free!"
print("free" in txt)
b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])
a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip())

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
b = a.split(",")
print(b)
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)
age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

x = 10
y = 20
result = f"The sum of {x} and {y} is {x + y}."
print(result)

name = "Alice"
age = 30
greeting = f"Hello, I'm {name} and I'm {age} years old."
print(greeting)
txt = 'It\'s alright.'
print(txt)

txt = "This will insert one \\ (backslash)."
print(txt)

txt = "Hello\nWorld!"
print(txt)

txt = "Hello\rWorld!"
print(txt)

txt = "Hello\tWorld!"
print(txt)

txt = "Hello \bWorld!"
print(txt)
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

x = 200
print(isinstance(x, int))
x = 5
y = 3
print(x + y)

x = 12
y = 3
print(x / y)

x = 15
y = 2
print(x // y)

x = 2
y = 5
print(x ** y)  # same as 2*2*2*2*2

x = 5
y = 3
print(x - y)

x = 5
y = 3
print(x * y)
x = 5
print(x)

x = 5
x += 3
print(x)
x = 5
y = 3
print(x == y)
print(x != y)
print(x >= y)
x = 5
print(x > 3 and x < 10)

x = 5
print(x > 3 or x < 4)

x = 5
print(not (x > 3 and x < 10))
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

print(x is not z)
print(x is not y)
print(x != y)
x = ["apple", "banana"]
print("banana" in x)

x = ["apple", "banana"]
print("pineapple" not in x)
print(6 & 3)
print(6 | 3)
print((6 + 3) - (6 + 3))
# Parenthesis have the highest precedence, and are evaluated first.
# The calculation above reads 9 - 9 = 0

