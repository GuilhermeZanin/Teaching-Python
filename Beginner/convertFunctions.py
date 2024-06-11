import math

# Converts degree to radians
def degreeToRadian(degree):
    """
    Parameters:
    radians: float
     value in degree
    """
    # Formula for radian:
    # PI * radians = 180º
    radians = (math.pi*degree)/180
    return radians

# print(degreeToRadian(180))


# Converts radians to degrees
def radianToDegree(radians):
    """
    Parameters:
    radians: float
     value in radians
    """
    # Formula for radian:
    # PI * radians = 180º
    degree = radians*180/(math.pi)
    return degree

# print(radianToDegree(1))


# Converts decimal to binary (or could use bin() in built function)
def decimalToBinary(decimal):
    """
    Parameters:
    decimal: int
     value in int
    """
    binary = ""

    while decimal > 0:
        # compute the remainder when the decimal number is divided by 2 using the modulus operator %
        # convert the remainder to a string and concatenate it with the left side of the binary string
        binary = str(decimal % 2) + binary

        # update the decimal number by performing integer division by 2 
        decimal = decimal // 2
    return binary

decimal = 10
print("Decimal: "+ str(decimal)+"\n\nInto Binary: "+decimalToBinary(decimal))
