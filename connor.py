

class Connor:
    def __init__(self):
        # member variable
        self.understands = True

    # member function of class 
    #note the 'self' keyword in the argument list, this allow 
    #you to refer to member variables
    def understandsClasses(self):
        return self.understands

    def changeUnderstanding(self, input):
        self.understands = input