##########################################################################
'''magic methods'''

#__call__ -> executed when you try to call an object
#__repr__ or __str__ -> executed when you try to print an object
#__contains__ -> executed when you try to use membership operator on an object
#__getitem__ -> executed when you try to index an object
#__setitem__ -> executed when you try to assign a value to an indexed object
#__gt__ -> executed when '>' is used between two objects
#__ge__ -> executed when '>=' is used between two objects
#__lt__ -> executed when '<' is used between two objects
#__le__ -> executed when '<=' is used between two objects
#__eq__ -> executed when '==' is used between two objects
#__ne__ -> executed when '!=' is used between two objects

#------------------------------------------------------------------------
class Sample:
    var1 = 10
    var2 = 20
    var3 = 30
    
    def __init__(self, a):
        self.a = a

    @staticmethod
    def method1():
        print("in method1")

    def __call__(self):
        print("i made the object a callable")

    def __str__(self):
        return "hello"

    def __repr__(self):
        return '10'

    def __contains__(self, value):
        return value in Sample.__dict__.values()
    
    def __getitem__(self, index):
        if index == 1:
            return self.var1
        elif index == 2:
            return self.var2
        elif index == 3:
            return self.var3
        else:
            return "index out of range"
    
    def __setitem__(self, index, value):
        if index == 1:
            Sample.var1 = value
        elif index == 2:
            Sample.var2 = value
        elif index == 3:
            Sample.var3 = value
        else:
           print("index not present")


    def __gt__(self, address):
        return self.a > address.a
    
    def __ge__(self, address):
        return self.a >= address.a

    def __lt__(self, address):
        return self.a < address.a

    def __le__(self, address):
        return self.a <= address.a

    def __eq__(self, address):
        return self.a == address.a

    def __ne__(self, address):
        return self.a != address.a


s1 = Sample(10)
print(callable(s1))
s1()            #s1.__call__()          #Sample.__call__(s1)
print(s1)       #s1.__str__()           #Sample.__str__(s1)
print(40 in s1) #s1.__contains__(40)    #Sample.__contains__(40)
print(s1[5])    #s1.__getitem__(5)      #Sample.__getitem__(5)

s2 = Sample(20)
print(s1 > s2)     #s1.__gt__(s2)      #Sample.__gt__(s1, s2)

s1[5] = 15         #s1.__setitem__(5, 15)       #Sample.__setitem__(s1, 5, 15)

###################################################################
'''----if __name__ == '__main__'----'''
#to check if the given function or class is called in the same module in which it is defined
#this random function will be executed in this module
#if it is used in other module, 'if' block will not be executed
def random():
    if __name__ == '__main__':
        print(__name__)
        print("nonsense")

random()

#--------------------------------------------------------------------
class Simple:
    def __init__(self):
        if __name__ == '__main__':
            print("object created")
        else:
            raise NameError


s1 = Simple()


##########################################################################