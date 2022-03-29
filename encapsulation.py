#assigning the class as protected
class Protected:
    #initialize function
    def __init__(self):
        #creating protected variable
        self._protectedVar = 0

#setting object to Protected
obj = Protected()
#defining variable
obj._protectedVar = "This is my protected variable"
#printing the variable
print(obj._protectedVar)

class Protected:
    #initialize function
    def __init__(self):
        #defining the private variable
        self.__privateVar = "My Private Variable"

    def getPrivate(self):
        print(self.__privateVar)

#setting object to Protected
obj = Protected()
#callinf the getPrivate function allowing the variable to be displayed
obj.getPrivate()