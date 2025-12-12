#1
a = 33
b = 200
if b > a:
    print("b is greater than a")
#2
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
#3
a = 200
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
#4
a = 200
b = 33
c = 500

if a > b and c > a:
    print("Both conditions are True")
#5    
a = 200
b = 33
c = 500

if a > b or a > c:
    print("At least one of the conditions is True")
#6
a = 33
b = 200

if not a > b:
    print("a is NOT greater than b")
#7
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
#8
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
#9
day = 4

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
#10
day = 4

match day:
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Looking forward to the Weekend")
#11
month = 5
day = 4

match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")
#12
i = 1

while i < 6:
    print(i)
    i += 1
#13
i = 1

while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
#14
i = 0

while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
#15
i = 1

while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
#16 
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)
#17  
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)
    if x == "banana":
        break
#18
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    if x == "banana":
        break
    print(x)
#19
def greet():
    print("Hello from a function")
#20
def my_function():
    print("Hello from a function")

my_function()
    
#21
def my_function():
    print("Hello from a function")

my_function()
my_function()
my_function()
#22   
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)
#23 
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))
#24
def get_greeting():
    return "Hello from a function"

message = get_greeting()
print(message)
#25
def get_greeting():
    return "Hello from a function"

print(get_greeting())
#26
def future_function():
    pass

future_function()
#27
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum:", sum)

add_numbers(5, 4)
#28
def greet(name):
    print("Hello", name)

greet("John")
#29
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")
#30
def my_function(name="friend"):
    print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")
#31
def my_function(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)
#32
def my_function(person):
    print("Name:", person["name"])
    print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)
#33
message = 'Hello'

def greet():
    print('Local', message)

greet()
print('Global', message)
#34
def outer():
    message = 'local'

    def inner():
        nonlocal message
        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()
#35
def myfunc():
    x = 300

    def myinnerfunc():
        print(x)

    myinnerfunc()

myfunc()
#36
def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)
#37
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
#38
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))
#39
name = input("Enter your name: ")
print("Hello,", name)
