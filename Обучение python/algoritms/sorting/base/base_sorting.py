from abc import ABC, abstractmethod


class BaseSorting(ABC):
    def __init__(self, data):
        self.data = data

    def __call__(self):
        return self.result()

    @abstractmethod
    def result(self):
        pass
