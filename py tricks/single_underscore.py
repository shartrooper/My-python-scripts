'''
In the following code example I’m unpacking a car tuple into separate variables but I’m only interested in the values for color and mileage.
However, in order for the unpacking expression to succeed I need to assign all values contained in the tuple to variables. That’s where “_” is useful as a placeholder variable:
'''

car = ('red', 'auto', 12, 3812.4)
color, _, _, mileage = car

color
'red'
mileage
3812.4
_
12
