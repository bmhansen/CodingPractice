#decimal to binary converter

def decimalToBinary(decimal):
    binary = ""
    while (decimal > 0):
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary

number = int(input("Enter a decimal number to be returned in binary \n"))
print(decimalToBinary(number))
