import numpy as np


class Algorithm:
    """
    An Algorithm which is initialized with parameter_a. Using `calc()` you can add any int to that parameter.

    :parameter_a: Any int which gets added
    :type parameter_a: int

    """
    def __init__(self, parameter_a: int):
        """
        Constructor initializing parameter_a with the given value.

        :param parameter_a:
        :type parameter_a: int
        :returns: Nothing
        :rtype: None

        """
        self.parameter_a = parameter_a
        pass

    def calc(self, parameter_b: int) -> int:
        """
        Add a parameter to the internal one.

        :param parameter_b: parameter to add
        :type parameter_b: int
        :returns: the result
        :rtype: int

        """
        print("calculating something inside the package")
        result = self.parameter_a + parameter_b
        return result
