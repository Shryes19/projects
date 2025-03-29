
def f1():
 n = 9
 assert n == 9, n
 print("after assert")
import math
def mysqrt():
 assert math.sqrt(26) == 5
 print("done")
f1()
mysqrt()


def test_f1():
 n = 9
 assert n == 9, n
 print("after assert")
import math
def testmysqrt():
 assert math.sqrt(26) == 5
 print("done")
test_f1()
testmysqrt()


def test_f1():
 n = 9
 assert n == 9, n
 print("after assert")
import math
def testmysqrt():
 assert math.sqrt(26) == 5
 print("done")
def decrementtest():
 n = 10
 assert 9 == n-1, "decremented value compared"
 print("after assert in decrementtest")
test_f1()
testmysqrt()
decrementtest()


