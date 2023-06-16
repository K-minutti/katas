class ExampleClass:
    def __init__(self, value):
        self.__value = value

    def __method(self):
        print(self.__value)

class SampleClass:
    class_attr = 100

    def __init__(self, instance_attr):
        self.instance_attr = instance_attr

    def method(self):
        print(f"Class attribute: {self.class_attr}")
        print(f"Instance attribute: {self.instance_attr}")

class ObjectCounterC:
    num_instances = 0
    def __init__(self):
        # ObjectCounter.num_instances +=1
        type(self).num_instances+=1  # does the same as the line above

class ObjectCounter:
    num_instances = 0
    def __init__(self):
        self.num_instances+=1

class SampleClass:
    class_attr = 100
    def __init__(self, instance_attr):
        self.instance_attr = instance_attr
    def method(self):
        print(f"Class attr: {self.class_attr}")
        print(f"Instance attr: {self.instance_attr}")

class Record:
    """Class to hold a record of data"""

class User:
    """Used to add dynamic methods"""
    pass

def run_example_class():
    ex = ExampleClass("Hello!")
    print(vars(ex))

    # print(ex.__value) <- throws an error
    #           ^^^^^^^^^^
    # AttributeError: 'ExampleClass' object has no attribute '__value'

    print(ex._ExampleClass__value)
    ex._ExampleClass__method()

def run_object_counter():
    for _ in range(4):
        ObjectCounterC()
    assert ObjectCounterC.num_instances == 4
    print(ObjectCounterC.num_instances)
    
    ex = ObjectCounter()
    assert ex.num_instances == 1
    print(ex.num_instances)

def run_sample_class():
    print(SampleClass.class_attr)
    print(SampleClass(300).instance_attr)
    print(SampleClass.__dict__)
    print(SampleClass.__dict__["class_attr"])
    sample = SampleClass("Hello, sample!")
    print(sample.method())
    sample.__dict__["instance_attr"] = "Hello - there"
    print("Instance attr updated: ", sample.instance_attr)

def run_record_class():
    d = {
        "name": "hi",
        "position": "Developer", 
        "salary": 200000,
        "is_manager": False,
    }
    rec = Record()
    print("Record: ", rec.__dict__)
    for field, val in d.items():
        setattr(rec, field, val)
    print("Record: ", rec.__dict__)

def __init__(self, name:str, color:str):
    self.name = name
    self.color = color

def run_user_class():
    a = User()
    a.name = "val"
    print(a.__dict__)

    User.__init__ = __init__
    print(User.__dict__)
    b = User('san', 'red')
    print(b.__dict__)
    

run_user_class()