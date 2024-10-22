num1 = input("Enter num1 : ")
num2 = input("Enter num2 : ")

print("Select Opertion: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

if choice in ['1', '2', '3' ,'4']:

    if choice == '1': print(int(num1) + int(num2))
    if choice == '2': print(int(num1) - int(num2))
    if choice == '3': print(int(num1) * int(num2))
    if choice == '4': print(int(num1) / int(num2))

    if choice not in['1','2','3','4']:
        print("Invalid input")
