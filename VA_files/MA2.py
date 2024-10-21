"""
Solutions to module 2 - A calculator
Student: agnes leth
Mail: agnes-leth@live.se
Reviewed by: Andrey
Reviewed date: 24/09-24
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

import math
from tokenize import TokenError  
from MA2tokenizer import TokenizeWrapper

memory = {0:0, 1:1, 2:1} #basecase
def fib(n):
    if n<0 or n != int(n): #tokenizer converts numerical inputs into floats by default
        raise EvaluationError(f'Argument to fib is {n}. Must be integer >= 0')
    
    if n not in memory: #memorazation bc more effecient
            memory[n] = fib(n-1) + fib(n-2)
    return memory[n]
    
    
def std(args):
    n = len(args)
    if n<=1:
        raise EvaluationError(f'Argument to std is {n}. Requires at 2 arguemnts')
    mu = sum(args)/n
    sta_dev = math.sqrt( sum((x-mu)**2 for x in args) / (n-1))
    return sta_dev


def log_function(x):
    if x <= 0:
        raise EvaluationError(f'Argument to log is {x}. Must be > 0')
    return math.log(x)

def fac_function(x):
    if x<0 or x != int(x):
        raise EvaluationError(f'Argument to fac is {x}. Must be integer >= 0')
    return math.factorial(int(x))

def div_function(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        raise EvaluationError(f'Division by zero')


function_1 = {'sin': math.sin, 'cos': math.cos, 'exp': math.exp, 'log': log_function, 'fac': fac_function, 'fib': fib}
function_n = {'sum': sum, 'max': max, 'min': min, 'std': std}


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

def statement(wtok, variables):
    """ See syntax chart for statement"""
    result = assignment(wtok, variables)
    if wtok.is_at_end():
        return result
    else: 
        raise SyntaxError("Expacted end of line")

set_variables = {'PI', 'E', 'ans'}
def assignment(wtok, variables):
    """ See syntax chart for assignment"""
    result = expression(wtok, variables)
    while wtok.get_current() == '=':
        wtok.next()
        if not wtok.is_name():
             raise SyntaxError("Expected name")
        
        if wtok.get_current() in set_variables:
            raise EvaluationError(f'Cannot assign to constant {wtok.get_current()}')
        variables[wtok.get_current()] = result #store result (ex 2=x -> x/2)
        wtok.next()
    return result


def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    while wtok.get_current() in ['+', '-']:
        if wtok.get_current() == '+':
            wtok.next()
            result = result + term(wtok, variables)
        elif wtok.get_current() == '-':
            wtok.next()
            result = result - term(wtok, variables)
    return result


def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while wtok.get_current() in  ['*', '/', '%']: 
        if wtok.get_current() == '*':
            wtok.next()
            result = result * factor(wtok, variables)
        elif wtok.get_current() == '/':
            wtok.next()
            result = div_function(result, factor(wtok, variables))  
        elif wtok.get_current()=='%':
            wtok.next()
            try:
                result=result%factor(wtok, variables)
            except ZeroDivisionError:
                raise EvaluationError(f'Division by zero')
    return result

def arglist(wtok, variables):
    arg_list = []
    if wtok.get_current() == '(':
        wtok.next() 
        arg_list.append(assignment(wtok, variables))
        while wtok.get_current() == ',':
            wtok.next()
            arg_list.append(assignment(wtok, variables))
        if wtok.get_current() not in [')', ',']:
            raise SyntaxError("Expected ')' or ','")
        else:
            wtok.next() 
    elif wtok.get_current() != '(':
        raise SyntaxError("Expected '('")
    return arg_list


def factor(wtok, variables):
    """ See syntax chart for factor"""
    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()

    elif wtok.get_current() in function_1.keys():
        func_name = wtok.get_current() #get key ex 'sin'
        wtok.next()
        if wtok.get_current() != '(':
            raise SyntaxError(f"Expected '(' after function '{func_name}'")
        
        wtok.next()
        arg = assignment(wtok, variables) #get argument ex '3'

        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        
        wtok.next()
        result = function_1[func_name](arg) 

        
    elif wtok.get_current() in function_n.keys():
        func_name = wtok.get_current() 
        wtok.next()
        arg = arglist(wtok, variables)
        result = function_n[func_name](arg)
            
    elif wtok.is_name():
        name = wtok.get_current()
        if name in variables:
            result = variables[name]
            wtok.next()
        else:
            raise EvaluationError(f'Undefined variable: "{wtok.get_current()}"')
            
    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()

    elif wtok.get_current() == '-':
        wtok.next()
        result = -factor(wtok, variables)

    else:
        raise SyntaxError(
            "Expected number, name, function, '-' or '('")  
    return result


         
def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """
    
    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    # Note: The unit test file initiate variables in this way. If your implementation 
    # requires another initiation you have to update the test file accordingly.
    init_file = 'MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()

        elif wtok.get_current() == 'vars':
            print(variables)

        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")
            
            except EvaluationError as ee:
                print("*** Evaluation error: ", ee)

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')
 


if __name__ == "__main__":
    main()
