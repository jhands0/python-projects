class SampleClass():
    def __init__(self, a):
        self.__a = a

    def get_a(self):
        return self.__a

    def set_a(self, a):
        self.__a = a


obj = SampleClass(10)
print(obj.get_a())
obj.set_a(45)
print(obj.get_a())