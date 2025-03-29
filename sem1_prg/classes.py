class A:
    def disp(self):
        print("in disp A")
class B:
    def disp(self):     
        print("in disp B")
class C(A,B): #reverse the order of A and B and observe the output
    def disp(self):
        super().disp()
        print("in disp C")
c1=C()
c1.disp()