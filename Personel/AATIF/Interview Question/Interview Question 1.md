1) What is Python? What are the benefits of using Python?

Python is a programming language with objects, modules, threads, exceptions and automatic memory management. The benefits of pythons are that it is simple and easy, portable, extensible, build-in data structure and it is an open source.

2) How Python is interpreted?

Python language is an interpreted language. Python program runs directly from the source code. It converts the source code that is written by the 
programmer into an intermediate language, which is again translated into machine language that has to be executed.

3) What are Python decorators?

A Python decorator is a specific change that we make in Python syntax to alter functions easily.

4) What is the difference between list and tuple?

The difference between list and tuple is that list is mutable while tuple is not. Tuple can be hashed for e.g as a key for dictionaries.

5) How are arguments passed by value or by reference?

Everything in Python is an object and all variables hold references to the objects. The references values are according to the functions; as a result you cannot change the value of the references. However, you can change the objects if it is mutable.

6) What is Dict and List comprehensions are?

They are syntax constructions to ease the creation of a Dictionary or List based on existing iterable.

7) What are the built-in type does python provides?

There are mutable and Immutable types of Pythons built in types Mutable built-in types
    • List
    • Sets
    • Dictionaries
Immutable built-in types
    • Strings
    • Tuples
    • Numbers
8) What is namespace in Python?

In Python, every name introduced has a place where it lives and can be hooked for. This is known as namespace. It is like a box where a variable name is mapped to the object placed. Whenever the variable is searched out, this box will be searched, to get corresponding object.

9) What is pass in Python?

Pass means, no-operation Python statement, or in other words it is a place holder in compound statement, where there should be a blank left and nothing has to be written there.

10) In Python what are iterators?

In Python, iterators are used to iterate a group of elements, containers like list.

11) In Python what is slicing?

A mechanism to select a range of items from sequence types like list, tuple, strings etc. is known as slicing.

12) What are generators in Python?

The way of implementing iterators are known as generators. It is a normal function except that it yields expression in the function.

13) What is docstring in Python?

A Python documentation string is known as docstring, it is a way of documenting Python functions, modules and classes.

14) How can you copy an object in Python?

To copy an object in Python, you can try copy.copy () or copy.deepcopy() for the general case. You cannot copy all objects but most of them.

15) What is negative index in Python?

Python sequences can be index in positive and negative numbers. For positive index, 0 is the first index, 1 is the second index and so forth. For negative index, (-1) is the last index and (-2) is the second last index and so forth.

16) How you can convert a number to a string?

In order to convert a number into a string, use the inbuilt function str(). If you want a octal or hexadecimal representation, use the inbuilt function oct() or hex().

17) What is the difference between Xrange and range?

Xrange returns the xrange object while range returns the list, and uses the same memory and no matter what the range size is.

18) What is module and package in Python?

In Python, module is the way to structure program. Each Python program file is a module, which imports other modules like objects and attributes.
The folder of Python program is a package of modules. A package can have modules or subfolders.

19) Mention what are the rules for local and global variables in Python?

Local variables: If a variable is assigned a new value anywhere within the function's body, it's assumed to be local.
Global variables: Those variables that are only referenced inside a function are implicitly global.

20) Explain how to delete a file in Python?

By using a command os.remove (filename) or os.unlink(filename)

21) Explain how can you generate random numbers in Python?

To generate random numbers in Python, you need to import command as
import random
random.random()
This returns a random floating point number in the range [0,1)

22) Mention the use of // operator in Python?

It is a Floor Divisionoperator , which is used for dividing two operands with the result as quotient showing only digits before the decimal point. For instance, 10//5 = 2 and 10.0//5.0 = 2.0.

23) Mention five benefits of using Python?

    • Python comprises of a huge standard library for most Internet platforms like Email, HTML, etc.
    • Python does not require explicit memory  management as the interpreter itself allocates the memory to new variables and free them automatically
    • Provide easy readability due to use of square brackets
    • Easy-to-learn for beginners
    • Having the built-in data types saves programming time and effort from declaring variables

24) Mention the use of the split function in Python?

The use of the split function in Python is that it breaks a string into shorter strings using the defined separator. It gives a list of all words present in the string.

25)Create a simple class with the name  “human”, Which would give out the name and age of the person.

Class human :
	name = None
	age = None

	def get_Name(self) :
		print(“Enter Your Name: ”)
		self.name = input()

	def get_age(self) :
		print(“Enter Your age: ”)
		Self.age = input()

	def put_name(self) :
		print(“Your name is: ”, self.name)

	def put_age(self) :
		print(“Your age is: ”, self.name)
	Person1 = human()
Person1.get_name()
person1.get_age()
