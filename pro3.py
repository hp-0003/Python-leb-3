class Parent1:
    def __init__(self):
        print("Parent class 1 ")
        
class Parent2:
    def __init__(self):
        print("Parent class 2")

class Child(Parent1, Parent2):
    def __init__(self):
        
        Parent1.__init__(self)
        Parent2.__init__(self)
        print("Child class")
        
ob = Child()


