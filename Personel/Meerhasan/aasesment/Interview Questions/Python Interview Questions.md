Python Interview Questions :

Q1. What is the difference between list and tuples in Python?
Ans : The difference between list and tuple is that list is mutable while tuple is not. Tuple can be    hashed for e.g as a key for dictionaries.

Q2. What are the key features of Python?
Ans : Key features of pthon are:
Simple
Easy to Learn
Free and Open Source
High-level Language
Portable
            Interpreted
Object Oriented
Extensible
Embeddable

Q3. What type of language is python? Programming or scripting?
Ans : Python is scripting, general-purpose, high-level, and interpreted programming language. It also provides the object-oriented programming approach.

Q4.Python an interpreted language. Explain.
Ans : An interpreted language is any programming language which is not in machine-level code before runtime. Therefore, Python is an interpreted language.

Q5.What is pep 8?
Ans : PEP stands for Python Enhancement Proposal. It is a set of rules that specify how to format Python code for maximum readability.

Q6. How is memory managed in Python?
Ans : Memory management in Python involves a private heap containing all Python objects and data structures. The management of this private heap is ensured internally by the Python memory manager.

Q7. What is namespace in Python?
Ans : A namespace is a system that has a unique name for each and every object in Python. An object might be a variable or a method. Python itself maintains a namespace in the form of a Python dictionary. Let's go through an example, a directory-file system structure in computers.



Q8. What is PYTHONPATH?
Ans : It is an environment variable which is used when a module is imported. Whenever a module is imported, PYTHONPATH is also looked up to check for the presence of the imported modules in various directories. The interpreter uses it to determine which module to load.

Q9. What are python modules? Name some commonly used built-in modules in Python?
Ans : Python modules are files containing Python code. This code can either be functions classes or variables. A Python module is a .py file containing executable code.
Some of the commonly used built-in modules are:
    • os
    • sys
    • math
    • random
    • data time
    • JSON

Q10.What are local variables and global variables in Python?
Ans : The scope of global variables is the entire program whereas the scope of local variable is limited to the function where it is defined.

Q11. Is python case sensitive?
Ans : Yes. Python is a case sensitive language.

Q12.What is type conversion in Python?
Ans : Type conversion refers to the conversion of one data type iinto another.
int() – converts any data type into integer type
float() – converts any data type into float type
ord() – converts characters into integer
hex() – converts integers to hexadecimal
oct() – converts integer to octal
tuple() – This function is used to convert to a tuple.
set() – This function returns the type after converting to set.
list() – This function is used to convert any data type to a list type.
dict() – This function is used to convert a tuple of order (key,value) into a dictionary.
str() – Used to convert integer into a string.

Q13. How to install Python on Windows and set path variable?
Ans : To install Python on Windows, follow the below steps:

1. Install python from this link: https://www.python.org/downloads/
2. After this, install it on your PC. Look for the location where PYTHON has been installed on your PC using the following command on your command prompt: cmd python. 
3. Then go to advanced system settings and add a new variable and name it as PYTHON_NAME and paste the copied path.
4. Look for the path variable, select its value and select ‘edit’.
5. Add a semicolon towards the end of the value if it’s not present and then type %PYTHON_HOME%

Q14. Is indentation required in python?
Ans : Indentation is necessary for Python. It specifies a block of code. All code within loops, classes, functions, etc is specified within an indented block. It is usually done using four space characters. If your code is not indented necessarily, it will not execute accurately and will throw errors as well.

Q15. What is the difference between Python Arrays and lists?
Ans : Arrays and lists, in Python, have the same way of storing data. But, arrays can hold only a single data type elements whereas lists can hold any data type elements.

Q16. What are functions in Python?
Ans : A function is a block of code which is executed only when it is called. To define a Python Function,  the def keyword is used.

Q17.What is __init__?
Ans : __init__ is a method or constructor in Python. This method is automatically called to allocate memory when a new object/ instance of a class is created. All classes have the __init__ method.

Q18.What is a lambda function?
Ans : An anonymous function is known as a lambda function. This function can have any number of parameters but, can have just one statement.

Q19. What is self in Python?
Ans : An instance of a class or an object is self in Python. It is included as the first parameter. It helps to differentiate between the methods and attributes of a class with local variables.

Q20. How does break, continue and pass work?
Ans : Break : This statements are use to terminate loop when condition gets true.

 Continue : The continue keyword is used to end the current iteration in a for loop (or a while loop), and continues to the next iteration.

 Pass : pass is a null statement. The interpreter does not ignore a pass statement, but nothing happens and the statement results into no operation. 

Q21. What does [::-1} do?
Ans :  [::-1] is used to reverse the order of an array or a sequence.

Q22. How can you randomize the items of a list in place in Python?

Q23. What are python iterators?
Ans : An iterator is an object that can be iterated upon, meaning that you can traverse through all the values. ... Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__() .

Q24. How can you generate random numbers in Python?
Ans : Using random(), we can generate random integers(numbers) in python.

Q25. What is the difference between range & xrange?
Ans : As range() returns the list, all the operations that can be applied on the list can be used on it. On the other hand, as xrange() returns the xrange object, operations associated to list cannot be applied on them, hence a disadvantage.

Q26. How do you write comments in python?
Ans : Using ‘#’ we can write comment in python.

Q27. What is pickling and unpickling?
Ans : Pickle module accepts any Python object and converts it into a string representation and dumps it into a file by using dump function, this process is called pickling. While the process of retrieving original Python objects from the stored string representation is called unpickling.

Q28. What are the generators in python?
Ans : It is a functions that return an iterable set of items called generators.

Q29. How will you capitalize the first letter of string?
Ans : using capitalize() methon we can capitilize the first letter of a string.

Q30. How will you convert a string to all lowercase?
Ans : To convert a string to lowercase, lower() function can be used.

Q31. How to comment multiple lines in python?Ans : Using triple-quoted string literals we can comment multiple line.

Q32.What are docstrings in Python?
Ans : Docstrings are not actually comments, but, they are documentation strings. These docstrings are within triple quotes. They are not assigned to any variable and therefore, at times, serve the purpose of comments as well.

Q33. What is the purpose of is, not and in operators?
Ans : Operators are special functions. They take one or more values and produce a corresponding result.
is: returns true when 2 operands are true  (Example: “a” is ‘a’)
not: returns the inverse of the boolean value
in: checks if some element is present in some sequence


Q34. What is the usage of help() and dir() function in Python?
Ans : Help() and dir() both functions are accessible from the Python interpreter and used for viewing a consolidated dump of built-in functions. 
    1. Help() function: The help() function is used to display the documentation string and also facilitates you to see the help related to modules, keywords, attributes, etc.
    2. Dir() function: The dir() function is used to display the defined symbols.

Q35. Whenever Python exits, why isn’t all the memory de-allocated?
Ans :Whenever Python exits, especially those Python modules which are having circular references to other objects or the objects that are referenced from the global namespaces are not always de-allocated or freed.
It is impossible to de-allocate those portions of memory that are reserved by the C library.
On exit, because of having its own efficient clean up mechanism, Python would try to de-allocate/destroy every other object.



Q36. What is a dictionary in Python?
Ans :The built-in datatypes in Python is called dictionary. It defines one-to-one relationship between keys and values. Dictionaries contain pair of keys and their corresponding values. Dictionaries are indexed by keys.

Q37. How can the ternary operators be used in python?
Ans : The Ternary operator is the operator that is used to show the conditional statements. This consists of the true or false values with a statement that has to be evaluated for it.

Q38. What does this mean: *args, **kwargs? And why would we use it?
Ans : *args and **kwargs are special keyword which allows function to take variable length argument, **kwargs passes variable number of keyword arguments dictionary to function on which operation of a dictionary can be performed. *args and **kwargs make the function flexible.

Q39. What does len() do?
Ans : The len() function returns the number of items in an object. When the object is a string, the len() function returns the number of characters in the string.

Q40. Explain split(), sub(), subn() methods of “re” module in Python.
Ans : split() – uses a regex pattern to “split” a given string into a list.

sub() – finds all substrings where the regex pattern matches and then replace them with a different string

subn() – it is similar to sub() and also returns the new string along with the no. of replacements.

Q41. What are negative indexes and why are they used?
Ans : Negative indexes are a way to allow you to index into a list, tuple or other indexable container relative to the end of the container, rather than the start. They are use d because they are more efficient and are considered by much more readable.


Q42. What are Python packages?
Ans : Python packages are namespaces containing multiple modules.

Q43.How can files be deleted in Python?
Ans : To delete a file in Python, you need to import the OS Module. After that, you need to use the os.remove() function.

Q44. What are the built-in types of python?
Ans : Built-in types in Python are as follows –
1. Integers
2. Floating-point
3. Complex numbers
4. Strings
5. Boolean
6. Built-in functions

Q45. What advantages do NumPy arrays offer over (nested) Python lists?
Ans : NumPy is the fundamental package for scientific computing in Python. NumPy arrays facilitate advanced mathematical and other types of operations on large numbers of data.

Advantages of using Numpy Arrays Over Python Lists:
    • consumes less memory.
    • fast as compared to the python List.
    • convenient to use.

Q46. How to add values to a python array?
Ans : Elements can be added to an array using the append(), extend() and the insert (i,x) functions.

Q47. How to remove values to a python array?
Ans : Array elements can be removed using pop() or remove() method. The difference between these two functions is that the former returns the deleted value whereas the latter does not.
Q48. Does Python have OOps concepts?
Ans :  Python is a great programming language that supports OOPs. You will use it to define a class with attributes and methods, which you will then call. Python offers a number of benefits compared to other programming languages

Q49. What is the difference between deep and shallow copy?
Ans : Shallow copy is used when a new instance type gets created and it keeps the values that are copied in the new instance. Shallow copy is used to copy the reference pointers just like it copies the values. These references point to the original objects and the changes made in any member of the class will also affect the original copy of it. Shallow copy allows faster execution of the program and it depends on the size of the data that is used.

Deep copy is used to store the values that are already copied. Deep copy doesn’t copy the reference pointers to the objects. It makes the reference to an object and the new object that is pointed by some other object gets stored. The changes made in the original copy won’t affect any other copy that uses the object. Deep copy makes execution of the program slower due to making certain copies for each object that is been called.


Q50. How is Multithreading achieved in Python?
Ans : Python has a multi-threading package but if you want to multi-thread to speed your code 	up, then it’s usually not a good idea to use it.
Python has a construct called the Global Interpreter Lock (GIL). The GIL makes sure that only one of your ‘threads’ can execute at any one time. A thread acquires the GIL, does a little work, then passes the GIL onto the next thread. 
This happens very quickly so to the human eye it may seem like your threads are executing in parallel, but they are really just taking turns using the same CPU core. 
All this GIL passing adds overhead to execution. This means that if you want to make your code run faster then using the threading package often isn’t a good idea.

Q51. What is the process of compilation and linking in python?
Ans : Compilation: The source code in python is saved as a . py file which is then compiled into a format known as byte code, byte code is then converted to machine code. This process is known as linking


Q52. What are Python libraries? Name a few of them.
Ans :Python libraries are a collection of Python packages. Some of the majorly used python libraries are TensorFlow, Scikit-Learn, Numpy, Keras, SciPy and many more.

Q53. What is split used for?
Ans : The split() method is used to separate a given string in Python.

Q54. How to import modules in python?
Ans : The import statement is the most common way of invoking the import machinery, but it is not the only way.      
1. import module_name. When import is used, it searches for the module initially in the local scope by calling __import__() function. ...     
2. import module_name.member_name    
3. from module_name import *

OOPS Python Interview Questions

Q55. Explain Inheritance in Python with an example.
Ans : Inheritance is a powerful feature in object oriented programming.
It refers to defining a new class with little or no modification to an existing class. The new class is called derived (or child) class and the one from which it inherits is called the base (or parent) class


Q56. How are classes created in Python?
Ans : Class creates a user-defined data structure, which holds its own data members and member functions, which can be accessed and used by creating an instance of that class. A class is like a blueprint for an object. Some points on Python class: Classes are created by keyword class
ex : 
class a :
    def __init__(self,a) :
           self.a = a
ob = a(“hello”)
print(ob.a)
   
Q57. What is monkey patching in Python?
Ans : Monkey patching can only be done in dynamic languages, of which python is a good example. Changing a method at runtime instead of updating the object definition is one example;similarly, adding attributes (whether methods or variables) at runtime is considered monkey patching

Q58. Does python support multiple inheritance?
Ans : Multiple inheritance: When a child class inherits from multiple parent classes, it is called multiple inheritance. Unlike Java and like C++, Python supports multiple inheritance.

Q59. What is Polymorphism in Python?
Ans : Polymorphism means the ability to take multiple forms. So, for instance, if the parent class has a method named ABC then the child class also can have a method with the same name ABC having its own parameters and variables. Python allows polymorphism.

Q60. Define encapsulation in Python?
Ans : Encapsulation means binding the code and the data together. A Python class in an example of encapsulation.

Q61. How do you do data abstraction in Python?
Ans : Data Abstraction is providing only the required details and hiding the implementation from the world. It can be achieved in Python by using interfaces and abstract classes.

Q62.Does python make use of access specifiers?
Ans : Python does not deprive access to an instance variable or function. Python lays down the concept of prefixing the name of the variable, function or method with a single or double underscore to imitate the behavior of protected and private access specifiers. 

Q64. What does an object() do?
Ans :  It returns a featureless object that is a base for all classes. Also, it does not take any parameters.





Programming Questions :

Q65. Write a program in Python to execute the Bubble sort algorithm.
Ans : Done
Q66. Write a program in Python to produce Star triangle.
Ans : Done 
Q67. Write a program to produce Fibonacci series in Python.
Ans : Done 
Q68. Write a program in Python to check if a number is prime.
Ans : Done 
Q69. Write a program in Python to check if a sequence is a Palindrome.
Ans : Done 
Q70. Write a one-liner that will count the number of capital letters in a file. Your code should work even if the file is too big to fit in memory.
Ans : Done 
Q71. Write a sorting algorithm for a numerical dataset in Python.
Ans : Done 
Q72. Looking at the below code, write down the final values of A0, A1, …An.
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
print(A0,A1,A2,A3,A4,A5,A6)





Python Libraries – Python Interview Questions

Q73. Explain what Flask is and its benefits?
Ans : Image result for Explain what Flask is and its benefits? Flask allows you to build a web application by providing tools, libraries, and technologies. This web application will be a web page, a wiki, or a big web-based calendar application or commercial website. Flask is classified into a micro-framework that means it has little to no dependencies on external libraries.

Q74. Is Django better than Flask?
Ans : Django is considered to be more popular because it provides many out of box features and reduces time to build complex applications. Flask is a good start if you are getting into web development. There are many websites built on the flask and gain heavy traffic, but not as much compared to the ones in Django.

Q75. Mention the differences between Django, Pyramid and Flask.
Ans :  1) Flask is a “microframework” primarily build for a small application with simpler 	requirements. In flask, you have to use external libraries. Flask is ready to use.
2) Pyramid is built for larger applications. It provides flexibility and lets the developer use the right tools for their project. The developer can choose the database, URL structure, templating style and more. Pyramid is heavy configurable.

3) Django can also be used for larger applications just like Pyramid. It includes an ORM.

Q76. Discuss Django architecture.
Ans : Django is based on MVT (Model-View-Template) architecture. MVT is a software design pattern for developing a web application. MVT Structure has the following three parts – Model: Model is going to act as the interface of your data. It is responsible for maintaining data.

Q77. Explain how you can set up the Database in Django.
Ans : You can use the command edit mysite/setting.py, it is a normal python module with module level representing Django settings.
Django uses SQLite by default; it is easy for Django users as such it won’t require any other type of installation. In the case your database choice is different that you have to the following keys in the DATABASE ‘default’ item to match your database connection settings.
    • Engines: you can change the database by using ‘django.db.backends.sqlite3’ , ‘django.db.backeneds.mysql’, ‘django.db.backends.postgresql_psycopg2’, ‘django.db.backends.oracle’ and so on
    • Name: The name of your database. In the case if you are using SQLite as your database, in that case, database will be a file on your computer, Name should be a full absolute path, including the file name of that file.
    • If you are not choosing SQLite as your database then settings like Password, Host, User, etc. must be added.
Django uses SQLite as a default database, it stores data as a single file in the filesystem. If you do have a database server—PostgreSQL, MySQL, Oracle, MSSQL—and want to use it rather than SQLite, then use your database’s administration tools to create a new database for your Django project. Either way, with your (empty) database in place, all that remains is to tell Django how to use it. This is where your project’s settings.py file comes in.

Q78. Give an example how you can write a VIEW in Django?
Ans :  First, we import the class HttpResponse from the django. http module, along with 	Python's datetime library.     
	Next, we define a function called current_datetime . This is the view function.   
	The view returns an HttpResponse object that contains the generated response.
Q79. Mention what the Django templates consist of.
Ans : The template is a simple text file.  It can create any text-based format like XML, CSV, HTML, etc.  A template contains variables that get replaced with values when the template is evaluated and tags (% tag %) that control the logic of the template.

Q80. Explain the use of session in Django framework?
Ans : Django provides a session that lets you store and retrieve data on a per-site-visitor basis. Django abstracts the process of sending and receiving cookies, by placing a session ID cookie on the client side, and storing all the related data on the server side.

Q81. List out the inheritance styles in Django.
Ans : In Django, there are three possible inheritance styles:
Abstract Base Classes: This style is used when you only want parent’s class to hold information that you don’t want to type out for each child model.

Multi-table Inheritance: This style is used If you are sub-classing an existing model and need each model to have its own database table.

Proxy models: You can use this model, If you only want to modify the Python level behavior of the model, without changing the model’s fields.



