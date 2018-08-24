from abc import ABC, abstractmethod


class Expr(ABC):
    """ Abstract Base Expression class to inherit from """

    @abstractmethod
    def evaluate(self):
        pass
