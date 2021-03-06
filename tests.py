import unittest
from main import splitArray

class SplitArrayTests(unittest.TestCase):

    def testNoArray(self):
        self.assertRaises(ValueError, splitArray, None, 10)

    def testEmptyArray(self):
        result = splitArray([], 10)
        self.assertEqual(result, [])

    def testBadSlicesArgument(self):
        self.assertRaises(ValueError, splitArray,[0,1,2,3,4], -1)

    def testNoSlices(self):
        self.assertRaises(ValueError, splitArray,[0,1,2,3,4], 0)

    def testLargeSlice(self):
        self.assertRaises(ValueError, splitArray,[0,1,2,3,4], 8)

    def testMinimalSlices(self):
        result = splitArray([0,1,2,3], 4)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0], [0])
        self.assertEqual(result[1], [1])
        self.assertEqual(result[2], [2])
        self.assertEqual(result[3], [3])

    def testDivisibleSlices(self):
        result = splitArray([0,1,2,3,4,5], 2)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], [0,1,2])
        self.assertEqual(result[1], [3,4,5])

        result = splitArray([0,1,2,3,4,5,6,7,8], 3)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], [0,1,2])
        self.assertEqual(result[1], [3,4,5])
        self.assertEqual(result[2], [6,7,8])

    def testIndivisibleSlices(self):
        result = splitArray([0,1,2,3,4], 2)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], [0,1,2])
        self.assertEqual(result[1], [3, 4])

        result = splitArray([0,1,2,3,4,5,6,7], 3)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], [0,1,2])
        self.assertEqual(result[1], [3,4,5])
        self.assertEqual(result[2], [6,7])

if __name__ == '__main__':
    unittest.main(exit=False)

    