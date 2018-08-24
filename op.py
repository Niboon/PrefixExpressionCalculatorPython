from abc import ABC, abstractmethod


class Op(ABC):
    """ Abstract Base Operator class to inherit from """

    @abstractmethod
    def execute(self, left_expr, right_expr):
        pass
