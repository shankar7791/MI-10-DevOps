class Hidden:

    # define hidden variable
    __a = 60

    def add(self, num):
        self.__a += num
        print(self.__a)


obj = Hidden()
obj.add(5)
