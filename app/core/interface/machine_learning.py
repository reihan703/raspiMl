from abc import ABC, abstractmethod

class MachineLearning(ABC):
    @abstractmethod
    def execute(self, file_name):
        pass