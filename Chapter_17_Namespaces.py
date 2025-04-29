"""
def fun():
    # name conflict, local a shadows out global a
    a = 45

    # name conflict, use global b
    global b
    b = 6.28

    # use local a, global b and s
    # print(a, b, s)

    print(locals())
    print(globals())


# global identifiers
a = 20
b = 3.14
s = 'Aabra ka Daabra'

print(locals())
print(globals())


fun()
# print(a, b, s)

"""

"""
Que 1:- Write aa program that nests function fun2() inside function fun1().
        Create two variables by the name a in each function. Prove that they are two different variables.
        
# Answer starts here...

def fun1():
    a = 45
    print(a)
    print(id(a))

    def fun2():
        a = 90
        print(a)
        print(id(a))

    fun2()


fun1()

"""

"""
Que 2:- Write a program that proves that the dictionary returned by globals() can be used to 
        manipulate values of variables in it.
        
# Answer starts here...

a = 10
b = 20
c = 30

print(a, b, c)

# manipulate values using

globals()['a'] = 25
globals()['b'] = 50
globals()['c'] = 75

print(a, b, c)


"""


"""
Que 3:- Write a program that proves that if dictionary returned by locals() is manipulated, 
        the values of original variables don't change. 
"""


def fun():
    a = 10
    b = 20
    c = 30

    locals()['a'] = 25
    locals()['b'] = 50
    locals()['c'] = 75

    print(a, b, c)


fun()


x = 10
y = 20

print(globals())
print(locals())


















