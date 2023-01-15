#!/usr/bin/python3
"""A unit test module for the polygon models.
"""
from io import StringIO
import unittest
from unittest.mock import patch
from importlib import import_module


Base = import_module('.base', package='models').Base
Rectangle = import_module('.rectangle', package='models').Rectangle
Square = import_module('.square', package='models').Square


class TestSquare(unittest.TestCase):
    """Tests the Square class and its methods.
    """

    def test_init(self):
        """Tests the initialization of the Square class.
        """
        polygon = Square(5)
        id_init = polygon.id
        self.assertIsInstance(polygon, Base)
        self.assertIsInstance(polygon, Rectangle)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.size, 5)
        self.assertEqual(polygon.size, polygon.width)
        self.assertEqual(polygon.size, polygon.height)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Square('10')
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.size, 5)
        self.assertEqual(polygon.size, polygon.width)
        self.assertEqual(polygon.size, polygon.height)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Square('10', 23)
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.size, 5)
        self.assertEqual(polygon.size, polygon.width)
        self.assertEqual(polygon.size, polygon.height)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Square(10, '20')
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.size, 5)
        self.assertEqual(polygon.size, polygon.width)
        self.assertEqual(polygon.size, polygon.height)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Square(10, 20, '25')
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.size, 5)
        self.assertEqual(polygon.size, polygon.width)
        self.assertEqual(polygon.size, polygon.height)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Square(0)
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.size, 5)
        self.assertEqual(polygon.size, polygon.width)
        self.assertEqual(polygon.size, polygon.height)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Square(-6)
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.size, 5)
        self.assertEqual(polygon.size, polygon.width)
        self.assertEqual(polygon.size, polygon.height)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Square(6, -3)
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.size, 5)
        self.assertEqual(polygon.size, polygon.width)
        self.assertEqual(polygon.size, polygon.height)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'x must be >= 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Square(6, 3, -7)
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.size, 5)
        self.assertEqual(polygon.size, polygon.width)
        self.assertEqual(polygon.size, polygon.height)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'y must be >= 0')
        with self.assertRaises(AttributeError):
            polygon.__nb_objects += 1
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Square(10, 13, 3, 7, 12)

    def test_attribute_validation(self):
        """Tests the validation of attribute and instantiation.
        """
        polygon = Square(12, 3)
        # region the id
        polygon.id = 23
        self.assertEqual(polygon.id, 23)
        polygon.id = 2.3
        self.assertEqual(polygon.id, 2.3)
        polygon.id = None
        self.assertEqual(polygon.id, None)
        polygon.id = False
        self.assertEqual(polygon.id, False)
        polygon.id = True
        self.assertEqual(polygon.id, True)
        polygon.id = 'foo'
        self.assertEqual(polygon.id, 'foo')
        # endregion
        # region the size attribute
        polygon.size = 12
        self.assertEqual(polygon.width, polygon.height)
        self.assertEqual(polygon.width, polygon.size)
        self.assertEqual(polygon.height, polygon.size)
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.size = '12'
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.size = b'12'
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.size = 5.0
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.size = 5.8
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.size = None
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.size = False
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.size = True
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(OverflowError):
            polygon.size = int(float('inf'))
        with self.assertRaises(OverflowError):
            polygon.size = int(float('-inf'))
        with self.assertRaises(ValueError):
            polygon.size = int(float('nan'))
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.size = 0
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.size = -5
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        # endregion
        # region the width attribute
        polygon.width = 17
        self.assertNotEqual(polygon.width, polygon.height)
        self.assertEqual(polygon.width, polygon.size)
        self.assertNotEqual(polygon.size, polygon.height)
        polygon.width = 19
        self.assertNotEqual(polygon.width, polygon.height)
        self.assertEqual(polygon.width, polygon.size)
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.width = '12'
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.width = b'12'
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.width = 5.0
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.width = 5.8
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.width = None
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.width = False
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.width = True
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(OverflowError):
            polygon.width = int(float('inf'))
        with self.assertRaises(OverflowError):
            polygon.width = int(float('-inf'))
        with self.assertRaises(ValueError):
            polygon.width = int(float('nan'))
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.width = 0
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.width = -5
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        # endregion
        # region the height attribute
        polygon.height = 15
        self.assertNotEqual(polygon.height, polygon.width)
        self.assertNotEqual(polygon.height, polygon.size)
        self.assertEqual(polygon.width, polygon.size)
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.height = '12'
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.height = b'12'
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.height = 5.0
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.height = 5.8
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.height = None
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.height = False
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.height = True
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(OverflowError):
            polygon.height = int(float('inf'))
        with self.assertRaises(OverflowError):
            polygon.height = int(float('-inf'))
        with self.assertRaises(ValueError):
            polygon.height = int(float('nan'))
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.height = 0
        self.assertEqual(str(asrt_ctxt.exception), 'height must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.height = -5
        self.assertEqual(str(asrt_ctxt.exception), 'height must be > 0')
        # endregion
        # region the x attribute
        polygon.x = 12
        self.assertEqual(polygon.x, 12)
        polygon.x = 0
        self.assertEqual(polygon.x, 0)
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.x = '12'
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.x = b'12'
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.x = 5.0
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.x = 5.8
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.x = None
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.x = False
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.x = True
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(OverflowError):
            polygon.x = int(float('inf'))
        with self.assertRaises(OverflowError):
            polygon.x = int(float('-inf'))
        with self.assertRaises(ValueError):
            polygon.x = int(float('nan'))
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.x = -5
        self.assertEqual(str(asrt_ctxt.exception), 'x must be >= 0')
        # endregion
        # region the y attribute
        polygon.y = 12
        self.assertEqual(polygon.y, 12)
        polygon.y = 0
        self.assertEqual(polygon.y, 0)
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.y = '12'
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.y = b'12'
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.y = 5.0
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.y = 5.8
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.y = None
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.y = False
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.y = True
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(OverflowError):
            polygon.y = int(float('inf'))
        with self.assertRaises(OverflowError):
            polygon.y = int(float('-inf'))
        with self.assertRaises(ValueError):
            polygon.y = int(float('nan'))
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.y = -5
        self.assertEqual(str(asrt_ctxt.exception), 'y must be >= 0')
        # endregion

    def test_size(self):
        """Tests the size get or set functions.
        """
        polygon = Square(4)
        self.assertEqual(polygon.size, 4)
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.size = 7.4
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.size = None
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.size = True
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.size = False
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.size = '4'
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(OverflowError):
            polygon.size = int(float('inf'))
        with self.assertRaises(OverflowError):
            polygon.size = int(float('-inf'))
        with self.assertRaises(ValueError):
            polygon.size = int(float('nan'))
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.size = 0
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.size = -4
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')

    def test_area(self):
        """Tests the area method of this polygon.
        """
        polygon = Square(12)
        self.assertEqual(polygon.area(), 12 ** 2)
        polygon = Square(10)
        self.assertEqual(polygon.area(), 10 ** 2)
        with self.assertRaises(TypeError):
            polygon.area(None)
        with self.assertRaises(TypeError):
            polygon.area(False)
        with self.assertRaises(TypeError):
            polygon.area(12)
        with self.assertRaises(TypeError):
            polygon.area(12, 12)

    def test_display_0(self):
        """Tests the display method for a polygon with all
        coordinate values being zero.
        """
        polygon = Square(3)
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            polygon.display()
            self.assertEqual(fake_stdout.getvalue(), '###\n###\n###\n')
        polygon = Square(2)
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            polygon.display()
            self.assertEqual(fake_stdout.getvalue(), '##\n##\n')
        polygon = Square(1)
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            polygon.display()
            self.assertEqual(fake_stdout.getvalue(), '#\n')
        with self.assertRaises(TypeError):
            polygon.display(2)

    def test_display_1(self):
        """Tests the display method for a polygon with a
        non-zero coordinate value.
        """
        polygon = Square(3, 0, 1)
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            polygon.display()
            self.assertEqual(fake_stdout.getvalue(), '\n###\n###\n###\n')
        polygon = Square(3, 1, 0)
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            polygon.display()
            self.assertEqual(fake_stdout.getvalue(), ' ###\n ###\n ###\n')
        polygon = Square(2, 2, 2)
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            polygon.display()
            self.assertEqual(fake_stdout.getvalue(), '\n\n  ##\n  ##\n')
        polygon = Square(1, 3, 0)
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            polygon.display()
            self.assertEqual(fake_stdout.getvalue(), '   #\n')
        polygon = Square(1, 0, 3)
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            polygon.display()
            self.assertEqual(fake_stdout.getvalue(), '\n\n\n#\n')
        with self.assertRaises(TypeError):
            polygon.display(2)

    def test_str(self):
        """Tests the __str__ method.
        """
        polygon = Square(4)
        id_init = getattr(polygon, 'id')
        self.assertEqual(
            str(polygon),
            '[Square] ({}) 0/0 - 4'.format(id_init)
        )
        polygon = Square(4, 7, 12)
        id_init += 1
        self.assertEqual(
            str(polygon),
            '[Square] ({}) 7/12 - 4'.format(id_init)
        )
        polygon = Square(4, 7, 12, None)
        id_init += 1
        self.assertEqual(
            str(polygon),
            '[Square] ({}) 7/12 - 4'.format(id_init)
        )
        polygon = Square(4, 7, 12, 5.6)
        self.assertEqual(str(polygon), '[Square] (5.6) 7/12 - 4')
        polygon = Square(4, 7, 12, (7, 6))
        self.assertEqual(str(polygon), '[Square] ((7, 6)) 7/12 - 4')

    def test_update(self):
        """Tests the update function.
        """
        polygon = Square(5)
        # region valid arguments
        polygon.update(1)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 5)
        polygon.update(1, 7)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        polygon.update(1, 7, 5)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        polygon.update(1, 7, 5, 2)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, 9)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, 9, 15)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, None)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        # endregion
        # region *args with **kwargs
        polygon = Square(5)
        polygon.update(1, size=12)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 5)
        polygon.update(1, size=[12, ])
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 5)
        polygon.update(1, 7, size=12)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        polygon.update(1, 7, size={12, })
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        polygon.update(1, 7, 5, size=12, x=17)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        polygon.update(1, 7, 5, size=12, x='17')
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        polygon.update(1, 7, 5, 2, size=12, x=17, y=18)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, size=12, x=17, y=1.8)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, 9, size=12, x=17, y=18)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, 9, size=12, x=17, y='18')
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, 9, 15, size=12, x=17, y=18)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, 9, 15, size=12, x=17, y=(18, 54))
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, None, size=12, x=17, y=18)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, None, size=None, x={'f': 17}, y=None)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, None, size='12', x=1.7, y=18)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(1, 7, 5, 2, None, size='12', x=1.7, y=18, bee=12)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        # endregion
        # region **kwargs and no *args
        polygon = Square(5)
        id_init = polygon.id
        polygon.update(id='35')
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 5)
        # id has no get/set function
        polygon.update(id=None)
        self.assertEqual(polygon.id, None)
        self.assertEqual(polygon.size, 5)
        polygon.update(size=7, id='35')
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        polygon.update(x=5, size=7, id='35')
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        polygon.update(x=5, size=7, id='35', y=2)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        # endregion
        # region update should only update supported attributes
        polygon.update(x=5, size=7, id='35', y=2, foo=63)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        with self.assertRaises(AttributeError):
            print(polygon.foo == 63)
        polygon.update(x=5, width=425, id='35', y=2, foo=63)
        self.assertFalse(polygon.size == 425)
        self.assertFalse(polygon.width == 425)
        self.assertFalse(polygon.height == 425)
        # endregion
        # region update does not recognize width and height
        polygon.update(x=5, size=7, width=35, y=2)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(x=5, size=7, width='35', y=2)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(x=5, size=7, width=None, y=2)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(x=5, size=7, width=True, y=2)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(x=5, size=7, height=35, y=2)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(x=5, size=7, height='35', y=2)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(x=5, size=7, height=None, y=2)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(x=5, size=7, height=True, y=2)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.size, 7)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 7)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        # endregion
        # region update allows validations to be performed
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(size='7', id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(size=b'7', id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(size=True, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(size=False, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(size=None, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(x='7', id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(x=b'7', id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(x=True, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(x=False, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(x=None, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(y='7', id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(y=b'7', id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(y=True, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(y=False, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(y=None, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.update(size=0, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.update(size=-10, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.update(x=-10, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'x must be >= 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.update(y=-10, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'y must be >= 0')
        # endregion

    def test_to_dictionary(self):
        """Tests the to_dictionary method.
        """
        polygon_0 = Square(2)
        id_init = polygon_0.id
        dict_square_0 = polygon_0.to_dictionary()
        self.assertDictEqual(dict_square_0, {
            'id': id_init,
            'size': 2,
            'x': 0,
            'y': 0
        })
        polygon_1 = Square(5, 6, 13)
        dict_square_1 = polygon_1.to_dictionary()
        self.assertDictEqual(dict_square_1, {
            'id': id_init + 1,
            'size': 5,
            'x': 6,
            'y': 13
        })
        polygon_1.update(**dict_square_0)
        dict_square_2 = polygon_1.to_dictionary()
        self.assertDictEqual(dict_square_0, dict_square_2)
        self.assertFalse(dict_square_0 is dict_square_2)

    def test_docs(self):
        """Tests the documentation length of the Square
        and TestSquare classes.
        """
        square_attrs = (
            '__init__',
            'size',
            '__str__',
            'update',
            'to_dictionary',
        )
        test_square_attrs = (
            'test_init',
            'test_size',
            'test_area',
            'test_display_0',
            'test_display_1',
            'test_str',
            'test_update',
            'test_to_dictionary',
            'test_docs',
        )
        min_char_count = 20
        min_word_count = 3
        class_doc = Square.__doc__.strip()
        self.assertGreater(len(class_doc), min_char_count)
        self.assertGreater(len(class_doc.split()), min_word_count)
        for attr_name in square_attrs:
            self.assertIsNotNone(attr_name)
            attr = getattr(Square, attr_name)
            self.assertIsNotNone(attr)
            attr_doc = attr.__doc__
            self.assertIsNotNone(attr_doc)
            attr_doc_trim = attr_doc.strip()
            self.assertGreater(len(attr_doc_trim), min_char_count)
            self.assertGreater(len(attr_doc_trim.split()), min_word_count)
        # the test class
        class_doc = TestSquare.__doc__.strip()
        self.assertGreater(len(class_doc), min_char_count)
        self.assertGreater(len(class_doc.split()), min_word_count)
        for attr_name in test_square_attrs:
            self.assertIsNotNone(attr_name)
            attr = getattr(TestSquare, attr_name)
            self.assertIsNotNone(attr)
            attr_doc = attr.__doc__
            self.assertIsNotNone(attr_doc)
            attr_doc_trim = attr_doc.strip()
            self.assertGreater(len(attr_doc_trim), min_char_count)
            self.assertGreater(len(attr_doc_trim.split()), min_word_count)
