#!/usr/bin/python3
"""A unit test module for the polygon models.
"""
from io import StringIO
import unittest
from unittest.mock import patch
from importlib import import_module


Base = import_module('.base', package='models').Base
Rectangle = import_module('.rectangle', package='models').Rectangle


class TestRectangle(unittest.TestCase):
    """Tests the Rectangle class and its methods.
    """

    def test_init(self):
        """Tests the initialization of the Square class.
        """
        polygon = Rectangle(5, 8, 0, 0)
        id_init = polygon.id
        self.assertIsInstance(polygon, Base)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 8)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Rectangle('10', 13)
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 8)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Rectangle(10, '13')
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 8)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Rectangle(10, 13, '20')
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 8)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'x must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Rectangle(10, 13, 20, '25')
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 8)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'y must be an integer')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Rectangle(0, 13)
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 8)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Rectangle(-10, 13)
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 8)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Rectangle(10, 0)
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 8)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'height must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Rectangle(10, -13)
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 8)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'height must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Rectangle(6, 9, -3)
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 8)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'x must be >= 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon = Rectangle(6, 9, 3, -7)
        self.assertEqual(polygon.id, id_init)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 8)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        self.assertEqual(str(asrt_ctxt.exception), 'y must be >= 0')
        with self.assertRaises(AttributeError):
            polygon.__nb_objects += 1
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon = Rectangle(10, 13, 3, 7, 1, 12)

    def test_attribute_validation(self):
        """Tests the validation of attribute and instantiation.
        """
        polygon = Rectangle(12, 3)
        # region the id
        polygon.id = 23
        self.assertEqual(polygon.id, 23)
        polygon.id = None
        self.assertEqual(polygon.id, None)
        polygon.id = False
        self.assertEqual(polygon.id, False)
        polygon.id = True
        self.assertEqual(polygon.id, True)
        polygon.id = 'foo'
        self.assertEqual(polygon.id, 'foo')
        # endregion
        # region the width attribute
        polygon.width = 12
        self.assertEqual(polygon.width, 12)
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
        polygon.height = 12
        self.assertEqual(polygon.height, 12)
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

    def test_area(self):
        """Tests the area method of this polygon.
        """
        polygon = Rectangle(12, 3)
        self.assertEqual(polygon.area(), 12 * 3)
        polygon = Rectangle(10, 10)
        self.assertEqual(polygon.area(), 10 * 10)
        polygon = Rectangle(10, 10, 60, 45, 3)
        self.assertEqual(polygon.area(), 10 * 10)
        polygon = Rectangle(10, 10, 60, 45)
        self.assertEqual(polygon.area(), 10 * 10)
        polygon = Rectangle(10, 10, 60)
        self.assertEqual(polygon.area(), 10 * 10)
        with self.assertRaises(TypeError):
            polygon.area(None)
        with self.assertRaises(TypeError):
            polygon.area(12)
        with self.assertRaises(TypeError):
            polygon.area(10, 10)

    def test_display_0(self):
        """Tests the display method for a polygon with all
        coordinate values being zero.
        """
        polygon = Rectangle(4, 3)
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            polygon.display()
            self.assertEqual(fake_stdout.getvalue(), '####\n####\n####\n')
        polygon = Rectangle(2, 2)
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            polygon.display()
            self.assertEqual(fake_stdout.getvalue(), '##\n##\n')
        polygon = Rectangle(1, 3)
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            polygon.display()
            self.assertEqual(fake_stdout.getvalue(), '#\n#\n#\n')
        polygon = Rectangle(3, 1)
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            polygon.display()
            self.assertEqual(fake_stdout.getvalue(), '###\n')
        with self.assertRaises(TypeError):
            polygon.display(2)

    def test_display_1(self):
        """Tests the display method for a polygon with a
        non-zero coordinate value.
        """
        polygon = Rectangle(4, 3, 0, 1)
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            polygon.display()
            self.assertEqual(fake_stdout.getvalue(), '\n####\n####\n####\n')
        polygon = Rectangle(4, 3, 1, 0)
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            polygon.display()
            self.assertEqual(fake_stdout.getvalue(), ' ####\n ####\n ####\n')
        polygon = Rectangle(2, 2, 2, 2)
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            polygon.display()
            self.assertEqual(fake_stdout.getvalue(), '\n\n  ##\n  ##\n')
        polygon = Rectangle(1, 3, 3, 0)
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            polygon.display()
            self.assertEqual(fake_stdout.getvalue(), '   #\n   #\n   #\n')
        polygon = Rectangle(3, 1, 0, 3)
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            polygon.display()
            self.assertEqual(fake_stdout.getvalue(), '\n\n\n###\n')
        with self.assertRaises(TypeError):
            polygon.display(2)

    def test_str(self):
        """Tests the __str__ method.
        """
        polygon = Rectangle(4, 3)
        id_init = getattr(polygon, 'id')
        self.assertEqual(
            str(polygon),
            '[Rectangle] ({}) 0/0 - 4/3'.format(id_init)
        )
        polygon = Rectangle(4, 3, 7, 12)
        id_init += 1
        self.assertEqual(
            str(polygon),
            '[Rectangle] ({}) 7/12 - 4/3'.format(id_init)
        )
        polygon = Rectangle(4, 3, 7, 12, None)
        id_init += 1
        self.assertEqual(
            str(polygon),
            '[Rectangle] ({}) 7/12 - 4/3'.format(id_init)
        )
        polygon = Rectangle(4, 3, 7, 12, 5.6)
        self.assertEqual(str(polygon), '[Rectangle] (5.6) 7/12 - 4/3')
        polygon = Rectangle(4, 3, 7, 12, (7, 6))
        self.assertEqual(str(polygon), '[Rectangle] ((7, 6)) 7/12 - 4/3')

    def test_update(self):
        """Tests the update function.
        """
        polygon = Rectangle(5, 9, 0, 0)
        # region valid arguments
        polygon.update(1)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 9)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        polygon.update(1, 7)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 9)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        polygon.update(1, 7, 5)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        polygon.update(1, 7, 5, 2)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.x, 2)
        self.assertEqual(polygon.y, 0)
        polygon.update(1, 7, 5, 2, 9)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.x, 2)
        self.assertEqual(polygon.y, 9)
        polygon.update(1, 7, 5, 2, 9, 15)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.x, 2)
        self.assertEqual(polygon.y, 9)
        polygon.update(None, 7, 5, 2, 9, None)
        self.assertEqual(polygon.id, None)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.x, 2)
        self.assertEqual(polygon.y, 9)
        # endregion
        # region *args with **kwargs
        polygon = Rectangle(5, 9, 0, 0)
        polygon.update(1, height=44, width=12)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 9)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        polygon.update(1, width=[12, 14], height=[4, 5])
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 9)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        polygon.update(1, 7, width=12, height=78)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 9)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        polygon.update(1, 7, width={12, 3}, height={23, 6})
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 9)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        polygon.update(1, 7, 5, width=12, height=22, x=17)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        polygon.update(1, 7, 5, width=12, height=16, x='17', y='jj')
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        polygon.update(1, 7, 5, 2, width=12, x=17, height=57, y=18)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.x, 2)
        self.assertEqual(polygon.y, 0)
        polygon.update(1, 7, 5, 2, width=0, x=1.7, y=1.8, height=0)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.x, 2)
        self.assertEqual(polygon.y, 0)
        polygon.update(1, 7, 5, 2, 9, width=12, x={7, 5}, height=55, y={8, 5})
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.x, 2)
        self.assertEqual(polygon.y, 9)
        polygon.update(1, 7, 5, 2, 9, width=12, x='17', y='18', height=23)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.x, 2)
        self.assertEqual(polygon.y, 9)
        polygon.update(1, 7, 5, 2, 9, 15, height=98, width=12, x=-17, y=-18)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.x, 2)
        self.assertEqual(polygon.y, 9)
        polygon.update(1, 7, 5, 2, 9, 15, width=-12,
                       x=17, height=-7, y=(18, 54))
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.x, 2)
        self.assertEqual(polygon.y, 9)
        polygon.update(1, 7, 5, 2, 9, None, size=12, x=0, y=0, height=25)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.x, 2)
        self.assertEqual(polygon.y, 9)
        polygon.update(1, 7, 5, 2, 9, width=None, x=None, y=None, height=None)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.x, 2)
        self.assertEqual(polygon.y, 9)
        polygon.update(1, 7, 5, 2, 9, width='12', x=1.7, y=1.8, height=2.3)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.x, 2)
        self.assertEqual(polygon.y, 9)
        polygon.update(1, 7, 5, 2, width=True, height=True, x=False, y=False)
        self.assertEqual(polygon.id, 1)
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.x, 2)
        self.assertEqual(polygon.y, 9)
        # endregion
        # region **kwargs and no *args
        polygon = Rectangle(5, 9, 0, 0)
        id_init = polygon.id
        polygon.update(id='35')
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 9)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        # id has no get/set function
        polygon.update(id=None)
        self.assertEqual(polygon.id, None)
        self.assertEqual(polygon.width, 5)
        self.assertEqual(polygon.height, 9)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        polygon.update(width=7, id='35')
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 9)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        polygon.update(width=7, id='35', height=55)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 55)
        self.assertEqual(polygon.x, 0)
        self.assertEqual(polygon.y, 0)
        polygon.update(x=5, width=7, id='35', height=55)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 55)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 0)
        polygon.update(x=5, size=7, id='35', y=13, height=55)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.width, 7)
        self.assertEqual(polygon.height, 55)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 13)
        # endregion
        # region update should only update supported attributes
        polygon.update(x=5, size=7, width=3, height=12, id='35', y=2, foo=63)
        self.assertEqual(polygon.id, '35')
        self.assertEqual(polygon.width, 3)
        self.assertEqual(polygon.height, 12)
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        with self.assertRaises(AttributeError):
            print(polygon.foo == 63)
        with self.assertRaises(AttributeError):
            print(polygon.size == 7)
        # endregion
        # region update allows validations to be performed
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(width='7', id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(width=b'7', id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(width=True, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(width=False, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(width=None, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(height='7', id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(height=b'7', id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(height=True, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(height=False, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
        with self.assertRaises(TypeError) as asrt_ctxt:
            polygon.update(height=None, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'height must be an integer')
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
            polygon.update(width=0, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.update(width=-10, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'width must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.update(height=0, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'height must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.update(height=-10, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'height must be > 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.update(x=-10, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'x must be >= 0')
        with self.assertRaises(ValueError) as asrt_ctxt:
            polygon.update(y=-10, id='35')
        self.assertEqual(str(asrt_ctxt.exception), 'y must be >= 0')
        # endregion
        # region update does not recognize size
        polygon = Rectangle(5, 9)
        polygon.update(x=5, size=7, id='35', y=2)
        self.assertEqual(polygon.id, '35')
        self.assertNotEqual(polygon.width, polygon.height)
        self.assertFalse(hasattr(polygon, 'size'))
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(x=5, id='35', width=7, size='35', y=2)
        self.assertEqual(polygon.id, '35')
        self.assertNotEqual(polygon.width, polygon.height)
        self.assertFalse(hasattr(polygon, 'size'))
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(x=5, id='35', size=None, y=2)
        self.assertEqual(polygon.id, '35')
        self.assertNotEqual(polygon.width, polygon.height)
        self.assertFalse(hasattr(polygon, 'size'))
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(x=5, size=True, y=2, id='35')
        self.assertEqual(polygon.id, '35')
        self.assertNotEqual(polygon.width, polygon.height)
        self.assertFalse(hasattr(polygon, 'size'))
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        polygon.update(id='35', x=5, size=False, height=35, y=2)
        self.assertEqual(polygon.id, '35')
        self.assertNotEqual(polygon.width, polygon.height)
        self.assertFalse(hasattr(polygon, 'size'))
        self.assertEqual(polygon.x, 5)
        self.assertEqual(polygon.y, 2)
        # endregion

    def test_to_dictionary(self):
        """Tests the to_dictionary method.
        """
        polygon_0 = Rectangle(2, 3)
        id_init = getattr(polygon_0, 'id')
        dict_rect_0 = polygon_0.to_dictionary()
        self.assertDictEqual(dict_rect_0, {
            'id': id_init,
            'width': 2,
            'height': 3,
            'x': 0,
            'y': 0
        })
        polygon_1 = Rectangle(5, 12, 6, 13)
        dict_rect_1 = polygon_1.to_dictionary()
        self.assertDictEqual(dict_rect_1, {
            'id': id_init + 1,
            'width': 5,
            'height': 12,
            'x': 6,
            'y': 13
        })
        polygon_1.update(**dict_rect_0)
        dict_rect_2 = polygon_1.to_dictionary()
        self.assertDictEqual(dict_rect_0, dict_rect_2)
        self.assertFalse(dict_rect_0 is dict_rect_2)

    def test_docs(self):
        """Tests the documentation length of the Rectangle
        and TestRectangle classes.
        """
        rect_attrs = (
            '__init__',
            'width',
            'height',
            'x',
            'y',
            'area',
            'display',
            '__str__',
            'update',
            'to_dictionary',
        )
        test_rect_attrs = (
            'test_init',
            'test_attribute_validation',
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
        class_doc = Rectangle.__doc__.strip()
        self.assertGreater(len(class_doc), min_char_count)
        self.assertGreater(len(class_doc.split()), min_word_count)
        for attr_name in rect_attrs:
            self.assertIsNotNone(attr_name)
            attr = getattr(Rectangle, attr_name)
            self.assertIsNotNone(attr)
            attr_doc = attr.__doc__
            self.assertIsNotNone(attr_doc)
            attr_doc_trim = attr_doc.strip()
            self.assertGreater(len(attr_doc_trim), min_char_count)
            self.assertGreater(len(attr_doc_trim.split()), min_word_count)
        # the test class
        class_doc = TestRectangle.__doc__.strip()
        self.assertGreater(len(class_doc), min_char_count)
        self.assertGreater(len(class_doc.split()), min_word_count)
        for attr_name in test_rect_attrs:
            self.assertIsNotNone(attr_name)
            attr = getattr(TestRectangle, attr_name)
            self.assertIsNotNone(attr)
            attr_doc = attr.__doc__
            self.assertIsNotNone(attr_doc)
            attr_doc_trim = attr_doc.strip()
            self.assertGreater(len(attr_doc_trim), min_char_count)
            self.assertGreater(len(attr_doc_trim.split()), min_word_count)
