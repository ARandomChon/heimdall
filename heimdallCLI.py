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


def getFunctions(module):
    """
    Returns a list of the functions of a module
    Format: (function name, reference to function)
    """
    allFuncs = inspect.getmembers(module)
    funcs = {}
    for func in allFuncs:
        if not func[0].startswith("__") and type(func[1]) == type(main):
            funcs[func[0]] = func[1]

    return funcs


def main():
    funcs = getFunctions(orbitalCalculations)
    print("Available Functions:")
    for func in funcs:
        print(func)

    choice = input("Choose a function to run: ")
    if not choice in funcs:
        print("Invalid function")
        return

    runFunction(funcs[choice])


if __name__ == "__main__":
    main()
