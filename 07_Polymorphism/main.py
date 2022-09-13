import abc

# we first create an Interface using abs library in python
# in which the interface cannot be initialized
# it can only be used to implement detail with inheritance
class ToolInterface(abc.ABC):
    # an abstract method is a method that is not implemented
    @abc.abstractmethod
    def activate(self):
        pass

    @abc.abstractmethod
    def deactivate(self):
        pass

# here we implement the interface by inheretence
class Tool1(ToolInterface):
    def activate(self):
        print("Tool1 is activated")

    def deactivate(self):
        print("Tool1 is deactivated")

class Tool2(ToolInterface):
    def activate(self):
        print("Tool2 is activated")

    def deactivate(self):
        print("Tool2 is deactivated")

# we create a caretaker for tool operation called control
# in which we implement staticmethod, because the class will not be initiated
class Control:
    # we can assert error to prevent caretaker to be initialized
    def __init__(self):
        assert False, "CareTaker cannot be initialized"
    @staticmethod
    def activatetool(tool):
        tool.activate()
    @staticmethod
    def deactivate(tool):
        tool.deactivate()

if __name__ == '__main__':
    # initialize two instance with same interface but different implementation
    tool1 = Tool1()
    tool2 = Tool2()
    # we utilize caretaker refer to an implementation
    Control.activatetool(tool1)
    Control.activatetool(tool2)
    control = Control()


