class HelloMeta(type):
    # A hello method
    def hello(cls):
        print("greetings from %s, a HelloMeta type class" % (type(cls())))

    # Call the metaclass
    def __call__(self, *args, **kwargs):
        # create the new class as normal
        cls = type.__call__(self, *args)

        # define a new hello method for each of these classes
        setattr(cls, "hello", self.hello)

        # return the class
        return cls

# Try out the metaclass
class TryHello(object, metaclass=HelloMeta):
    def greet(self):
        self.hello()

greeter = TryHello()
greeter.greet()