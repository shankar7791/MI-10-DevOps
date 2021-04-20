Python Interview Questions :

Q1. What is the difference between list and tuples in Python?
Ans: 1. list is mutable ,              tuple is immutable
    2. list takes elemnt in [] ,   tuple takes element in () round bracket
    3. consumes less memory         consumes more memory


Q2. What are the key features of Python?
Ans: Free and Open Source
    Easy to code
    Portable language
     Object-Oriented Language
   	GUI Programming Support
    High-Level Language

Q3. What type of language is python? Programming or scripting?
Ans: Python is Scripting Language.

Q4.Python an interpreted language. Explain.
Ans:It complie without a program into machine instruction.
Python is an interpreted language, This means it uses an interpreter.
Interpreter executes the statements of code one-by-one. That's why python shows only one error message even though your code has multiple errors.

Q5.What is pep 8?
Ans: PEP 8, design to help python Developer. 
The primary focus of PEP 8 is to improve the readability and consistency of Python code. 
PEP stands for Python Enhancement Proposal.

Q6. How is memory managed in Python?
Ans:The Python memory manager manages Python’s memory allocations. 
There’s a private heap that contains all Python objects and data structures. 
The Python memory manager manages the Python heap on demand. 
The Python memory manager has object-specific allocators to allocate memory distinctly for specific objects such as int, string, etc


Q7. What is namespace in Python?
Ans: A namespace is a system that has a unique name for each and every object in Python. An object might be a variable or a method. Python itself maintains a namespace in the form of a Python dictionary. Let’s go through an example, a directory-file system structure in computers

Q8. What is PYTHONPATH?
Ans:  PYTHONPATH is an environment variable which you can set to add additional directories where python will look for modules and packages. For most installations, you should not set these variables since they are not needed for Python to run. Python knows where to find its standard library.


Q9. What are python modules? Name some commonly used built-in modules in Python?
Ans: A module is a file containing Python definitions and statements. 
A module can define functions, classes, and variables.
.py is called python modules.
It is used to break down large program into small manegable and organized files.

Operator: This module provides a set of pre-defined functions corresponding to operators in Python.

math: Math module is used to perform mathematical operations.
This module provides some pre-defined mathematical functions like sqrt, factorial, etc.

string : string module provides a set of functions that are used to perform certain operations on characters.
This module has pre-defined functions like capwords, ascii_letters, etc.


Q10.What are local variables and global variables in Python?
Ans:
Local Variable: A variable declared inside the function's body or in the local scope is known as a local variable.

Global Vaiable: In Python, a variable declared outside of the function or in global scope is known as a global variable. This means that a global variable can be accessed inside or outside of the function.

Example: 
x=10
def python():
	y=11
python()

explaination: x is global variable and y is local its scope decide the it is local or global.


Q11. Is python case sensitive?
Ans: 
Yes, Python is case Sensitive.


Q12.What is type conversion in Python?
Ans: Type Conversion is the conversion of object from one data type to another data type.  
Python automatically converts one data type to another data type. This process doesn't need any user involvement.

Explicit :Type Conversion is also called Type Casting, the data types of objects are converted using predefined functions by the user.
We use the predefined functions like int(), float(), str(), etc to perform explicit type conversion.
Implict : Complier converts one data into another type of data automatically.
there is no data loss.

Q13. How to install Python on Windows and set path variable?
Ans: Installers are available for download - two each for the 32-bit and 64-bit versions of the interpreter.
You need to download package of python. 
Then install this into your system.
Then set path:
Right-clicking This-PC and going to Properties.
    1. Clicking on the Advanced system settings in the menu on the left.
    2. Clicking on the Environment Variables button on the bottom right.
    3. In the System variables section, selecting the Path variable and clicking on Edit.
    4. Clicking on New and entering Python's install directory.
    5. Pate the path of python i.e where python is installed.

Q14. Is indentation required in python?
Ans: Yes, Indentation is important in python.

Q15. What is the difference between Python Arrays and lists?
Ans:
List: A list in Python is a collection of items which can contain elements of multiple data types, which may be either numeric, character logical values, etc. A list can be created using [] containing data values.
Example:
sample_list = [1,"Python",['a','e']]
print(sample_list)


Array: An array is a vector containing homogeneous elements i.e. belonging to the same data type. Elements are allocated with contiguous memory locations allowing easy modification, that is, addition, deletion, accessing of elements. In Python, we have to use the array module to declare arrays. If the elements of an array belong to different data types, an exception “Incompatible data types” is thrown.

Example: 
import array
sample_array = array.array('i', [1, 2, 3])
for i in sample_array:       #accessing elements of array
	print(i)


Q16. What are functions in Python?
Ans: A function is a block of organized, reusable code that is used to perform a single, related action. As you already know, Python gives you many built-in functions like print(), etc. but you can also create your own functions.
Using “def” Keyword and parathisis ()
i.e def function_name():
	///write function defination
     function_name()  //This is function calling you need to call function compulsary.

Q17.What is __init__?
Ans:
"__init__" is a reseved method in python classes. 
It is called as a constructor in object oriented terminology. 
This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.


Q18.What is a lambda function?
Ans:In Python, a lambda function is a single-line function declared with no name, which can have any number of arguments, but it can only have one expression.
Syntax: lambda arguments : expression
Example: x = lambda a, b, c : a + b + c
                print(x(5, 6, 2)) 

Q19. What is self in Python?
Ans: self represents the instance of the class. By using the “self” keyword we can access the attributes and methods of the class in python.

Example:
class Person:
	def __init__(self, name, age):
	self.name = name
	slelf.age = age

p1 = Person("name", 36)

Q20. How does break, continue and pass work?
Ans: These all are Control statemnet:
break: The break statement in Python terminates the current loop and resumes execution at the next statement.

continue: continue statement is opposite to that of break statement, instead of terminating the loop, it forces to execute the next iteration of the loop.

pass:As the name suggests pass statement simply does nothing. The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute. It is like null operation, as nothing will happen is it is executed.
If you want the funtion become empty so wite path inside function 

Q21. What does [::-1} do?
Ans:  It reverse a string.

Q22. How can you randomize the items of a list in place in Python?
Ans: Shuffle a List
    1. Create a list. Create a list using a list() constructor. ... 
    2. Import random module. Use a random module to perform the random generations on a list.
    3. Use the shuffle() function of a random module.
    4. Display the shuffled list.
    5. Get shuffled list instead of modifying the original list. 
    6. Customize the shuffling if needed.


Q23. What are python iterators?
Ans:Iterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets. The iterator object is initialized using the iter() method. It uses the next() method for iteration.

for loop is also iterator in python.

Q24. How can you generate random numbers in Python?
Ans: Random integer values can be generated with the randint() function. 
This function takes two arguments: the start and the end of the range for the generated integer values. 


Q25. What is the difference between range & xrange?
Ans:  range() – This returns a range object (a type of iterable).
xrange() – This function returns the generator object that can be used to display numbers only by looping.