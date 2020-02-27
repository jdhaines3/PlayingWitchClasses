###-----notes-----###
#rectangle class
    #width: get and set
    #height: get and set
    #shouldnt be able to change area: set only
        #def getArea(self): return self.area (calculate and store in variable)
    #self in parenthesis means its a method of class not a function
    #double underscore is private (self.__width)
    #add parameters with default values in case instance has no values when init
###-----end notes-----###


#shape super class with height and width
#all polygons have height and width
class Polygon():
    #initialize with self width and height
    def __init__(self, width, height):
        #get w and h from set methods--both will be hidden/properties
        self.setWidth(width)
        self.setHeight(height)


    #setWidth--w needs to be greater than zero, elso set to a number
    def setWidth(self, width):
        #width must be larger than zero
        if (width <= 0):
            print ("Width needs to be larger than zero, setting to 3.")
            self.__width = 3
        else:
            self.__width = width

    #getWidth, return __width
    def getWidth(self):
        return self.__width

    #make width a property
    #needs to go through getters and setters, but main calls for b.width
    width = property(fget = getWidth, fset = setWidth)

    #setHeight--same if/else as width
    def setHeight(self, height):
        #height must be larger than zero
        if (height <= 0):
            print ("Height needs to be larger than zero, setting to 4.")
            self.__height = 4
        else:
            self.__height = height

    #getHeight return hidden height
    def getHeight(self):
        return self.__height

    #height property like width
    height = property(fget = getHeight, fset = setHeight)


#Rectangle class--inherits from w and h from polygon
#calculates area and perimeter which are diff than other polygon a/p calculations
class Rectangle(Polygon):
    #initalize with width set to 3 and height to 4 for polymorphism
    def __init__(self, width = 3, height = 4):
        #initalize polygon's w and h
        Polygon.__init__(self, width, height)

    #getArea--return getW times getH
    def getArea(self):
        return self.getWidth() * self.getHeight()

    #area property--no setter b/c read only
    area = property(fget = getArea)

    #getPerim--2*getW plus 2*getH
    def getPerimeter(self):
        return (2 * self.getWidth()) + (2 * self.getHeight())

    #perimeter property--only getter (read only)
    perimeter = property(fget = getPerimeter)

    #getStats method
    #must print all properties
    #return multiline string with properties formatted in order
    def getStats(self):
        return str("""width:     {}
height:    {}
area:      {}
perimeter: {}""".format(self.width, self.height, self.area, self.perimeter))


#copied main function
def main():
    print ("Rectangle a:")
    a = Rectangle(5, 7)
    print ("area:      {}".format(a.area))
    print ("perimeter: {}".format(a.perimeter))
    
    print ("")
    print ("Rectangle b:")
    b = Rectangle()
    b.width = 10
    b.height = 20
    print (b.getStats())


#run main
#write if name == main 
if __name__ == "__main__":
    main()
