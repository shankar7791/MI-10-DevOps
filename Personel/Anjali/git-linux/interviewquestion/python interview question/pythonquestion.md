							Python Interview Questions :

Q1. What is the difference between list and tuples in Python?
ANS:	 List are commonly enclosed with the square bracket [], and elements are comma-separated element.
	 Tuples are enclosed with parenthesis (), and elements are separated by the comma. The parenthesis is optional to use, and these types of tuples are 		 called tuple packing.

Q2. What are the key features of Python?
ANS:	Easy to Learn and Use
	Expressive Language
	Interpreted Language
	Cross-platform Language
	Free and Open Source
	Object-Oriented Language
	Extensible
	Large Standard Library
	GUI Programming Support

Q3. What type of language is python? Programming or scripting?
ANS:Python is scripting, general-purpose, high-level, and interpreted programming language. It also provides the object-oriented programming approach.

Q4.Python an interpreted language. Expla0in.
ANS:Yes python is interpreted language.it means the Python program is executed one line at a time. 

Q5.What is pep 8?
ANS:PEP 8 is a document that provides guidelines and best practices on how to write Python code.

Q6. How is memory managed in Python?
ANS:Heap 

Q7. What is namespace in Python?
ANS:	A namespace is a collection of currently defined symbolic names along with information about the object that each name references. You can think   		of a namespace as a dictionary in which the keys are the object names and the values are the objects themselves.

Q8. What is PYTHONPATH?
ANS:PYTHONPATH is an environment variable which you can set to add additional directories where python will look for modules and packages.

Q9. What are python modules? Name some commonly used built-in modules in Python?
ANS: Consider a module to be the same as a code library.A file containing a set of functions you want to include in your application.
	1)OS Module
	2)Sys Module
	3)Statistics Module
	4)Collections Module
	5)Random Module

Q10.What are local variables and global variables in Python?
ANS:A global variable can be reached anywhere in the code, a local only in the scope.

Q11. Is python case sensitive?
ANS: Yes, python is case sensitive.

Q12.What is type conversion in Python?
ANS:Type Conversion is the conversion of object from one data type to another data type.

Q13. How to install Python on Windows and set path variable?

Q14. Is indentation required in python?
ANS: Yes, Indentation required in python.
 
Q15. What is the difference between Python Arrays and lists?
ANS:List:A list in Python is a collection of items which can contain elements of multiple data types, which may be either numeric, character logical values,  	  etc.
    Arrays: An array is a vector containing homogeneous elements i.e. belonging to the same data type. 

Q16. What are functions in Python?
ANS:A function is a block of organized, reusable code that is used to perform a single, related action.

Q17.What is __init__?
ANS:is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created  	from  a class and it allows the class to initialize the attributes of the class.

Q18.What is a lambda function?
ANS:a lambda function is a single-line function declared with no name, which can have any number of arguments, but it can only have one expression. 

Q19. What is self in Python?
ANS:self represents the instance of the class. By using the “self” keyword we can access the attributes and methods of the class in python.

Q20. How does break, continue and pass work?
ANS:	break:terminates the current loop and resumes execution at the next statement
	continue:returns the control to the beginning of the while loop.
	Pass:when a statement is required syntactically but you do not want any command or code to execute.

Q21. What does [::-1} do?
ANS:It iterate over a list in reverse order.

Q22. How can you randomize the items of a list in place in Python?
ANS:

Q23. What are python iterators?
ANS:Iterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets. The iterator object is initialized using the iter() method.

Q24. How can you generate random numbers in Python?
ANS:Random integer values can be generated with the randint() function.

Q25. What is the difference between range & xrange?
ANS:	Range:This returns a range object
	xrange:This function returns the generator object that can be used to display numbers only by looping.

Q26. How do you write comments in python?
ANS: for singal line use #, And for multiline use '''  '''.

Q27. What is pickling and unpickling?
ANS:    Pickling: It is a process where a Python object hierarchy is converted into a byte stream.
    	Unpickling: It is the inverse of Pickling process where a byte stream is converted into an object hierarchy.

Q28. What are the generators in python?
ANS:Generators are very easy to implement, but a bit difficult to understand.Generators are used to create iterators, but with a different approach. 		Generators are simple functions which return an iterable set of items, one at a time, in a special way.

Q29. How will you capitalize the first letter of string?
ANS: Using capitalize() method

Q30. How will you convert a string to all lowercase?
ANS:using lower() method

Q31. How to comment multiple lines in python?
ANS:"""..."""

Q32. What are docstrings in Python?
ANS:Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.

Q33. What is the purpose of is, not and in operators?
ANS:	is:True if the operands are identical. 
	not:True if operand is false.
	in:is used to check if a value exists in a sequence or not.

Q34. What is the usage of help() and dir() function in Python?
ANS:	help():used to see the documentation or docstrings of the module passed as argument.
	Dir():function returns all properties and methods of the specified object, without the values. This function will return all the properties and 		methods, even built-in properties which are default for all object.

Q35. Whenever Python exits, why isn’t all the memory de-allocated?
ANS: the object referenced from global namespaces of Python modules are not always deallocated.

Q36. What is a dictionary in Python?
ANS:A dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value.

Q37. How can the ternary operators be used in python?
ANS:Ternary operators also known as conditional expressions are operators that evaluate something based on a condition being true or false.

Q38. What does this mean: *args, **kwargs? And why would we use it?
ANS:	*args:used to pass a variable number of arguments to a function. It is used to pass a non-key worded, variable-length argument list. 
	**kwargs: is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star. The reason is because the double 				star allows us to pass through keyword arguments.

Q39. What does len() do?
ANS:	It return a length of given string.

Q40. Explain split(), sub(), subn() methods of “re” module in Python.
ANS:split():
	This function splits the string according to the occurrences of a character or a pattern. When it finds that pattern, it returns the 		   		remaining characters from the string as part of the resulting list.  The split method should be imported before using it in the program.

	Syntax:  re.split (pattern, string, maxsplit=0, flags=0)
    
    sub():
	This function stands for the substring in which a certain regular expression pattern is searched in the given string (3rd parameter). When it finds  		the substring, the pattern is replaced by repl (2nd parameter). The count checks and maintains the number of times this has occurred.

	Syntax:re.sub (pattern, repl, string, count=0, flags=0)

     subn():
	This function is similar to sub() in all ways except the way in which it provides the output. It returns a tuple with count of total of all the  		replacements as well as the new string.

	Syntax:re.subn (pattern, repl, string, count=0, flags=0)


Q41. What are negative indexes and why are they used?
ANS: The negative index is used to remove any new-line spaces from the string and allow the string to except the last character that is given.The negative 	index is also used to show the index to represent the string in correct order.
 
Q42. What are Python packages?
ANS:A python package is a collection of modules. Modules that are related to each other are mainly put in the same package. When a module from an external  	package is required in a program, that package can be imported and its modules can be put to use.

Q43.How can files be deleted in Python?
ANS:	os.remove() = deletes single Python files. 
 	os.rmdir() = removes a file or a directory. 
	shutil.rmtree() = delete a directory and the files contained in it.

Q44. What are the built-in types of python?
ANS: Variables can store data of different types, and different types can do different things.

Q45. What advantages do NumPy arrays offer over (nested) Python lists?
ANS:    consumes less memory.
    	fast as compared to the python List.
    	convenient to use.

Q46. How to add values to a python array?
ANS: append() method to add an element to an array.

Q47. How to remove values to a python array?
ANS: pop() method

Q48. Does Python have OOps concepts?
ANS: yes

Q49. What is the difference between deep and shallow copy?
ANS:	A shallow copy constructs a new compound object and then inserts references into it to the objects found in the original. 
	A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.

Q50. How is Multithreading achieved in Python?
ANS: importing the threading module.

Q51. What is the process of compilation and linking in python?
ANS:	Compilation: The source code in python is saved as a .py file which is then compiled into a format known as byte code, byte code is then converted to 			machine code. After the compilation, the code is stored in .pyc files and is regenerated when the source is updated. This process is known as 			compilation.

	Linking: Linking is the final phase where all the functions are linked with their definitions as the linker knows where all these functions are 		implemented. This process is known as linking.

Q52. What are Python libraries? Name a few of them.
ANS:Python Libraries are a set of useful functions that eliminate the need for writing codes from scratch. 

	Name of libraries:
	1)Numpy
	2)Pandas
	3)Keras
	4)SciPy

Q53. What is split used for?
ANS:splits a string into a list. 

Q54. How to import modules in python?
ANS: using import Module_name

OOPS Python Interview Questions

Q55. Explain Inheritance in Python with an example.
ANS: Inheritance:
	Inheritance provides code reusability to the program because we can use an existing class to create a new class instead of creating it from scratch.
	In inheritance, the child class acquires the properties and can access all the data members and functions defined in the parent class.
	A child class can also provide its specific implementation to the functions of the parent class. 
	In this section of the tutorial, we will discuss inheritance in detail.

1) Single inheritance: When a child class inherits from only one parent class, it is called single inheritance.
	Example:
		    class Animal: 
        		def speak(self): 
            			print("Animal Speaking") 

    		    class Dog(Animal): 
        		def bark(self): 
            			print("dog barking") 
    		    d = Dog() 
    		    d.bark() 
    		    d.speak() 

2) Multiple inheritance: When a child class inherits from multiple parent classes, it is called multiple inheritance. Python supports multiple inheritance.  				 We specify all parent classes as a comma-separated list in the bracket. 
	Example:
			class Animal:
				def speak(self):
					print("Animal speaking")
			class wild:
				def fun(self):
					print("Wild Animal")
			class pet:
				def fun2(self):
					print("pet animal")
			class dog(Animal,wild,pet):
				def fun3(self):
					print("dog is pet animal")
			c=dog()
			c.speak()
			c.fun()
			c.fun2()
			c.fun3()

3) Multilevel inheritance: When we have a child and grandchild relationship.
	Example:
		class Animal:  
    			def speak(self): 
        		print("Animal Speaking") 

		class Dog(Animal): 
    			def bark(self): 
        		print("dog barking") 

		class DogChild(Dog):  
    			def eat(self): 
        		print("Eating bread...") 
		d = DogChild()  
		d.bark()  
		d.speak()  
		d.eat() 

4) Hierarchical inheritance More than one derived classes are created from a single base.
	Example:
		 class Parent: 
   			def functionl(self): 
      				print("this is first function 1")
 
 		class Childl(Parent): 
   			def function2(self): 
      				print("this is second function 2") 

 		class Child2(Parent): 
   			def function3(self):
      				print("this is third function 3")
 
 		x = Childl()
 		xl = Child2() 
 		x.functionl() 
 		x.function2()

5) Hybrid inheritance: Hybrid inheritance is a combination of multiple inheritance and multilevel inheritance. 

Q56. How are classes created in Python?
ANS: Using def keyword we creat a class in python.

Q57. What is monkey patching in Python?
ANS: the term monkey patch only refers to dynamic modifications of a class or module at runtime, which means monkey patch is a piece of Python code that 	extends or modifies other code at runtime

Q58. Does python support multiple inheritance?
ANS: Yes,Python support multiple inheritance.

Q59. What is Polymorphism in Python?
ANS: A child class inherits all the methods from the parent class. However, in some situations, the method inherited from the parent class doesn’t quite fit 	  into the child class. In such cases, you will have to re-implement method in the child class.

Q60. Define encapsulation in Python?
ANS: It is used to restrict access to methods and variables. In encapsulation, code and data are wrapped together within a single unit from being modified 	by accident.

Q61. How do you do data abstraction in Python?
ANS: Abstraction is used to hide the internal functionality of the function from the users. The users only interact with the basic implementation of the     	  function, but inner working is hidden. 

Q62.Does python make use of access specifiers?
ANS: The access modifiers in Python are used to modify the default scope of variables. There are three types of access modifiers in Python: public, private, 	  and protected.

Q64. What does an object() do?
ANS:  The object() function returns an empty object. You cannot add new properties or methods to this object. This object is the base for all classes, it  	 holds the built-in properties and methods which are default for all classes.

Programming Questions :

Q65. Write a program in Python to execute the Bubble sort algorithm.
ANS: 
    def bubble_sort(list1): 
        # Outer loop for traverse the entire list  
        for i in range(0,len(list1)-1):  
            for j in range(len(list1)-1):  
                if(list1[j]>list1[j+1]):  
                    temp = list1[j]  
                    list1[j] = list1[j+1]  
                    list1[j+1] = temp  
        return list1  
      list1 = [5, 3, 8, 6, 7, 2] 
      print("The unsorted list is: ", list1) 
      print("The sorted list is: ", bubble_sort(list1)) 

Q66. Write a program in Python to produce Star triangle.
ANS:
    n = int(input("Enter the number of rows")) 
     
    for i in range(0, n): 
        
            for j in range(0, i + 1):  

                print("* ", end="")       
      
            print()  
	 	
Q67. Write a program to produce Fibonacci series in Python.
ANS:

	val=int(input("Enter the number"))
	first=0
	second=1
	i=0

	while i<val:
    		if i<=1 :
        		j=i
    		else :
        		j=first+second
        		first=second
        		second=j
    		print(j)
    		i=i+1

Q68. Write a program in Python to check if a number is prime.
ANS:
	def prime(num):
	    if num>1:
        	for i in range(2,num):
            		if num%i==0:
                		print("no is not prime")
        		print("no is prime")
	prime(3)

Q69. Write a program in Python to check if a sequence is a Palindrome.
ANS:

	def pali(str):
	    str1=""
    	    for i in str:
        	str1=i+str1
        	print(f"string is in reverse {str1}")
    	    if str==str1:
        		print("String is palindrome")
    	    else:
        		print("String is not palindrome")
	str=input("Enter the string  ")
	pali(str)
	
Q70. Write a one-liner that will count the number of capital letters in a file. Your code should work even if the file is too big to fit in memory.
ANS:

Q71. Write a sorting algorithm for a numerical dataset in Python.
ANS:

Q72. Looking at the below code, write down the final values of A0, A1, …An.
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
print(A0,A1,A2,A3,A4,A5,A6)

ANS:	{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5} range(0, 10) [] [1, 2, 3, 4, 5] [1, 2, 3, 4, 5] {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 		9: 81} [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]


Python Libraries – Python Interview Questions

Q73. Explain what Flask is and its benefits?
ANS:	Flask is a web framework. Flask allows you to build a web application by providing tools, libraries, and technologies.
	
	Benefits=	
		1)Integrated support for unit testing
		2)Built-in development server and fast debugger
		3)Restful request dispatching
		4)Unicode base
		5)Support for cookies

Q74. Is Django better than Flask?
ANS:It is depends on you django is a full feature web freamwork and hance it required decison made by you or your team you can move probably faster that  	way.However if your not satisfied with the one of the choices thats django mades for you or you have the unique application requirmentes then an this 		case you may have look at the flask as well.both the freamwork have lower the bariyar.

Q75. Mention the differences between Django, Pyramid and Flask.
ANS:	Django:
	Flask:Flask is a "microframework" primarily aimed at small applications with simpler requirements.
	
Q76. Discuss Django architecture.
ANS:	mvc is  django architecture model,view,control

Q77. Explain how you can set up the Database in Django.
ANS: Django uses SQLite by default; it is easy for Django users as such it won’t require any other type of installation. In the case your database choice is  	   different that you have to the following keys in the DATABASE ‘default’ item to match your database connection settings

     Engines: you can change database by using ‘django.db.backends.sqlite3’ , ‘django.db.backeneds.mysql’, ‘django.db.backends.postgresql_psycopg2’, 		     ‘django.db.backends.oracle’ and so on
     Name: The name of your database. In the case if you are using SQLite as your database, in that case database will be a file on your computer, Name 	   should be a full absolute path, including file name of that file.


Q78. Give an example how you can write a VIEW in Django?
ANS: 	import datetime 
	# Create your views here. 
	from django.http import HttpResponse 
	def index(request): 
    		now = datetime.datetime.now() 
    		html = "<html><body><h3>Now time is %s.</h3></body></html>" % now 
    		return HttpResponse(html)    # rendering the template in HttpResponse 

Q79. Mention what the Django templates consist of.
ANS: A template consists of static parts of the desired HTML output as well as some special syntax describing how dynamic content will be inserted.

Q80. Explain the use of session in Django framework?
ANS:	A session is a mechanism to store information on the server side during the interaction with the web application.

Q81.  List out the inheritance styles in Django.
ANS:	Abstract Base Class Inheritance
	Multi Table Model Inheritance
	Proxy Model Inheritance

