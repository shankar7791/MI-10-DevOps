Python Interview Questions :

Q1. What is the difference between list and tuples in Python?
Ans : 

List:-
                                                             	   
1)It is mutable	                                                
2)The implication of iterations is time-consuming in the list.	
3)Operations like insertion and deletion are better performed.	
4)Consumes more memory.	                                        
5)Many built-in methods are available.	                        
6)Unexpected errors and changes can easily occur in lists.

Tuple:-

1)It is immutable
2)Implications of iterations are much faster in tuples.
3)Elements can be accessed better.
4)Consumes less memory.
5)Does not have many built-in methods.
6)Unexpected errors and changes rarely occur in tuples.


Q2. What are the key features of Python?
Ans :- 
   Easy to code: Python is a high-level programming language.
   Free and Open Source.
   Object-Oriented Language
   GUI Programming Support
   High-Level Language.
   Extensible feature
   Python is Portable language.
   Python is Integrated language



Q3. What type of language is python? Programming or scripting?
Ans :- Yes, Python is scripting, general-purpose, high-level, and interpreted programming language.

Q4. Python an interpreted language. Explain.
Ans :- Python is an “interpreted” language. This means it uses an interpreter. ... An interpreter executes the statements of code “one-by-one” whereas the compiler executes the code entirely and lists all possible errors at a time. That's why python shows only one error message even though your code has multiple errors.

Q5. What is pep 8?
Ans :- PEP8 or PEP-8, is a document that provides guidelines and best practices on how to write Python code The primary focus of PEP 8 is to improve the readability and consistency of Python code. PEP stands for Python Enhancement Proposal, and there are several of them.

Q6. How is memory managed in Python?
Ans:- Memory management in Python involves a private heap containing all Python objects and data structures. The management of this private heap is ensured internally by the Python memory manager.

Q7. What is namespace in Python?
Ans:- A namespace is a system that has a unique name for each and every object in Python. An object might be a variable or a method. Python itself maintains a namespace in the form of a Python dictionary

Q8. What is PYTHONPATH?
Ans:- PYTHONPATH is an environment variable which you can set to add additional directories where python will look for modules and packages. For most installations, you should not set these variables since they are not needed for Python to run. Python knows where to find its standard library.

Q9. What are python modules? Name some commonly used built-in modules in Python?
Ans :-  Modules refer to a file containing Python statements and definitions. A file containing Python code, for example: example.py , is called a module, and its module name would be example . We use modules to break down large programs into small manageable and organized files. 

1)OS Module.
2)Sys Module.
3)Math Module.
4)Statistics Module.
5)Collections Module.
6)Random Module.

Q10.What are local variables and global variables in Python?
Ans :- This means that local variables can be accessed only inside the function in which they are declared, whereas global variables can be accessed throughout the program body by all functions. When you call a function, the variables declared inside it are brought into scope.

Q11. Is python case sensitive?
Ans:- Yes Python is a case-sensitive language which simply means that a variable named as X and a variable named x are two separate variables.

Q12.What is type conversion in Python?
Ans: - Type Conversion is the conversion of object from one data type to another data type



Q13. How to install Python on Windows and set path variable?
Ans: - PATH variable
1.Right-clicking This PC and going to Properties.
2.Clicking on the Advanced system settings in the menu on the left.
3.Clicking on the Environment Variables button o​n the bottom right.
4.In the System variables section, selecting the Path variable and clicking on Edit. ...
5.Clicking on New and entering Python's install directory.


Q14. Is indentation required in python?
Ans: - To indicate a block of code in Python, you must indent each line of the block by the same amount. In most other programming languages, indentation is used only to help make the code look pretty. But in Python, it is required for indicating what block of code a statement belongs to.

Q15. What is the difference between Python Arrays and lists?.
Ans: - 
List	Array
Can consist of elements belonging to different data types	Only consists of elements belonging to the same data type
No need to explicitly import a module for declaration	Need to explicitly import a module for declaration
Cannot directly handle arithmetic operations	Can directly handle arithmetic operations
Can be nested to contain different type of elements	Must contain either all nested elements of same size
Preferred for shorter sequence of data items	Preferred for longer sequence of data items
Greater flexibility allows easy modification (addition, deletion) of data	Less flexibility since addition, deletion has to be done element wise
The entire list can be printed without any explicit looping	A loop has to be formed to print or access the components of array
Consume larger memory for easy addition of elements	Comparatively more compact in memory size



Q16. What are functions in Python?
Ans: - Function in Python is defined by the "def " statement followed by the function name and parentheses ( () ) Example: Let us define a function by using the command " def func1():" and call the function. The output of the function will be "I am learning Python function".

Q17.What is __init__?
Ans :- __init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.

Q18.What is a lambda function?
Ans :  a lambda function is a single-line function declared with no name, which can have any number of arguments, but it can only have one expression. Such a function is capable of behaving similarly to a regular function declared using the Python's def keyword.

Q19. What is self in Python?
Ans : self represents the instance of the class. By using the “self” keyword we can access the attributes and methods of the class in python.

Q20. How does break, continue and pass work?
Ans :- The flow of the code is as shown below: When the while loop executes, it will check the if-condition, if it is true, the continue statement is executed. The control will go back to the start of while –loop for the next iteration. If if the condition is false, the code inside while-loop will get executed

Q21. What does [::-1} do?
Ans: - It iterate over a list in reverse order ….it will start from the last index and reach index = 0 at the last.

Q22. How can you randomize the items of a list in place in Python?
Ans : - import the Python random package by adding the line import random near the top of your program. Then, if you have a list called x, you can call random. shuffle(x) to have the random shuffle function reorder the list in a randomized way. Note that the shuffle function replaces the existing list.

Q23. What are python iterators?
Ans : An iterator is an object that can be iterated upon, meaning that you can traverse through all the values. ... Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__() .


Q24. How can you generate random numbers in Python?
Ans : Random integer values can be generated with the randint() function. This function takes two arguments: the start and the end of the range for the generated integer values. Random integers are generated within and including the start and end of range values, specifically in the interval [start, end]

Q25. What is the difference between range & xrange?
Ans :-  range() – This returns a range object (a type of iterable).
xrange() – This function returns the generator object that can be used to display numbers only by looping. Only particular range is displayed on demand and hence called “lazy evaluation”.

Q26. How do you write comments in python?
Ans:- Comments in Python begin with a hash mark ( # ) 

Q27. What is pickling and unpickling?
Ans:- Pickle module accepts any Python object and converts it into a string representation and dumps it into a file by using dump function, this process is called pickling. While the process of retrieving original Python objects from the stored string representation is called unpickling.

Q28. What are the generators in python?
Ans: - Python generators are a simple way of creating iterators. All the work we mentioned above are automatically handled by generators in Python. Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).

Q29. How will you capitalize the first letter of string?
Ans : the capitalize() method returns a copy of the original string and converts the first character of the string to a capital (uppercase) letter while making all other characters in the string lowercase letters.

Q30. How will you convert a string to all lowercase?
Ans :- lower() method returns the lowercased string from the given string. It converts all uppercase characters to lowercase. If no uppercase characters exist, it returns the original string.
