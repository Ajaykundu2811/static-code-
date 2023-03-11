'''
Module to classify the triangles
Functions:
classifytriange
    Arguments:
    set_a -- the length of the first side of the triangle
    set_b -- the length of the second side of the triangle
    set_c -- the length of the third side of the triangle

    Returns:
    'Equilateral' if the triangle has three sides of equal length
    'Isosceles' if the triangle has two sides of equal length
    'Scalene' if the triangle has no sides of equal length
    'NotATriangle' if the three side lengths do not form a valid triangle
    'InvalidInput' if any of the side lengths are not positive integers less than or equal to 200
'''

def classifytriangle(set_a, set_b, set_c):
    '''
    Classify a triangle based on the lengths of its sides.

    Arguments:
    set_a -- the length of the first side of the triangle
    set_b -- the length of the second side of the triangle
    set_c -- the length of the third side of the triangle

    Returns:
    'Equilateral' if the triangle has three sides of equal length
    'Isosceles' if the triangle has two sides of equal length
    'Scalene' if the triangle has no sides of equal length
    'NotATriangle' if the three side lengths do not form a valid triangle
    'InvalidInput' if any of the side lengths are not positive integers less than or equal to 200

    '''
    if not(set_a in range(0,200) or set_b in range(0,200) or set_c in range(1, 200)):
        return 'InvalidInput'
    if (set_a > (set_b + set_c)) or (set_b > (set_a + set_c)) or (set_c > (set_a + set_b)):
        return 'NotATriangle'
    if set_a == set_b and set_b == set_c:
        return 'Equilateral'
    if ((set_a ** 2) + (set_b ** 2)) == (set_c ** 2) or ((set_b ** 2) + (set_c ** 2)) == (set_a ** 2) or ((set_a ** 2) + (set_c ** 2)) == (set_a ** 2):
        return 'Right'
    if set_a != set_b and set_b != set_c and set_a != set_c:
        return 'Scalene'
    return 'Isosceles'
