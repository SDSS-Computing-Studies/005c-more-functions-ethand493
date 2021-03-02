#!python3
"""
Create a function that converts from degrees F to degrees C or
vice versa, depending on which initial unit is given
2 input parameters:
float: the number of degrees
string: the unit that you currently have: may be 'C' of 'F'

return: float the number of degrees of the other unit

Sample assertions:
assert convertTemp(10,'C') == 50
assert converTemp(32,'F') == 0
"""
def convertTemp(temp, unit):
    newunit = int(0)
    if unit == 'C':
        newunit = int(temp * (9/5) + 32)
    elif unit == 'F':
        newunit = int((temp - 32) * (5/9))
    return newunit

assert convertTemp(10,'C') == 50
assert convertTemp(32,'F') == 0
