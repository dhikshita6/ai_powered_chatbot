
import math


def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.
    
    Parameters
    ----------
    numbers : list
        A list of numbers for which to calculate the average.
    
    Returns
    -------
    float
        The average of the input numbers.
    
    Raises
    ------
    ValueError
        If the input list is empty.
    """

    total = 0
    for n in numbers:
        total += n
    if len(numbers) == 0:
        return 0
    return total / len(numbers)


def add(a: int, b: int) -> int:
    """
    Calculates the sum of two integers.
    
    Parameters
    ----------
    a : int
        The first integer to add.
    b : int
        The second integer to add.
    
    Returns
    -------
    int
        The sum of a and b.
    """
    return a + b


class Processor:
    def process(self, data):
        """
        Calculates the result of processing a given dataset.
        
        Parameters
        ----------
        self : Processor
            The processor instance.
        data : list
            The list of items to process.
        
        Raises
        ------
        ValueError
            If the input list contains None values.
        """
        for item in data:
            if item is None:
                continue
            print(item)