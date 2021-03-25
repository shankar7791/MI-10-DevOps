class GrandPa:
    def __init__(self):
        print("Grand Paa")

class Father(GrandPa):
    def __init__(self):
        super().__init__()
        print("Father")

class Mother(GrandPa):
    def __init__(self):
        super().__init__()
        print("Mother")


class child(Father, Mother):
    def __init__(self):
        super().__init__()
        print("Child")

c = child()