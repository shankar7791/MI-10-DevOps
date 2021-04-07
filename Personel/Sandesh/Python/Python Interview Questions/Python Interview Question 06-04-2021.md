Q31. How to comment multiple lines in python?
Ans : Ways to achieve multiline comments in Python

    Consecutive Single line commentby using (#) eg . #sandesh 
    Using Multi-line string as comment by using (""") eg. """Comment statement """
    
Q32.What are docstrings in Python?
Ans : Python documentation strings (or docstrings) provide a convenient way of associating documentation with Python modules, functions, classes, and methods. It's specified in source code that is used, like a comment, to document a specific segment of code. The docstrings are declared using ”’triple single quotes”’ or “””triple double quotes””” just below the class, method or function declaration. All functions should have a docstring.

Q33. What is the purpose of is, not and in operators?
Ans : in and not in are the membership operators in Python. They are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary). In a dictionary we can only test for presence of key, not the value.

Q34. What is the usage of help() and dir() function in Python?
Ans : Help() and dir(), are the two functions that are reachable from the python interpreter. Both functions are utilized for observing the combine dump of build-in-function. These created functions in python are truly helpful for the efficient observation of the built-in system.

Q35. Whenever Python exits, why isn’t all the memory de-allocated?
Ans : When Python exit, the object referenced from global namespaces of Python modules are not always deallocated. So, Python doesn't recognize and free circular memory references before using the garbage collector.

Q36. What is a dictionary in Python?
Ans :A Dictionary in Python is the unordered and changeable collection of data values that holds key-value pairs. A Dictionary in python is declared by enclosing a comma-separated list of key-value pairs using curly braces({}). Python Dictionary is classified into two elements: Keys and Values.

Q37. How can the ternary operators be used in python?
Ans : the ternary operator in python is used to return a value based on the result of a binary condition. It takes binary value(condition) as an input, so it looks similar to an “if-else” condition block. However, it also returns a value so behaving similar to a function.

 Q38. What does this mean: *args, **kwargs? And why would we use it?
Ans : The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function. It is used to pass a non-key worded, variable-length argument list. 
      The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star. The reason is because the double star allows us to pass through keyword arguments (and any number of them).
      
Q39. What does len() do?
Ans : it is used to determine the length of a string, a list, an array, etc.

Q40. Explain split(), sub(), subn() methods of “re” module in Python.
Ans :  sub() – finds all substrings where the regex pattern matches and then replace them with a different string. split() – uses a regex pattern to “split” a given string into a list. subn() – being similar to sub() it also returns the new string along with the number of replacements.

Q41. What are negative indexes and why are they used?
Ans : The negative index is used to remove any new-line spaces from the string and allow the string to except the last character that is given as S[:-1]. The negative index is also used to show the index to represent the string in correct order.

Q42. What are Python packages?
Ans : A python package is a collection of modules. Modules that are related to each other are mainly put in the same package. When a module from an external package is required in a program, that package can be imported and its modules can be put to use.

Q43.How can files be deleted in Python?
Ans : To delete a file in Python, you need to import the OS Module. After that, you need to use the os.remove() function.
Example:
	import os
	os.remove("xyz.txt")
	
Q44. What are the built-in types of python?
Ans:  Built-in types in Python are as follows –
    Integers
    Floating-point
    Complex numbers
    Strings
    Boolean
    Built-in functions
	
Q45. What advantages do NumPy arrays offer over (nested) Python lists?
Ans : Python’s lists are efficient general-purpose containers. They support (fairly) efficient insertion, deletion, appending, and concatenation, and Python’s list comprehensions make them easy to construct and manipulate.
    They have certain limitations: they don’t support “vectorized” operations like elementwise addition and multiplication, and the fact that they can contain objects of differing types mean that Python must store type information for every element, and must execute type dispatching code when operating on each element.
    NumPy is not just more efficient; it is also more convenient. You get a lot of vector and matrix operations for free, which sometimes allow one to avoid unnecessary work. And they are also efficiently implemented.
    NumPy array is faster and You get a lot built in with NumPy, FFTs, convolutions, fast searching, basic statistics, linear algebra, histograms, etc.
    
Q46. How to add values to a python array?
Ans : Elements can be added to an array using the append(), extend() and the insert (i,x) functions.

Q47. How to remove values to a python array?
Ans : Array elements can be removed using pop() or remove() method. The difference between these two functions is that the former returns the deleted value whereas the latter does not.

Q48. Does Python have OOps concepts?
Ans : Python is an object-oriented programming language. This means that any program can be solved in python by creating an object model. However, Python can be treated as procedural as well as structural language.

Q49. What is the difference between deep and shallow copy?
Ans : Shallow copy is used when a new instance type gets created and it keeps the values that are copied in the new instance. Shallow copy is used to copy the reference pointers just like it copies the values. These references point to the original objects and the changes made in any member of the class will also affect the original copy of it. Shallow copy allows faster execution of the program and it depends on the size of the data that is used.
      Deep copy is used to store the values that are already copied. Deep copy doesn’t copy the reference pointers to the objects. It makes the reference to an object and the new object that is pointed by some other object gets stored. The changes made in the original copy won’t affect any other copy that uses the object. Deep copy makes execution of the program slower due to making certain copies for each object that is been called.

Q50. How is Multithreading achieved in Python?
Ans:Python has a multi-threading package but if you want to multi-thread to speed your code up, then it’s usually not a good idea to use it.
    Python has a construct called the Global Interpreter Lock (GIL). The GIL makes sure that only one of your ‘threads’ can execute at any one time. A thread acquires the GIL, does a little work, then passes the GIL onto the next thread.
    This happens very quickly so to the human eye it may seem like your threads are executing in parallel, but they are really just taking turns using the same CPU core.
    All this GIL passing adds overhead to execution. This means that if you want to make your code run faster then using the threading package often isn’t a good idea.

Q51. What is the process of compilation and linking in python?
Ans: The compiling and linking allows the new extensions to be compiled properly without any error and the linking can be done only when it passes the compiled procedure. If the dynamic loading is used then it depends on the style that is being provided with the system. The python interpreter can be used to provide the dynamic loading of the configuration setup files and will rebuild the interpreter.

The steps that are required in this as:

    Create a file with any name and in any language that is supported by the compiler of your system. For example file.c or file.cpp
    Place this file in the Modules/ directory of the distribution which is getting used.
    Add a line in the file Setup.local that is present in the Modules/ directory.
    Run the file using spam file.o
    After a successful run of this rebuild the interpreter by using the make command on the top-level directory.
    If the file is changed then run rebuildMakefile by using the command as ‘make Makefile’.

Q52. What are Python libraries? Name a few of them.
Ans : Python libraries are a collection of Python packages. Some of the majorly used python libraries are – Numpy, Pandas, Matplotlib, Scikit-learn and many more.

Q53. What is split used for?
Ans : The split() method is used to separate a given string in Python.


Q54. How to import modules in python?

Ans  : Modules can be imported using the import keyword. You can import modules in three ways-






    
    
    
    
