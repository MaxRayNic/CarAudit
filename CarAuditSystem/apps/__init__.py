from abc import ABC, abstractmethod


class BaseService(ABC):
    def __init__(self, payload=None, arguments=None):
        self.data = payload
        self.parameters = arguments

    @abstractmethod
    def execute(self):
        pass
