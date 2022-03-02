# You're going to write an interactive calculator!
# User input is assumed to be a formula that consists of a number, an operator (at least + and -), and another number, separated by white space
# (e.g. 1 + --> Split user input and check whether the resulting list is valid:
# -> If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
# -> Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError
# -> If the second input is not '+' or '-', again raise a FormulaError
# -> If the input is valid, perform the calculation and print out the result.
# -> The user is then prompted to provide new input, and so on until the user enters quit.
# -> Example image in attached in thread



class FormulaError(Exception):
       pass
    
while True:
    inputs = list(map(str,input().split(" ")))
    try:
        flag = False
        if (len(inputs) == 3) or ('quit' in inputs and len(inputs) == 1):
            if 'quit' in inputs and len(inputs) == 1:
                break
            else:
                try:
                    float(inputs[0])
                    float(inputs[2])
                    if inputs[1] == '+':
                        print(float(inputs[0]) + float(inputs[2]))
                    elif inputs[1] == '-':
                        print(float(inputs[0]) - float(inputs[2]))     
                    else:
                        raise FormulaError           
                except ValueError:
                    flag = True
            if flag:
                raise FormulaError        
        else:
            raise FormulaError
    except FormulaError:
        print('Something went wrong 🙃 !!')
        
        
        
        


# class Error(Exception):
#     pass

# class FormulaError(Error):
#        pass

# while True:
#     try:
#         inputs = list(map(str,input().split(" ")))
#         if (len(inputs) == 3) or ('quit' in inputs and len(inputs) == 1):
#             if 'quit' in inputs and len(inputs) == 1:
#                 break
#             elif inputs[0].isnumeric() and inputs[2].isnumeric():
#                 if inputs[1] == '+':
#                     print(float(inputs[0]) + float(inputs[2]))
#                 elif input[1] == '-':
#                     print(float(inputs[0]) - float(inputs[2]))     
#                 else:
#                     raise FormulaError           
#             else:
#                 raise FormulaError
#         else:
#             raise FormulaError
#     except FormulaError:
#         print('sorry')
        





    