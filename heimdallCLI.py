"""
Authors: Sri Kamal Chillarage, kvc9128@rit.edu
         Chris Cheney, cjc1294@rit.edu
         Sean Bergen, sdb2139@rit.edu
         Copyright 2019
heimdall-cli.py
Text interface to for end user
"""
import inspect
import orbitalCalculations

def runFunction(func):
    """
    Get the values of a function's parameters
    from the user and pass them to the function
    """
    sig = inspect.signature(func)
    values = []
    for parameter in sig.parameters.keys():
        values.append(input(parameter + ": "))

    func(*values)


def main():
    pass


if __name__ == "__main__":
    main()
