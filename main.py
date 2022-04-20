#8 task 04

def den():
    try:
        a = int(input("Enter number: "))
        b = int(input("Enter number: "))
        z = a/b
    except ZeroDivisionError:
        print ("The Error!")
        den()
    else:
        print (z)

den()