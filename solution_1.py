class Circle:
    '''
    Class of Circle

    ...

    Сlass instance attribute:
    radius : int
            radius of circle

    Сlass attribute:
    all_circles : list
            list with with all instances of the class (circles)
    pi : float
            the value of pi     

    '''
    pi = 3.1415
    all_circles = []

    def __init__(self, radius=1):
        '''
        Function that initializes attributes of class instances

        ...

        Parameters:
         radius : int
            radius of circle

        '''
        self.radius = radius
        Circle.all_circles.append(self)

    def area(self):
        '''
        Function that decode from english

        ...

        Parameters:
        radius : int
            radius of circle
        pi : float
                the value of pi  

        ...

        return : self.pi * self.radius ** 2

        '''
        return self.pi * self.radius ** 2

    @staticmethod
    def total_area():
        '''
        Function which counts the area of all instances of the class (circles)

        ...

        Parameters:
        total_area : int
                area counter

        ...

        return :  total_area
    
        '''
        total_area = 0
        for circle in Circle.all_circles:
            total_area += circle.area()
        return total_area
    
    def __str__(self):
        '''

        String representation method
    
        '''
        return f'{self.radius}'

    def __repr__(self):
        '''

        String representation method
    
        '''
        return f'{self.radius}'

    
