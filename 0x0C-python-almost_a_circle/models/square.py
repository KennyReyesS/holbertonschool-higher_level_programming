#!/usr/bin/python3
"""
square.py module.
"""


from models.rectangle import Rectangle

"""
Class Square inherits from Rectangle.
"""


class Square(Rectangle):
    """Initializes the Square data"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """Returns width"""
        return self.width

    @size.setter
    def size(self, value):
        """assign width and height to size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes"""
        if args is not None and len(args) > 0:
            for num, v in enumerate(args):
                if num == 0:
                    self.id = v
                if num == 1:
                    self.size = v
                if num == 2:
                    self.x = v
                if num == 3:
                    self.y = v
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
