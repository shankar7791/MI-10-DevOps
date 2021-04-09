Python Interview Questions :

Q1. What is the difference between list and tuples in Python?
        List                                Tuples
List is Mutable                       Tuples Are immutable
List can be changed                   Tuple cannot be changed
and modified					they are constant

Q2. What are the key features of Python?
        Easy to code : python is high level programming programming.
        Free and Open source : 
        Object Oriented Programming Language
        GUI Programming Support
        Python is portable language
        python is interpreted 

Q3. What type of language is python? Programming or scripting?
	Yes, Python is scripting,general purpose programming language,high level and interpreted programming language.It also provides the object oriented programming approach.
	
Q4.Python an interpreted language. Explain.
	Python is an interpretd language this means thats is uses interpreter.An interpreter executes the code line by line,whereas the compiler runs the code directly and list all possible errors at a time.

Q5.What is pep 8?
     Pep8 sometimes is called PEP8 or PEP-8 is a document that provides guidelines and practices on how to write python code.

Q6. How is memory managed in Python?
	Python involves a Private heap and containing all python object and data structures.
The management of this private heap space is managed by python memory management.

Q7. What is namespace in Python?
	A namespace in python ensures that object names in a programme are a unique and can be used without conflict
python implement these namespace as dictionaries with name as key mapped to a corresponding object as value.

Q8. What is PYTHONPATH?
	Pythonpath is an environment variable which you can set to add additional directories where python will look for module and packages.

Q9. What are python modules? Name some commonly used built-in modules in Python?
      	A module is a python object with arbitarily named attributes that you can bind and referance.module is file consistency in python code.a module can define function,classes and variables.
Os Module
sys Module
math module
statistic Module


Q10.What are local variables and global variables in Python?
	The scope of global variable is the netire program whereas the scope of local variable is limited to the function where it is defined.

Q11. Is python case sensitive?
	Python is case sensitive language.this means the variable and variable ar not same.
Always give the identifier a name that make sense.

Q12.What is type conversion in Python?
	Type conversion is the conversion of object from one data type to another data type.

Q13. How to install Python on Windows and set path variable?
	Right click on pc and go to properties
	click on the advanced system setting 
	click on the environment vairable
	in system variable selecting path variable and edit
	click on new and enter python install directories.
	
Q14. Is indentation required in python?
	To indicate a block of code in python,You must indent each line of block by the same amount.in other programming languages indentation is used only to help make the code look preety.But in python it is required for indicating block of code a statements belong to.

Q15. What is the difference between Python Arrays and lists?
	
                        List 
                           Array
Can consist of elements  belonging of different data types
Only consisting elements belongs to same data type
Cannot directly handled arithmetic operations
Can directly handled arithmetic operation
Preferred for shorter sequene of data
Preferred for longer sequence of data

Q16. What are functions in Python?
	A function is a block of organize reusable code that is used to perform single related 
action.python gives you many built in functions like print() etc.

Q17.What is __init__?
	Init is reserved method in python.in oop it is known as constructor.the init method can be called when an object is created from the class and access is required to intialize the attribute of class.

Q18.What is a lambda function?
	In python, lambda function is a single line function with no name which can have any number of argument,but it can only have one expression.

Q19. What is self in Python?
	Self represent the instance of class.by using the self keyword we can access the attributes and methods of the class in python.

Q20. How does break, continue and pass work?
	Pass : lets start with something relatively easy.nothing happens when pass is executed.
	Break : the break statement allows you to leave for or while loop immediately.
	Continue : the continue statement ignores the rest of the statements inside a loop and continues to next iteration of loop.

Q21. What does [::-1] do ?
	It is slicing operator and it reversed the string numbers.

Q22. How can you randomize the items of a list in place in Python?
	To randomely shuffle elements of list ,string and tuples in python use the random module.randomes use the shuffle() and shuffle the  original list in place sample() retunrs the new list that is randomly shuffled.
	
Q23. What are python iterators?
	An iterator is an object that can be iterated upon.that you can travese through all the elements.

Q24. How can you generate random numbers in Python?
	Random integer values can be genrated with randint() function.this function takes two arguments.the start and the end of the range for the genrated integer values.

Q25. What is the difference between range & xrange?
	
                       range
                            xrange
As range returns the list
As xrange() returns the object
Operations on list that can be applied on other hand
Operations associated with list cannot be changed.


Q26. How do you write comments in python?
	A comment in python start with hash character.

Q27. What is pickling and unpickling?
	Pickling  : It is a process where a python object hierarchy is converted int byte stream.
	Unpickling : It is the inverse of pickling process where a byte steam is converted into object hierarchy.

Q28. What are the generators in python?
	Python generators are a simple way of creating iterators.All the work we mentioned above are automatically handled by generators of python.

Q29. How will you capitalize the first letter of string?
	The capitalize() method is returns the original string of python and converts the first character of python to a capital letter.

Q30. How will you convert a string to all lowercase?
	The toLowercase() method converts a string to all lowercase letters.

Q31. How to comment multiple lines in python?
	Using tripled  quoted string letters we do the multiple line comments.

Q32.What are docstrings in Python?
	Python documentation string provides a convenient way of associating documetation with python modules,functions ,classes and methods.

Q33. What is the purpose of is, not and in operators?
	In and not is membership operators of python.they are used to test whether a value or variable is found in sequence.

Q34. What is the usage of help() and dir() function in Python?
	Help() and Dir() are the two functionsthat are reachable from the python interpreter.Both functions are utilized for observing the combine dump of built in function.

Q35. Whenever Python exits, why isn’t all the memory de-allocated?
	When python exit,the object referenced from global namespace of python modules are not always deallocated.
Q36. What is a dictionary in Python?
	Dictionaries are pythons implementations of a data structure that is more generally known as an associative array. A dictionary consist of key value pairs.

Q37. How can the ternary operators be used in python?
	Ternary operators also known as conditional expressions are operators that evaluate.it is based on condition being true or false.it was added in python version 2.5.

Q38. What does this mean: *args, **kwargs? And why would we use it?
	The special syntax **kwargs in a function definition is used to pass a keyworded, variable-length argument list. **kwargs allows you to pass keyworded variable length of arguments to a function. ... *args can be used to unpack values from iterable objects(list, tuple) in Python.

Q39. What does len() do?
	len() function is returns the number of objects in the list.when len() have string it returns the size of string.

Q40. Explain split(), sub(), subn() methods of “re” module in Python.
	split() : it splits string into a list splitting it wherever RE matches.
	sub() : find all substring where RE matches,and replace them with a different string.
	subn() : does the same thing as sub().but returns the new string and the number of replacements.

Q41. What are negative indexes and why are they used?
	The negative indexes are used to remove new line spaces.from the string and allow the string to except the last character that is given as s[::-1].

Q42. What are Python packages?
	A python packages is a collection of modules.modules that are related to each other
Are mainly put in the same module.

Q43.How can files be deleted in Python?
	Open a python file window
	Type this code import os os.remove(“changedfile.csv”) print(“file removed”)
	Run module 

Q44. What are the built-in types of python?
	The principal built-in types are numerics, sequences, mappings, classes, instances and exceptions. Some collection classes are mutable

Q45. What advantages do NumPy arrays offer over (nested) Python lists?
	Python's lists are efficient general-purpose containers. They support (fairly) efficient insertion, deletion, appending, and concatenation, and Python's list comprehensions make them easy to construct and manipulate.
	
Q46. How to add values to a python array?
	If you are using a list then you can use append(),insert() and extend() functions.
	If you are using a python array module then you can use the concatenation using the + operator, append(),insert(),extend () usend to add the elements.

Q47. How to remove values to a python array?
	Use list.pop() to remove an element from a list of index.
	Use the del keyword to remove an element from a list of index.
	Use the list.remove() an element by index of list of value.

Q48. Does Python have OOps concepts?
	Major OOP concepts in python include class ,object ,method ,inheritance,polymorphism,data abstraction, and encapsulation.

Q49. What is the difference between deep and shallow copy?
	
                  Deep copy
                  Shallow copy
A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original
A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.

Q50. How is Multithreading achieved in Python?
	Multithreading in Python can be achieved by importing the threading module. Now that you have threading module installed, let us move ahead and do Multithreading in Python.

Q51. What is the process of compilation and linking in python?

Q52. What are Python libraries? Name a few of them.

Q53. What is split used for?

Q54. How to import modules in python?


OOPS Python Interview Questions

Q55. Explain Inheritance in Python with an example.

Q56. How are classes created in Python?

Q57. What is monkey patching in Python?

Q58. Does python support multiple inheritance?

Q59. What is Polymorphism in Python?

Q60. Define encapsulation in Python?

Q61. How do you do data abstraction in Python?

Q62.Does python make use of access specifiers?

Q64. What does an object() do?

Programming Questions :

Q65. Write a program in Python to execute the Bubble sort algorithm.

Q66. Write a program in Python to produce Star triangle.

Q67. Write a program to produce Fibonacci series in Python.

Q68. Write a program in Python to check if a number is prime.

Q69. Write a program in Python to check if a sequence is a Palindrome.

Q70. Write a one-liner that will count the number of capital letters in a file. Your code should work even if the file is too big to fit in memory.

Q71. Write a sorting algorithm for a numerical dataset in Python.

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

Q74. Is Django better than Flask?

Q75. Mention the differences between Django, Pyramid and Flask.

Q76. Discuss Django architecture.

Q77. Explain how you can set up the Database in Django.

Q78. Give an example how you can write a VIEW in Django?

Q79. Mention what the Django templates consist of.

Q80. Explain the use of session in Django framework?

Q81.  List out the inheritance styles in Django.


