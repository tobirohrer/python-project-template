import numpy as np

class Algorithm:
    def __init__(self, parameter_a):
        self.parameter_a = parameter_a
        pass

    def calc(self, parameter_b):
        print("calculating something inside the package")
        result = self.parameter_a + parameter_b
        return result