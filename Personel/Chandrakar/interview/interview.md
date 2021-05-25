Python Interview Questions :

Q1. What is the difference between list and tuples in Python?
Ans. List items are ordered, changeable, and allow duplicate values and reprsented squre breket [ ] .but in  tuple is a collection which
is ordered and unchangeable
Tuples are written with round brackets( ).


Q2. What are the key features of Python?
Ans. Python is an interpreted language .python does not need to be compiled before it is run.
Python is dynamically typed, this means that you don’t need to state the types of variables when you declare them or anything like that. You can do things like x=111 and then x="I'm a string" without error
object oriented programing in that it allows the definition of classes along with composition and inheritance.
in Python,function  are first-class objects. This means that they can be assigned to variables, returned from other functions and passed into functions.



Q3. What type of language is python? Programming or scripting?
Ans. Python is capable of scripting, but in general sense, it is considered as a general-purpose programming language



Q4.Python an interpreted language. Explain.
An interpreted language is any programming language which is not in machine-level code before runtime.Therefore, Python is an interpreted language.



Q5.What is pep 8?
PEP stands for Python Enhancement Proposal. It is a set of rules that specify how to format Python code for maximum readability.



Q6. How is memory managed in Python?
Ans. Memory management in python is managed by Python private heap space. All Python objects and data structures are located in a private heap. The programmer does not have access to this private heap. The python interpreter takes care of this instead.
    1. The allocation of heap space for Python objects is done by Python’s memory manager. The core API gives access to some tools for the programmer to code.
    2. Python also has an inbuilt garbage collector, which recycles all the unused memory and so that it can be made available to the heap space.



Q7. What is namespace in Python?

Ans.A namespace is a naming system used to make sure that names are unique to avoid naming conflicts.



Q8. What is PYTHONPATH?
Ans.It is an environment variable which is used when a module is imported. Whenever a module is imported, PYTHONPATH is also looked up to check for the presence of the imported modules in various directories. The interpreter uses it to determine which module to load.



Q9. What are python modules? Name some commonly used built-in modules in Python?
Ans. Python modules are files containing Python code. This code can either be functions classes or variables. A Python module is a .py file containing executable code.
Some of the commonly used built-in modules are:
    • os
    • sys
    • math
    • random
    • data time
    • JSON




Q10.What are local variables and global variables in Python?
Ans. Global Variables:
Variables declared outside a function or in global space are called global variables. These variables can be accessed by any function in the program.
Local Variables:
Any variable declared inside a function is known as a local variable. This variable is present in the local space and not in the global space.



Q11. Is python case sensitive?
Ans. Yes python is case sensitive becuse ifany variable dicler than used on small later any vriable.other wise error show.



Q12.What is type conversion in Python?
Ans.one data to another data types change it’s call tpye conversion. Like int() that means change
into integer types


Q13. How to install Python on Windows and set path variable?
Ans. To install Python on Windows, follow the below steps:
    • Install python from this link:https://www.python.org/downloads/
    • After this, install it on your PC. Look for the location where PYTHON has been installed on your PC using the following command on your command prompt: cmd python.
    • Then go to advanced system settings and add a new variable and name it as PYTHON_NAME and paste the copied path.
    • Look for the path variable, select its value and select ‘edit’.
    • Add a semicolon towards the end of the value if it’s not present and then type %PYTHON_HOME%

Q14. Is indentation required in python?
Ans.
Indentation is necessary for Python. It specifies a block of code. All code within loops, classes, functions, etc is specified within an indented block. It is usually done using four space characters. If your code is not indented necessarily, it will not execute accurately and will throw errors as well

Q15. What is the difference between Python Arrays and lists?
Ans. Arrays and lists, in Python, have the same way of storing data. But, arrays can hold only a single data type elements whereas lists can hold any data type elements.

Q16. What are functions in Python?
Ans. A function is a block of code which is executed only when it is called. To define a Python function, thedef keyword is used.
Q17.What is __init__?
__init__ is a method or constructor in pyhton This method is automatically called to allocate memory when a new object/ instance of a class is created. All classes have the __init__ method.

Q18.What is a lambda function?
Ans. An anonymous function is known as a lambda function. This function can have any number of parameters but, can have just one statement.
Q19. What is self in Python?
Ans. Self is an instance or an object of a class. In Python, this is explicitly included as the first parameter. However, this is not the case in Java where it’s optional. It helps to differentiate between the methods and attributes of a class with local variables.
The self variable in the init method refers to the newly created object while in other methods, it refers to the object whose method was called.

Q20. How does break, continue and pass work?
Ans.
The break statement terminates the loop containing it. Control of the program flows to the statement immediately after the body of the loop.
If the break statement is inside a nested loop (loop inside another loop), the break statement will terminate the innermost loop.

Q21. What does [::-1} do?
Ans. [::-1] is used to reverse the order of an array or a sequence.

Q22. How can you randomize the items of a list in place in Python?
Ans. Consider the example shown below:
from random import shuffle
x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
shuffle(x)
print(x)

The output of the following code is as below.
['Flying', 'Keep', 'Blue', 'High', 'The', 'Flag']

Q23. What are python iterators?
Ans. Iterators are objects which can be traversed though or iterated upon
Q24. How can you generate random numbers in Python?
Ans. Used on import random
random.random
Q25. What is the difference between range & xrange?
For the most part, xrange and range are the exact same in terms of functionality. They both provide a way to generate a list of integers for you to use, however you please. The only difference is that range returns a Python list object and x range returns an xrange object.
This means that xrange doesn’t actually generate a static list at run-time like range does. It creates the values as you need them with a special technique called yielding. This technique is used with a type of object known as generators. That means that if you have a really gigantic range you’d like to generate a list for, say one billion, xrange is the function to use



Q26. How do you write comments in python
ans.  in python used on # comments of the line.


Q27. What is pickling and unpickling?
ans.Pickling  - is the process whereby a Python object hierarchy is converted into a byte stream.
 
    unpickling -is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an
    object hierarchy.
    
    
Q28. What are the generators in python?
ans. a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).


Q29. How will you capitalize the first letter of string?
ans.In Python, the capitalize() method returns a copy of the original string and converts the first character of the string to a capital
 (uppercase) letter



Q30. How will you convert a string to all lowercase?
ans .In Python, lower() is a built-in method used for string handling. The lower() methods returns the lowercased string from the given
 string. It converts all uppercase characters to lowercase.


Q31. How to comment multiple lines in python?
ans .  Python doesn't support multi-line comment blocks out of the box. The recommended way to comment out multiple lines of code in
 Python is to use consecutive # single-line comments


Q32.What are docstrings in Python?
ans.  Python docstrings are strings used right after the definition of a function, method, class, or module (like in Example 1). They are
 used to document our code. We can access these docstrings using the __doc__ attribute.


Q33. What is the purpose of is, not and in operators?
ans . is not - Returns True if both variables are not the same object
      in - Returns True if a sequence with the specified value is present in the object

Q34. What is the usage of help() and dir() function in Python?
ans . help() - The python help function is used to display the documentation of modules, functions, classes, keywords etc. The help
 function has the following syntax: help([object]) If the help function is passed without an argument, then the interactive help utility
 starts up on the console
  
  dir() - The dir() function returns all properties and methods of the specified object, without the values. This function will return
   all the properties and methods, even built-in properties which are default for all object.
   
   
Q35. Whenever Python exits, why isn’t all the memory de-allocated?
ans.When Python exit, the object referenced from global namespaces of Python modules are not always deallocated. So, Python doesn't
 recognize and free circular memory references before using the garbage collector


Q36. What is a dictionary in Python?
ans. Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
Dictionaries are written with curly brackets, and have keys and values:


Q37. How can the ternary operators be used in python?
ans. ternary operator in python is used to return a value based on the result of a binary condition. It takes binary value(condition) as
 an input, so it looks similar to an “if-else” condition block. However, it also returns a value so behaving similar to a function


Q38. What does this mean: *args, **kwargs? And why would we use it?
ans. *args - *args in function definitions in python is used to pass a variable number of arguments to a function. It is used to pass a
 non-key worded, variable-length argument list. The syntax is to use the symbol * to take in a variable number of arguments; by
  convention, it is often used with the word args
  
  **kwargs -  **kwargs passes variable number of keyword arguments dictionary to function on which operation of a dictionary can be
   performed

Q39. What does len() do?
ans. The len() function returns the number of items in an object. When the object is a string, the len() function returns the number of
 characters in the string.



Q40. Explain split(), sub(), subn() methods of “re” module in Python.
ans : sub() – finds all substrings where the regex pattern matches and then replace them with a different string. 
split() – uses a regex pattern to “split” a given string into a list. 
subn() – being similar to sub() it also returns the new string along with the number of replacement


Q41. What are negative indexes and why are they used?
ans . Negative indexes are a way to allow you to index into a list, tuple or other indexable container relative to the end of the
 container, rather than the start. They are use d because they are more efficient and are considered by much more readable.


Q42. What are Python packages?
ans . A python package is a collection of modules. Modules that are related to each other are mainly put in the same package. When a
 module from an external package is required in a program, that package can be imported and its modules can be put to use. Any Python
 file, whose name is the module's name property without the .
 

Q43.How can files be deleted in Python?
ans.To delete a file in Python, you need to import the OS Module. After that, you need to use the os.remove() function.

Example:

1
2
import os
os.remove("xyz.txt")




Q44. What are the built-in types of python?
ans. Python uses five numeric types: Booleans, integers, long integers, floating-point numbers, and complex numbers. Except for Booleans,
 all numeric objects are signed. All numeric types are immutable. Booleans are represented by two values: True and False
 
 
Q45. What advantages do NumPy arrays offer over (nested) Python lists?
ans. Python’s lists are efficient general-purpose containers. They support (fairly) efficient insertion, deletion, appending, and concatenation, and Python’s list comprehensions make them easy to construct and manipulate.


They have certain limitations: they don’t support “vectorized” operations like elementwise addition and multiplication, and the fact that they can contain objects of differing types mean that Python must store type information for every element, and must execute type dispatching code when operating on each element.


NumPy is not just more efficient; it is also more convenient. You get a lot of vector and matrix operations for free, which sometimes allow one to avoid unnecessary work. And they are also efficiently implemented.
NumPy array is faster and You get a lot built in with NumPy, FFTs, convolutions, fast searching, basic statistics, linear algebra, histograms, etc. 


Q46. How to add values to a python array?
ans . If you are using List as an array, you can use its append(), insert(), and extend() functions. ...
If you are using array module, you can use the concatenation using the + operator, append(), insert(), and extend() functions to add
 elements to the array.


Q47. How to remove values to a python array?
ans. Use list. pop() to remove an element from a list by index. 
Use the del keyword to remove an element from a list by index. Place the del keyword before the name of a list followed by the index of
 the element to remove in square brackets.
Use list. remove() to remove an element from a list by value.
Use np.


Q48. Does Python have OOps concepts?
ans. Python is an object-oriented programming language. This means that any program can be solved in python by creating an object model.
 However, Python can be treated as procedural as well as structural language.


Q49. What is the difference between deep and shallow copy?
ans.    Shallow copy is used when a new instance type gets created and it keeps the values that are copied in the new instance. Shallow
 copy is used to copy the reference pointers just like it copies the values. These references point to the original objects and the
  changes made in any member of the class will also affect the original copy of it. Shallow copy allows faster execution of the program
   and it depends on the size of the data that is used.
  

Deep copy is used to store the values that are already copied. Deep copy doesn’t copy the reference pointers to the objects. It makes the
 reference to an object and the new object that is pointed by some other object gets stored. The changes made in the original copy won’t
  affect any other copy that uses the object. Deep copy makes execution of the program slower due to making certain copies for each
   object that is been called.


Q50. How is Multithreading achieved in Python?
ans. Python has a multi-threading package but if you want to multi-thread to speed your code up, then it’s usually not a good idea to use
 it.
Python has a construct called the Global Interpreter Lock (GIL). The GIL makes sure that only one of your ‘threads’ can execute at any
 one time. A thread acquires the GIL, does a little work, then passes the GIL onto the next thread


Q51. What is the process of compilation and linking in python?
ans.The compiling and linking allows the new extensions to be compiled properly without any error and the linking can be done only when
 it passes the compiled procedure. If the dynamic loading is used then it depends on the style that is being provided with the system.
  The python interpreter can be used to provide the dynamic loading of the configuration setup files and will rebuild the interpreter.


Q52. What are Python libraries? Name a few of them.
ans. Python libraries are a collection of Python packages. Some of the majorly used python libraries are – Numpy, Pandas, Matplotlib,
 Scikit-learn and many more.



Q53. What is split used for?
ans . The split() method is used to separate a given string in Python.

Example:

1
2
a="edureka python"
print(a.split())
Output:  [‘edureka’, ‘python’]


Q54. How to import modules in python?
ans. Modules can be imported using the import keyword.  You can import modules in three ways-

Example:

1
2
3
import array           #importing using the original module name
import array as arr    # importing using an alias name
from array import *    #imports everything present in the array module


OOPS Python Interview Questions

Q55. Explain Inheritance in Python with an example.
ans. Inheritance allows One class to gain all the members(say attributes and methods) of another class. Inheritance provides code reusability, makes it easier to create and maintain an application. The class from which we are inheriting is called super-class and the class that is inherited is called a derived / child class.

They are different types of inheritance supported by Python:

Single Inheritance – where a derived class acquires the members of a single super class.
Multi-level inheritance – a derived class d1 in inherited from base class base1, and d2 are inherited from base2.
Hierarchical inheritance – from one base class you can inherit any number of child classes
Multiple inheritance – a derived class is inherited from more than one base class.






Q56. How are classes created in Python?
ans. A class is a code template for creating objects. Objects have member variables and have behaviour associated with them. In python a
 class is created by the keyword class .


Q57. What is monkey patching in Python?
ans. In Python, the term monkey patch only refers to dynamic modifications of a class or module at run-time.

Consider the below example:

1
2
3
4
# m.py
class MyClass:
def f(self):
print "f()"
We can then run the monkey-patch testing like this:

1
2
3
4
5
6
7
import m
def monkey_f(self):
print "monkey_f()"
 
m.MyClass.f = monkey_f
obj = m.MyClass()
obj.f()
The output will be as below:

monkey_f()
As we can see, we did make some changes in the behavior of f() in MyClass using the function we defined, monkey_f(), outside of the module m.



Q58. Does python support multiple inheritance?
ans.Multiple inheritance means that a class can be derived from more than one parent classes. Python does support multiple inheritance,
 unlike Java.

Q59. What is Polymorphism in Python?
ans. Polymorphism means the ability to take multiple forms. So, for instance, if the parent class has a method named ABC then the child
 class also can have a method with the same name ABC having its own parameters and variables. Python allows polymorphism.



Q60. Define encapsulation in Python?
ans.  Encapsulation means binding the code and the data together. A Python class in an example of encapsulation.

Q61. How do you do data abstraction in Python?
ans.Data Abstraction is providing only the required details and hiding the implementation from the world. It can be achieved in Python by
 using interfaces and abstract classes.



Q62.Does python make use of access specifiers?
ans.
Python does not deprive access to an instance variable or function. Python lays down the concept of prefixing the name of the variable,
 function or method with a single or double underscore to imitate the behavior of protected and private access specifiers.  
 
 
Q64. What does an object() do?
ans . It returns a featureless object that is a base for all classes. Also, it does not take any parameters.



Programming Questions :

Q65. Write a program in Python to execute the Bubble sort algorithm.
ans.def bubble(a):
    for i in range(len(a)):
        for j in range(i , len(a)-i-1):
            if a[j] > a[j+1] :
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
a  = [5,1,4,2,8]
print(f"before bubble sortting =  {a} ")     
bubble(a)  
print(f"after  bubble sortting =  {a} ") 

output - [1,2,4,5,8] 
   

Q66. Write a program in Python to produce Star triangle.
ans. def pyfunc(r):
    for x in range(r):
        print(' '*(r-x-1)+'*'*(2*x+1))    
pyfunc(9)
Output:

        *
       ***
      *****
     *******
    *********
  


Q67. Write a program to produce Fibonacci series in Python.
ans.

Q68. Write a program in Python to check if a number is prime.
ans.
num = 29

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
flag = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
    
    
    

Q69. Write a program in Python to check if a sequence is a Palindrome.
ans. 
a=input("enter sequence")
b=a[::-1]
if a==b:
  &amp;amp;amp;nbsp; print("palindrome")
else:
  &amp;amp;amp;nbsp; print("Not a Palindrome")
Output:

enter sequence 323 palindrome




Q70. Write a one-liner that will count the number of capital letters in a file. Your code should work even if the file is too big to fit in memory.
ans.Let us first write a multiple line solution and then convert it to one-liner code.


with open(SOME_LARGE_FILE) as fh:
count = 0
text = fh.read()
for character in text:
    if character.isupper():
count += 1
We will now try to transform this into a single line.
count sum(1 for line in fh for character in line if character.isupper())


Q71. Write a sorting algorithm for a numerical dataset in Python.
ans. The following code can be used to sort a list in Python:
list = ["1", "4", "0", "6", "9"]
list = [int(i) for i in list]
list.sort()
print (list)



Q72. Looking at the below code, write down the final values of A0, A1, …An.

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
print(A0,A1,A2,A3,A4,A5,A6)

ans.  The following will be the final outputs of A0, A1, … A6


A0 = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4} # the order may vary
A1 = range(0, 10) 
A2 = []
A3 = [1, 2, 3, 4, 5]
A4 = [1, 2, 3, 4, 5]
A5 = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
A6 = [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]

Python Libraries – Python Interview Questions

Q73. Explain what Flask is and its benefits?
ans.Flask is a web microframework for Python based on “Werkzeug, Jinja2 and good intentions” BSD license. Werkzeug and Jinja2 are two of
 its dependencies. This means it will have little to no dependencies on external libraries.  It makes the framework light while there is
  a little dependency to update and fewer security bugs.

A session basically allows you to remember information from one request to another. In a flask, a session uses a signed cookie so the
 user can look at the session contents and modify. The user can modify the session if only it has the secret key Flask.secret_key.

Q74. Is Django better than Flask?
ans. Django and Flask map the URL’s or addresses typed in the web browsers to functions in Python. 

Flask is much simpler compared to Django but, Flask does not do a lot for you meaning you will need to specify the details, whereas
 Django does a lot for you wherein you would not need to do much work. Django consists of prewritten code, which the user will need to
  analyze whereas Flask gives the users to create their own code, therefore, making it simpler to understand the code. Technically both
   are equally good and both contain their own pros and cons.



Q75. Mention the differences between Django, Pyramid and Flask.
ans. Flask is a “microframework” primarily build for a small application with simpler requirements. In flask, you have to use external
 libraries. Flask is ready to use.
Pyramid is built for larger applications. It provides flexibility and lets the developer use the right tools for their project. The
 developer can choose the database, URL structure, templating style and more. Pyramid is heavy configurable.
Django can also be used for larger applications just like Pyramid. It includes an ORM.




Q76. Discuss Django architecture.
ans.The developer provides the Model, the view and the template then just maps it to a URL and Django does the magic to serve it to the
 user.



Q77. Explain how you can set up the Database in Django.
ans. We will add the following lines of code to the setting.py file:

DATABASES = {
     'default': {
          'ENGINE' : 'django.db.backends.sqlite3',
          'NAME' : os.path.join(BASE_DIR, 'db.sqlite3'),
     }
}


Q78. Give an example how you can write a VIEW in Django?
ans.This is how we can use write a view in Django:
from django.http import HttpResponse
import datetime
 
def Current_datetime(request):
     now = datetime.datetime.now()
     html = "&amp;amp;lt;html&amp;amp;gt;&amp;amp;lt;body&amp;amp;gt;It is now %s&amp;amp;lt;/body&amp;amp;gt;&amp;amp;lt;/html&amp;amp;gt; % now
     return HttpResponse(html)
     

Q79. Mention what the Django templates consist of.
ans. The template is a simple text file.  It can create any text-based format like XML, CSV, HTML, etc.  A template contains variables
 that get replaced with values when the template is evaluated and tags (% tag %) that control the logic of the template.


Q80. Explain the use of session in Django framework?
ans. Django provides a session that lets you store and retrieve data on a per-site-visitor basis. Django abstracts the process of sending
 and receiving cookies, by placing a session ID cookie on the client side, and storing all the related data on the server side.







