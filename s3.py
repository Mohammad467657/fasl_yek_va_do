# ایجاد لیست
fruits = ['apple', 'banana', 'cherry']
print(fruits)

# متد append() – اضافه کردن به انتهای لیست
fruits.append("orange")
print(fruits)

# افزودن یک لیست دیگر به داخل لیست
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)

# متد clear() – پاک کردن تمام عناصر لیست
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits)

# متد copy() – ساخت یک کپی از لیست
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)

# متد count() – شمارش تعداد وقوع یک مقدار
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)

# متد extend() – افزودن چند آیتم به انتهای لیست
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

# متد index() – موقعیت اولین وقوع مقدار
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange', 'cherry']
x = fruits.index("cherry", 4)
print(x)

# متد insert() – درج مقدار در موقعیت مشخص
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

# متد pop() – حذف آیتم از موقعیت مشخص
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

# pop بدون اندیس (حذف آخرین عنصر)
my_list = [10, 20, 30]
x = my_list.pop()
print(my_list)
print(x)

# خطای رایج:
fruits = ['apple', 'banana', 'cherry']
fruits = fruits.pop(1)
print(fruits)  # خطا: مقدار بازگشتی pop یک آیتم است نه لیست

# متد remove() – حذف اولین وقوع مقدار
fruits = ['apple', 'banana', 'cherry', 'banana']
fruits.remove("banana")
print(fruits)

# del – حذف با اندیس یا کل لیست
my_list = [1, 2, 3]
del my_list[1]
print(my_list)
# del my_list  # حذف کل لیست از حافظه

# متد reverse() – برعکس کردن ترتیب عناصر
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

# متد sort() – مرتب‌سازی لیست
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)
# ایجاد تاپل
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# تاپل با مقادیر تکراری
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# ایجاد تاپل با سازنده tuple()
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

# تبدیل لیست به تاپل
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)

# دسترسی با اندیس
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# اندیس منفی
print(thistuple[-1])

# محدوده شاخص‌ها
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[-4:-1])

# بررسی وجود مقدار
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the tuple")

# به‌روزرسانی تاپل با تبدیل به لیست
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# افزودن آیتم جدید با append از طریق لیست
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

# افزودن تاپل دیگر با +=
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

# حذف آیتم با تبدیل به لیست
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# حذف کامل تاپل
thistuple = ("apple", "banana", "cherry")
del thistuple

# Unpacking tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# استفاده از * برای جمع‌آوری مقادیر باقی‌مانده
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(tropic)

# حلقه در تاپل
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

# حلقه while روی تاپل
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1

# اتصال و تکرار تاپل‌ها
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

# متدهای تاپل
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple.count(5))
print(thistuple.index(8))
# ایجاد مجموعه
thisset = {"apple", "banana", "cherry"}
print(thisset)

# سازنده set()
thisset = set(("apple", "banana", "cherry"))
print(thisset)
print(type(thisset))

# پیمایش مجموعه
for x in thisset:
    print(x)

# افزودن آیتم جدید
thisset.add("orange")
print(thisset)

# افزودن چند آیتم از مجموعه یا لیست دیگر
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# حذف آیتم
thisset.remove("banana")
print(thisset)

# حذف بدون خطا
thisset.discard("banana")

# حذف تصادفی با pop()
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# خالی کردن مجموعه
thisset.clear()
print(thisset)

# حذف کامل مجموعه
thisset = {"apple", "banana", "cherry"}
del thisset

# Union, Update, Intersection, Difference, Symmetric Difference
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
print(set1.union(set2))
print(set1 | set2)

set1.update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print(set1.intersection(set2))
print(set1 & set2)

# frozenset
mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
print(x)
# ایجاد دیکشنری
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict)
print(thisdict["brand"])

# با سازنده dict()
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)

# دسترسی به مقدار با get()
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict.get("model"))

# keys(), values(), items()
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())

# بررسی وجود کلید
if "model" in thisdict:
    print("Yes, 'model' is in dictionary")

# update()
thisdict.update({"year": 2020})
print(thisdict)

# افزودن کلید جدید
thisdict["color"] = "red"
print(thisdict)

# pop(), popitem(), del, clear()
thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

thisdict["year"] = 2020
del thisdict["year"]
print(thisdict)

thisdict.clear()
print(thisdict)
# حلقه روی کلیدها و مقادیر
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for x in thisdict:
    print(x, thisdict[x])

# حلقه فقط روی مقادیر
for value in thisdict.values():
    print(value)

# حلقه فقط روی کلیدها
for key in thisdict.keys():
    print(key)

# حلقه روی کلیدها و مقادیر با items()
for x, y in thisdict.items():
    print(x, y)

# کپی دیکشنری
mydict = thisdict.copy()
print(mydict)
mydict2 = dict(thisdict)
print(mydict2)

# دیکشنری‌های تو در تو
child1 = {"name": "Emil", "year": 2004}
child2 = {"name": "Tobias", "year": 2007}
child3 = {"name": "Linus", "year": 2011}
myfamily = {"child1": child1, "child2": child2, "child3": child3}
print(myfamily)

# دسترسی به داده‌های تودرتو
print(myfamily["child2"]["name"])

# حلقه روی دیکشنری‌های تودرتو
for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print(y + ":", obj[y])
