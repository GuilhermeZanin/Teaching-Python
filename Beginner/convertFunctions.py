import math

def degreeToRadian(degree):
    """
    Converts degree to radians.
    Parameters:
    radians: float
     value in degree
    """
    # Formula for radian:
    # PI * radians = 180º
    radians = (math.pi*degree)/180
    return radians

# print(degreeToRadian(180))

def radianToDegree(radians):
    """
    Converts radians to degrees.
    Parameters:
    radians: float
     value in radians
    """
    # Formula for radian:
    # PI * radians = 180º
    degree = radians*180/(math.pi)
    return degree

# print(radianToDegree(1))

