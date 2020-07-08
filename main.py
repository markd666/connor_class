import sys
# 'connor' = filename
# 'Connor' = class name 
from connor import Connor

if __name__ == "__main__":
    # execute only if run as a script
    print("main function")
    #create a object from class 'Connor'
    c = Connor()
    # call 'c' objects member function 'understandClasses
    print(c.understandsClasses())

    d = Connor()
    d.changeUnderstanding(False)
    print(d.understandsClasses())