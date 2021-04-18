class Person:
    "This is a person class"
    age = 17

    def hello(self):
        print('Hello')


# Output: 10
print(Person.age)

# Output: <function Person.greet>
print(Person.hello)

# Output: "This is a person class"
print(Person.__doc__)