from calc import *
from input import *



def Result1(a,b,c):
    if a.pi>b.pi:
        if a.pi>c.pi:
            print("Самый вогодный проект на основе PI это 1 проект")
            a.output_1()
        else:
            print("Самый вогодный проект на основе PI это 3 проект")
            c.output_1()
    elif b.pi>c.pi:
        print("Самый вогодный проект на основе PI это 2 проект")
        b.output_1()
    else:
        print("Самый вогодный проект на основе PI это 3 проект")
        c.output_1()

def Result2(a,b):
    if a.pi > b.pi:
        print("Самый вогодный проект на основе PI это 1 проект")
        a.output_1()
    else:
        print("Самый вогодный проект на основе PI это 2 проект")
        b.output_1()

