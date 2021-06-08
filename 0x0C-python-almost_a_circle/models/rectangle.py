#!/usr/bin/python3
"""
rectangle.py module
"""


from models.base import Base

"""
Class Rectangle inherits from Base.
"""


class Rectangle(Base):
    """Initializes the Rectangle data"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets conditions for the width of the Rectangle"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("width"))
        elif value <= 0:
            raise ValueError("{} must be > 0".format("width"))
        else:
            self.__width = value

    @property
    def height(self):
        """Returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets conditions for the height of the Rectangle"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("height"))
        elif value <= 0:
            raise ValueError("{} must be > 0".format("height"))
        else:
            self.__height = value

    @property
    def x(self):
        """Returns x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets conditions"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("x"))
        elif value < 0:
            raise ValueError("{} must be >= 0".format("x"))
        else:
            self.__x = value

    @property
    def y(self):
        """Returns y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets conditions"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("y"))
        elif value < 0:
            raise ValueError("{} must be >= 0".format("y"))
        else:
            self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance"""
        return (self.__width * self.__height)

    def display(self):
        """prints the Rectangle instance with the character #"""
        for i in range(self.__y):
            print("")
        for j in range(self.__height):
            print(" " * self.__x, end="")
            for k in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigns arguments to attributes"""
        if args is not None and len(args) > 0:
            for i, v in enumerate(args):
                if i == 0:
                    self.id = v
                if i == 1:
                    self.__width = v
                if i == 2:
                    self.__height = v
                if i == 3:
                    self.__x = v
                if i == 4:
                    self.__y = v

        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "height":
                    self.__height = value
                if key == "width":
                    self.__width = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
