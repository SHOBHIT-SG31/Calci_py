x = int(input("Enter the first element: "))
y = int(input("Enter the second element: "))
print('''Choose the operation respectively: 
    1. Addition
    2. Sustraction
    3. Multiplication
    4. division''')
a = int(input("Enter the operation: "))
if(a == 1):
    result = x + y
elif(a == 2):
    result = x - y
elif(a == 3):
    result = x * y
elif(a == 4):
    if y != 0:
        result = x / y
    else:
        result = "Cannot divide by zero"
else :
    result = "Invalid operator"

print("Result: ", result)