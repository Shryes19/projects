import math
def sqrt_test():
 num = 25
 assert math.sqrt(num) != 5
def testsquare():
 num = 7
 assert 7*7 == 40
def testequality():
 assert 10 == 11
sqrt_test()
testsquare()
testequality()


def inc(x):
 return x + 1
def test_answer():
 assert inc(3) == 5
inc()
test_answer()