
# import sys
# sys.path.append(r'/home/cisco/PycharmProjects/samp_proj1/day_291018/testing1')
# import unittest
# from testing1 import myadd, mysub
import unittest



def myadd(x, y):
    return x + y


def mysub(x, y):
    return x - y

class MathTest(unittest.TestCase):
    def testadd(self):
        self.assertTrue(myadd(2,3) == 5)


    def testsub(self):
        self.assertTrue(mysub(3,2) == 1)

    def testnotadd(self):
        return self.assertNotEqual(myadd(2,3),6)

    def testobj(self):
        return self.assertIsInstance(math1, MathTest)

math1 = MathTest()


if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(MathTest)
    unittest.TextTestRunner(verbosity=4).run(suite)

#print(dir(unittest.TestCase))