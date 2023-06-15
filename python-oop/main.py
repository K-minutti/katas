class ExampleClass:
    def __init__(self, value):
        self.__value = value

    def __method(self):
        print(self.__value)


ex = ExampleClass("Hello!")
print(vars(ex))

# print(ex.__value) <- throws an error
#           ^^^^^^^^^^
# AttributeError: 'ExampleClass' object has no attribute '__value'

print(ex._ExampleClass__value)
ex._ExampleClass__method()
