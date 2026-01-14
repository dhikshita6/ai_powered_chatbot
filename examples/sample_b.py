def generator_example(n):
    """
    generator_example function.
    
    :param n: DESCRIPTION
    :type n: TYPE
    """
    """
    generator_example function.
    
    :param n: DESCRIPTION
    :type n: TYPE
    """
    """Example yields numbers.

    Args:
        n (int): Number of values to generate.

    Yields:
        int: Next number in sequence.
    """
    for i in range(n):
        yield i


def raises_example(x):
    """Raises ValueError if x is negative.

    Args:
        x (int): Input value.

    Returns:
        int: Double of x.

    Raises:
        ValueError: If x is negative.
    """
    if x < 0:
        raise ValueError("negative")
    return x * 2