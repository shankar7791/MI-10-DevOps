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

Q31. How to comment multiple lines in python?
Ans : Using triple-quoted string literals we can comment multiple line.

Q32.What are docstrings in Python?
Ans : Docstrings are not actually comments, but, they are documentation strings. These docstrings are within triple quotes. They are not assigned to any variable and therefore, at times, serve the purpose of comments as well.

