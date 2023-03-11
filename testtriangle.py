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

import unittest
from datetime import datetime

def my_brand(assign_name):
    '''
    To display the details of the student
    Arguments:
    assign_name = Name of the assignment
    '''
    my_name = "=*=*=*= Ajay Kundu =*=*=*="
    course = "=*=*=*= Course 2023S-SSW567-WS =*=*=*="
    assign_name = "=*=*=*= "+ assign_name +" =*=*=*="
    date_time = "=*=*=*= "+ str(datetime.now()) +" =*=*=*="
    print(my_name + "\n" + course + "\n" + assign_name + "\n" + date_time)
    print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"+"\n")

ASSIGNMENT_NAME = "HW 02-Testing a legacy program and reporting on testing results"
my_brand(ASSIGNMENT_NAME)

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

    if not(set_a in range(200) or set_b in range(200) or set_c in range(200)):
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

def run_classify_triange(set_a, set_b, set_c):
    '''
    To run and print the result of the classifytriange function.
    Arguments:
    set_a -- the length of the first side of the triangle
    set_b -- the length of the second side of the triangle
    set_c -- the length of the third side of the triangle

    '''
    print(classifytriangle(set_a, set_b, set_c))

class TestTriangle(unittest.TestCase):
    """
    A unit test class for testing the classifytriangle function.
    """

    def test_set1(self):
        """
   Test function to check the classifytriangle function with input parameters (10, 10, 0).
    Input parameters:
    - set_a: integer, represents the length of side a of the triangle
    - set_b: integer, represents the length of side b of the triangle
    - set_c: integer, represents the length of side c of the triangle
    Expected output:
    - 'Equilateral'
    """
        self.assertEqual(classifytriangle(10, 10, 10), 'Equilateral')

    def test_set2(self):
        '''
        Test function to check the classifytriangle function with input parameters (2, 2, 3).
    Input parameters:
    - set_a: integer, represents the length of side a of the triangle
    - set_b: integer, represents the length of side b of the triangle
    - set_c: integer, represents the length of side c of the triangle
    Expected output:
    - 'Isosceles'
    '''
        self.assertEqual(classifytriangle(2, 2, 3), 'Isosceles')

    def test_set3(self):
        '''
        Test function to check the classifytriangle function with input parameters (8, 5, 17).
    Input parameters:
    - set_a: integer, represents the length of side a of the triangle
    - set_b: integer, represents the length of side b of the triangle
    - set_c: integer, represents the length of side c of the triangle
    Expected output:
    - 'Right'
    '''
        self.assertEqual(classifytriangle(8, 15, 17), 'Right')

    def test_set4(self):
        '''
        Test function to check the classifytriangle function with input parameters (7, 8, 9).
    Input parameters:
    - set_a: integer, represents the length of side a of the triangle
    - set_b: integer, represents the length of side b of the triangle
    - set_c: integer, represents the length of side c of the triangle
    Expected output:
    - 'Scalene'
    '''
        self.assertEqual(classifytriangle(7, 8, 9), 'Scalene')

    def test_set5(self):
        '''
        Test function to check the classifytriangle function with input parameters (2, 2, 2).
    Input parameters:
    - set_a: integer, represents the length of side a of the triangle
    - set_b: integer, represents the length of side b of the triangle
    - set_c: integer, represents the length of side c of the triangle
    Expected output:
    - 'Equilateral'
    '''
        self.assertEqual(classifytriangle(2, 2, 2), 'Equilateral')

    def test_set6(self):
        '''
        Test function to check the classifytriangle function with input parameters (20, 20, 20).
    Input parameters:
    - set_a: integer, represents the length of side a of the triangle
    - set_b: integer, represents the length of side b of the triangle
    - set_c: integer, represents the length of side c of the triangle
    Expected output:
    - 'Equilaterl'
    '''
        self.assertEqual(classifytriangle(20, 20, 20), 'Equilateral')

    def test_set7(self):
        '''
        Test function to check the classifytriangle function with input parameters (4, 2, 4).
    Input parameters:
    - set_a: integer, represents the length of side a of the triangle
    - set_b: integer, represents the length of side b of the triangle
    - set_c: integer, represents the length of side c of the triangle
    Expected output:
    - 'Isosceles'
    '''
        self.assertEqual(classifytriangle(4, 2, 4), 'Isosceles')

    def test_set8(self):
        '''
        Test function to check the classifytriangle function with input parameters (11, 15, 18).
    Input parameters:
    - set_a: integer, represents the length of side a of the triangle
    - set_b: integer, represents the length of side b of the triangle
    - set_c: integer, represents the length of side c of the triangle
    Expected output:
    - 'Scalene'
    '''
        self.assertEqual(classifytriangle(11, 15, 18), 'Scalene')

    def test_set9(self):
        '''
        Test function to check the classifytriangle function with input parameters (9, 40, 41).
    Input parameters:
    - set_a: integer, represents the length of side a of the triangle
    - set_b: integer, represents the length of side b of the triangle
    - set_c: integer, represents the length of side c of the triangle
    Expected output:
    - 'Right'
    '''
        self.assertEqual(classifytriangle(9, 40, 41), 'Right')

    def test_set10(self):
        '''
        Test function to check the classifytriangle function with input parameters (9, 10, 12).
    Input parameters:
    - set_a: integer, represents the length of side a of the triangle
    - set_b: integer, represents the length of side b of the triangle
    - set_c: integer, represents the length of side c of the triangle
    Expected output:
    - 'Scalene'
    '''
        self.assertEqual(classifytriangle(9, 10, 12), 'Scalene')

    def test_set11(self):
        '''
        Test function to check the classifytriangle function with input parameters (6, 7, 8).
    Input parameters:
    - set_a: integer, represents the length of side a of the triangle
    - set_b: integer, represents the length of side b of the triangle
    - set_c: integer, represents the length of side c of the triangle
    Expected output:
    - 'Scalene'
    '''
        self.assertEqual(classifytriangle(6, 7, 8), 'Scalene')

    def test_set12(self):
        '''
        Test function to check the classifytriangle function with input parameters (3, 4, 5).
    Input parameters:
    - set_a: integer, represents the length of side a of the triangle
    - set_b: integer, represents the length of side b of the triangle
    - set_c: integer, represents the length of side c of the triangle
    Expected output:
    - 'Right'
    '''
        self.assertEqual(classifytriangle(3, 4, 5), 'Right')

    def test_set13(self):
        '''
        Test function to check the classifytriangle function with input parameters (12, 5, 13).
    Input parameters:
    - set_a: integer, represents the length of side a of the triangle
    - set_b: integer, represents the length of side b of the triangle
    - set_c: integer, represents the length of side c of the triangle
    Expected output:
    - 'Right'
    '''
        self.assertEqual(classifytriangle(12, 5, 13), 'Right')

    def test_set14(self):
        '''
        Test function to check the classifytriangle function with input parameters (1, 3, 3).
    Input parameters:
    - set_a: integer, represents the length of side a of the triangle
    - set_b: integer, represents the length of side b of the triangle
    - set_c: integer, represents the length of side c of the triangle
    Expected output:
    - 'Isosceles'
    '''
        self.assertEqual(classifytriangle(1, 3, 3), 'Isosceles')

    def test_set15(self):
        '''
        Test function to check the classifytriangle function with input parameters (1, 3, 9).
    Input parameters:
    - set_a: integer, represents the length of side a of the triangle
    - set_b: integer, represents the length of side b of the triangle
    - set_c: integer, represents the length of side c of the triangle
    Expected output:
    - 'NotATriangle'
    '''
        self.assertEqual(classifytriangle(1, 3, 9), 'NotATriangle')

    def test_set16(self):
        '''
        Test function to check the classifytriangle function with input parameters (1, 3, a).
    Input parameters:
    - set_a: integer, represents the length of side a of the triangle
    - set_b: integer, represents the length of side b of the triangle
    - set_c: integer, represents the length of side c of the triangle
    Expected output:
    - 'InvalidInput'
    '''
        self.assertEqual(classifytriangle(1, 3, 500), 'NotATriangle')

if __name__ == '__main__':
    unittest.main()
