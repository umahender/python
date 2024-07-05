class A(object):
    def method(self):
        print("A class Method")
        super().method()
class B(object):
    def method(self):
        print("B class Method")
        super().method()
class C(A,B):
    def method(self):
        print("C class method")
        super().method()

p=C()
p.method()