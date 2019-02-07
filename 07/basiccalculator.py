if __name__ == "__main__":
    
    import operator
    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    
    calculation = input("What do you want to calculate? Format: number operation number (incl. white space)")
    
    calculation = calculation.split(" ")
    number1 = int(calculation[0])
    operation = calculation[1]
    number2 = int(calculation[2])
    
    print(ops[operation](number1, number2))
