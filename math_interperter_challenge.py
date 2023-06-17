"""
x= integer
y=+,*,/
z=integer
"""
#prompt the user for the expression
#use .split()to gert the parts of the expression- at the space
#get values from the list
#determine the type of operation to carry out- using if/elif/else statment
"""
Function to get valid expression inputs from user
Inputs:none
outputs: (int)number1,(int)number2,(string)operator(y)
"""
def get_valid_espression_inputs():
    while True:
        expression=input("Enter math expression:")
        expression_list = expression.split()
        if len(expression_list) !=3:
            print("Error:enter expression in (x,y,z)format\n")
            continue
        try:
            x=float(expression_list[0])
            z=float(expression_list[2])
        except ValueError:
            print("Error:x and z must be numbers. (x y z)\n")
            continue
        y = expression_list[1]
        if y not in ["+","-","*","/"]:
            print("Error: Incorrect y. Only (+,-,*,/)")
            continue
        if z==0:
            print("Error:Divide by zero")
            continue

        break
    return x, z, y
"""
function to evaluate expression
inputs:(uint)x, (int)z, (string)y
output:(int)answer
"""
def evaluate_expression(x, z, y):
    if y == "+":
        result = x+z
    elif y == "-":
        result = x-z
    elif y == "*":
        result = x*z
    elif y == "/":
        result = x/z
    return result
def main():
    while True:
    #call get_valid_expression_inputs function to get the x, x and operator values
        x, z, y = get_valid_espression_inputs()
        result = evaluate_expression(x, z, y)

        print(f"{result:.1f}")
        another_calculation = input("Would you like to evaluate another expression? Press y to continue and any other key to exit")
        if another_calculation != "y":
            break
main()