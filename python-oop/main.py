class ExampleClass:
    def __init__(self, value):
        self.__value = value

    def __method(self):
        print(self.__value)


def run_example_class():
    ex = ExampleClass("Hello!")
    print(vars(ex))

    # print(ex.__value) <- throws an error
    #           ^^^^^^^^^^
    # AttributeError: 'ExampleClass' object has no attribute '__value'

    print(ex._ExampleClass__value)
    ex._ExampleClass__method()

class ObjectCounterC:
    num_instances = 0
    def __init__(self):
        # ObjectCounter.num_instances +=1
        type(self).num_instances+=1  # does the same as the line above

class ObjectCounter:
    num_instances = 0
    def __init__(self):
        self.num_instances+=1

def run_object_counter():
    for _ in range(4):
        ObjectCounterC()
    assert ObjectCounterC.num_instances == 4
    print(ObjectCounterC.num_instances)
    
    ex = ObjectCounter()
    assert ex.num_instances == 1
    print(ex.num_instances)

run_object_counter()