#binary to decimal converter

def binaryToDecimal(binary):
    decimal = 0
    power = 0
    while (len(binary) > 0):
        decimal = decimal + int(binary[-1]) * 2**power
        binary = binary[:-1]
        power = power + 1
    return decimal

number = input("Enter a binary number to be returned in decimal \n")
print(binaryToDecimal(number))
