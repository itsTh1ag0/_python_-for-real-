#Python_Tools#
##############


# BASICS (Variables, Strings, Numbers, Lists, Tuples)
astring = "Hello world!"
print("single quotes are ' '")
print(len(astring))
print(astring.index("o"))
print(astring.count("l"))
print(astring[3:7])
print(astring[::-1]) # reverse string
print(astring.upper())
print(astring.lower())
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))
afewwords = astring.split(" ")

data = ("John", "Doe", 53.44)
format_string = "Hello"
print(format_string % data)
print("%s is %d years old." % (data[0], data[2]))

number = 1 + 2 * 3 / 4.0
remainder = 11 % 3
squared = 7 ** 2
cubed = 2 ** 3
helloworld = "hello" + " " + "world"
lotsofhellos = "hello" * 10

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.pop("world")
second_name = names[1]

one = 1
two = 2
three = one + two
print(three)
hello = "hello" 
world = "world"
nullholder = None
helloworld = hello + " " + world
print(helloworld)


# CONDITIONS (If, Else, Elif, and-or-is-in-not)
statement = False
another_statement = True
someList = [1,2,3,4,5]
if statement is True and another_statement is not True: # if
    # do something
    pass
elif 2 in someList or statement != another_statement: # else if
    # do something else
    pass
else:
    # do another thing
    pass


# LOOPS (For, While)
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed, loop")


# FUNCTIONS (Definition & Evoking)
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, number):
    print("Hello, %s, From My Function!, I wish you %d luckiness"%(username, number))

def sum_two_numbers(a, b):
    return a + b

my_function()
my_function_with_args("John Doe", 7)
x = sum_two_numbers(1,2)


# CLASSES & OBJECTS (Templates & Instances for OOP)
class MyClass:
    variable = "blah"

    def __init__(self, number):
        self.number = number

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjectx.variable
myobjectx.function()
NumberHolder = MyClass(7)
print(NumberHolder.number)


# DICTIONARIES (Key:Value pair data-structures)
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781

del phonebook["John"]
phonebook.pop("John")

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))


# MODULES & PACKAGES (Importing external code-source libraries/files)
# from typing import __all__
# import foo.bar
# from foo import bar

# dir(urllib)

# sys.path.append("/foo") 
# PYTHONPATH=/foo python game.py

# __init__.py:__all__ = ["bar"]


# INPUT & OUTPUT (formatted strings)
name = input("Enter your name: ")
age = int(input("Enter your age: "))
country = input("Enter your country: ")

print("Hello, my name is {}, I am {} years old, and I am from {}." .format(name, age, country)) 
print("Hello, my name is %s, I am %d years old, and I am from %s." % (name, age, country))


# GENERATORS (Yielding iterables)
import random

def lottery(): 
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1, 15)

for random_number in lottery():
    print("And the seven numbers are... %d!" %(random_number))


# LIST COMPREHENSIONS (List-building from iterables during assingnment)
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)


# LAMBDA FUNCTIONS (Anonymous | "self-containded" functions)
l = [2,4,7,3,14,19]
for i in l:
    my_lambda = lambda x : (x % 2) == 1
    print(my_lambda(i))


# MULTIPLE FUNCTION ARGUMENTS (ANY N | ARG-DECLARED)
def foo(a, b, c, *args):
    return len(args)

def bar(a, b, c, **kwargs):
    return kwargs["magicnumber"] == 7

# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")


# REGULAR EXPRESSIONS (Pattern recognition)
import re
def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]
    for email in emails:
        if not re.match(pattern, email):
            print("You failed to match %s" % (email))
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")
# Your pattern here!
pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
test_email(pattern)


# EXCEPTION HANDLING (Try, Except, Finally -> Error Handling)
def do_stuff_with_number(n):
    print(n)

def catch_this():
    the_list = (1, 2, 3, 4, 5)

    for i in range(20):
        try:
            do_stuff_with_number(the_list[i])
        except IndexError: # Raised when accessing a non-existing index of a list
            do_stuff_with_number(0)

catch_this()


# SETS (Over/Un-lapping of elements)
a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]

A = set(a)
B = set(b)

print(A.difference(B))
print(A.union(B))
print(A.symmetric_difference(B))
print(a.intersection(b))


# SERIALIZATION (Decode<T>Encode of payloads)
import json

def add_employee(salaries_json, name, salary):
    salaries = json.loads(salaries_json)
    salaries[name] = salary

    return json.dumps(salaries)

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])


# PARTIAL FUNCTIONS (Partial-args heritage)
from functools import partial
def func(u, v, w, x):
    return u*4 + v*3 + w*2 + x

p = partial(func,5,6,7)
print(p(8))


# CODE INTROSPECTION ("Checker" codding utilities)
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
print(dir(Vehicle))

# tooling _v
help()
dir() 
hasattr() 
id() 
type() 
repr() 
callable() 
issubclass() 
isinstance() 


# CLOSURES (Outer-scope arg function-accessing) #
def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier

multiplywith5 = multiplier_of(5)
print(multiplywith5(9))


# DECORATORS (Re-assembling of functions) #
def type_check(correct_type):
    def check(old_function):
        def new_function(arg):
            if (isinstance(arg, correct_type)):
                return old_function(arg)
            else:
                print("Bad Type")
        return new_function
    return check

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])


# MAP, FILTER, and REDUCE #
__builtins__ , map, filter
from functools import reduce

my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
my_numbers = [4, 6, 9, 23, 5]

map_result = list(map(lambda x: round(x ** 2, 3), my_floats))
filter_result = list(filter(lambda name: len(name) <= 7, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

print(map_result)
print(filter_result)
print(reduce_result)

#-------------------#

# PARSING CSV FILES (Opening, Reading, Writing) #
import csv

with open('inputfile.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('outputfile.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        header = next(reader)
        writer.writerow(header)
        for row in reader:
            if int(row[0]) > 50: 
                writer.writerow(row)

#--------#---------#
