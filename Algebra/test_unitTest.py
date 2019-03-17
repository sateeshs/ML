##https://pythontesting.net/framework/pytest/pytest-introduction/
#https://exercism.io/my/tracks/r
import unittest
#import VectorOperations
from .vectors import VectorOperations

class VectorOperationsTests(unittest.TestCase):

    def test_addVector(self):
        operations = VectorOperations()
        x=[4,5,6]
        y=[1,2,3]
        value = operations.addition(x,y)
        self.assertEqual(len(value),len(x)
        