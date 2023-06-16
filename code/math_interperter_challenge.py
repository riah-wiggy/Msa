"""
x= integer
y=+,*,/
z=integer
"""
#prompt the user for the expression
#use .split()to gert the parts of the expression- at the space
#get values from the list
#determine the type of operation to carry out- using if/elif/else statment
#carry out the expression and print the out put formated to one decimal place
expression=input("Enter math expression:")
expression_list = expression.split()
x=float(expression_list[0])
y=expression_list[1]
z=float(expression_list[2])
result=0
if y == "+":
    result = x+z
elif y == "-":
    result = x-z
elif y == "*":
    result = x*z
elif y == "/":
    result = x/z

print(f"(result:.1f)")

