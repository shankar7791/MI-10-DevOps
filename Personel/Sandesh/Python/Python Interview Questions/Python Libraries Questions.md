                           Python Libraries – Python Interview Questions
Q73. Explain what Flask is and its benefits?
Ans: Flask is a web microframework for Python based on “Werkzeug, Jinja2 and good intentions” BSD license. Werkzeug and Jinja2 are two of its dependencies. This means it will have little to no dependencies on external libraries.  It makes the framework light while there is a little dependency to update and fewer security bugs.

A session basically allows you to remember information from one request to another. In a flask, a session uses a signed cookie so the user can look at the session contents and modify. The user can modify the session if only it has the secret key Flask.secret_key.

Q74. Is Django better than Flask?
Ans: Django and Flask map the URL’s or addresses typed in the web browsers to functions in Python. 

Flask is much simpler compared to Django but, Flask does not do a lot for you meaning you will need to specify the details, whereas Django does a lot for you wherein you would not need to do much work. Django consists of prewritten code, which the user will need to analyze whereas Flask gives the users to create their own code, therefore, making it simpler to understand the code. Technically both are equally good and both contain their own pros and cons.

Q75. Mention the differences between Django, Pyramid and Flask.
Ans:  Flask is a “microframework” primarily build for a small application with simpler requirements. In flask, you have to use external libraries. Flask is ready to use.
    Pyramid is built for larger applications. It provides flexibility and lets the developer use the right tools for their project. The developer can choose the database, URL structure, templating style and more. Pyramid is heavy configurable.
    Django can also be used for larger applications just like Pyramid. It includes an ORM.

Q76. Discuss Django architecture.

Ans: Django MVT Pattern:
The developer provides the Model, the view and the template then just maps it to a URL and Django does the magic to serve it to the user.

Q77. Explain how you can set up the Database in Django.
Ans: You can use the command edit mysite/setting.py, it is a normal python module with module level representing Django settings.

Django uses SQLite by default; it is easy for Django users as such it won’t require any other type of installation. In the case your database choice is different that you have to the following keys in the DATABASE ‘default’ item to match your database connection settings.

    Engines: you can change the database by using ‘django.db.backends.sqlite3’ , ‘django.db.backeneds.mysql’, ‘django.db.backends.postgresql_psycopg2’, ‘django.db.backends.oracle’ and so on
    Name: The name of your database. In the case if you are using SQLite as your database, in that case, database will be a file on your computer, Name should be a full absolute path, including the file name of that file.
    If you are not choosing SQLite as your database then settings like Password, Host, User, etc. must be added.

Django uses SQLite as a default database, it stores data as a single file in the filesystem. If you do have a database server—PostgreSQL, MySQL, Oracle, MSSQL—and want to use it rather than SQLite, then use your database’s administration tools to create a new database for your Django project. Either way, with your (empty) database in place, all that remains is to tell Django how to use it. This is where your project’s settings.py file comes in.

We will add the following lines of code to the setting.py file:
	DATABASES = {
     'default': {
          'ENGINE' : 'django.db.backends.sqlite3',
          'NAME' : os.path.join(BASE_DIR, 'db.sqlite3'),
     }
}

Q78. Give an example how you can write a VIEW in Django?
Ans: This is how we can use write a view in Django:	
from django.http import HttpResponse
import datetime
 
def Current_datetime(request):
     now = datetime.datetime.now()
     html = "&amp;amp;lt;html&amp;amp;gt;&amp;amp;lt;body&amp;amp;gt;It is now %s&amp;amp;lt;/body&amp;amp;gt;&amp;amp;lt;/html&amp;amp;gt; % now
     return HttpResponse(html)

Returns the current date and time, as an HTML document

Q79. Mention what the Django templates consist of.
Ans: The template is a simple text file.  It can create any text-based format like XML, CSV, HTML, etc.  A template contains variables that get replaced with values when the template is evaluated and tags (% tag %) that control the logic of the template.

Q80. Explain the use of session in Django framework?
Ans: Django provides a session that lets you store and retrieve data on a per-site-visitor basis. Django abstracts the process of sending and receiving cookies, by placing a session ID cookie on the client side, and storing all the related data on the server side. So the data itself is not stored client side. This is nice from a security perspective.

Q81.  List out the inheritance styles in Django.
Ans: In Django, there are three possible inheritance styles:

    Abstract Base Classes: This style is used when you only want parent’s class to hold information that you don’t want to type out for each child model.
    Multi-table Inheritance: This style is used If you are sub-classing an existing model and need each model to have its own database table.
    Proxy models: You can use this model, If you only want to modify the Python level behavior of the model, without changing the model’s fields.

