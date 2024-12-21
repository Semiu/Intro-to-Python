class Calculator:
    def __init__(self):
        pass
    def add_int(self, x, y):
        """
        add two integers and produce the result
        >>> c = Calculator()
        >>> c.add_int(1,1)
        2
        >>> c.add_int(12, 15)
        27
        """
        return x + y
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()