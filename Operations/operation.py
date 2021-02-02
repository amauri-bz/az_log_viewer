import abc

class Operation(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute(self):
        pass
