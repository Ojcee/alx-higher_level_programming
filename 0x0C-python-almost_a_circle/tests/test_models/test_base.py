#!/usr/bin/python3
"""A unit test module for the polygon models.
"""
import os
import unittest
import json
from importlib import import_module


Base = import_module('.base', package='models').Base
Rectangle = import_module('.rectangle', package='models').Rectangle
Square = import_module('.square', package='models').Square


def remove_files():
    """Removes the serialized polygon object files
    from the current working directory.
    """
    if os.path.isfile('Base.json'):
        os.unlink('Base.json')
    if os.path.isfile('Rectangle.json'):
        os.unlink('Rectangle.json')
    if os.path.isfile('Square.json'):
        os.unlink('Square.json')
    if os.path.isfile('Base.csv'):
        os.unlink('Base.csv')
    if os.path.isfile('Rectangle.csv'):
        os.unlink('Rectangle.csv')
    if os.path.isfile('Square.csv'):
        os.unlink('Square.csv')


def read_text_file(file_name):
    """Reads the contents of a given file.
    Args:
        file_name (str): The name of the file to read.
    Returns:
        str: The contents of the file if it exists.
    """
    lines = []
    if os.path.isfile(file_name):
        with open(file_name, mode='r') as file:
            for line in file.readlines():
                lines.append(line)
    return ''.join(lines)


class TestBase(unittest.TestCase):
    """Tests the Base class and its methods.
    """

    def test_init(self):
        """Tests the initialization of the Base class.
        """
        polygon = Base()
        id_init = polygon.id
        polygon = Base()
        self.assertEqual(polygon.id, id_init + 1)
        polygon = Base('0x10')
        self.assertEqual(polygon.id, '0x10')
        polygon = Base()
        self.assertEqual(polygon.id, id_init + 2)
        polygon = Base([1, 5])
        self.assertListEqual(polygon.id, [1, 5])
        polygon = Base()
        self.assertEqual(polygon.id, id_init + 3)
        polygon = Base(None)
        self.assertIsNotNone(polygon.id)
        self.assertEqual(polygon.id, id_init + 4)
        polygon = Base(False)
        self.assertEqual(polygon.id, False)
        polygon = Base(True)
        self.assertEqual(polygon.id, True)
        with self.assertRaises(AttributeError):
            polygon.__nb_objects += 1
        with self.assertRaises(TypeError):
            polygon = Base(1, 2)

    def test_to_json_string(self):
        """Tests the to_json_string method of the Base class.
        """
        self.assertEqual(Base.to_json_string(None),
                         '[]')
        self.assertEqual(Base.to_json_string(
            [
                {'id': 1, 'width': 2, 'height': 3, 'x': 5, 'y': 5},
                {'id': None, 'width': 2, 'height': 3, 'x': 5, 'y': 0},
                {'id': 2, 'width': 10, 'height': 3, 'x': 0, 'y': 0}
            ]),
            '[{"id": 1, "width": 2, "height": 3, "x": 5, "y": 5}, ' +
            '{"id": null, "width": 2, "height": 3, "x": 5, "y": 0}, ' +
            '{"id": 2, "width": 10, "height": 3, "x": 0, "y": 0}]')
        self.assertEqual(Base.to_json_string(
            [
                {'id': 1, 'size': 2, 'x': 5, 'y': 5},
                {'id': '34', 'size':    25, 'x': 5,   'y': 0},
                {'id': 2, 'size': 10, 'x': 0,   'y': 0}
            ]),
            '[{"id": 1, "size": 2, "x": 5, "y": 5}, ' +
            '{"id": "34", "size": 25, "x": 5, "y": 0}, ' +
            '{"id": 2, "size": 10, "x": 0, "y": 0}]')
        self.assertEqual(Base.to_json_string([None, False, 1]),
                         '[null, false, 1]')
        self.assertEqual(Base.to_json_string(True),
                         'true')
        self.assertEqual(Base.to_json_string(False),
                         'false')
        self.assertEqual(Base.to_json_string(55),
                         '55')
        self.assertEqual(Base.to_json_string('55'),
                         '"55"')

    def test_save_to_file(self):
        """Tests the save_to_file function of the Base class.
        """
        # region Base
        polygons = None
        remove_files()
        Base.save_to_file(polygons)
        self.assertEqual(read_text_file('Base.json'), '[]')
        self.assertFalse(os.path.isfile('Rectangle.json'))
        self.assertFalse(os.path.isfile('Square.json'))
        polygons = []
        remove_files()
        Base.save_to_file(polygons)
        self.assertEqual(read_text_file('Base.json'), '[]')
        self.assertFalse(os.path.isfile('Square.json'))
        self.assertFalse(os.path.isfile('Rectangle.json'))
        polygons = [Base(3), Base(10)]
        with self.assertRaises(AttributeError):
            remove_files()
            Base.save_to_file(polygons)
        polygons = [Square(3, 0, 0, 1), Square(10, 9, 7, 8)]
        remove_files()
        Base.save_to_file(polygons)
        self.assertEqual(read_text_file('Base.json'), '[]')
        self.assertFalse(os.path.isfile('Square.json'))
        self.assertFalse(os.path.isfile('Rectangle.json'))
        polygons = [Rectangle(5, 13, 0, 0, 1), Rectangle(10, 2, 9, 7, 8)]
        remove_files()
        Base.save_to_file(polygons)
        self.assertEqual(read_text_file('Base.json'), '[]')
        self.assertFalse(os.path.isfile('Square.json'))
        self.assertFalse(os.path.isfile('Rectangle.json'))
        polygons = [Square(3, 0, 0, 1), Rectangle(10, 3, 9, 7, 8), Base(2)]
        with self.assertRaises(AttributeError):
            remove_files()
            Base.save_to_file(polygons)
        with self.assertRaises(TypeError):
            Base.save_to_file(polygons, polygons)
        # endregion
        # region Rectangle
        polygons = None
        remove_files()
        Rectangle.save_to_file(polygons)
        self.assertEqual(read_text_file('Rectangle.json'), '[]')
        polygons = []
        remove_files()
        Rectangle.save_to_file(polygons)
        self.assertEqual(read_text_file('Rectangle.json'), '[]')
        polygons = [Rectangle(3, 5, 0, 0, 1), Rectangle(10, 4, 9, 7, 8)]
        remove_files()
        Rectangle.save_to_file(polygons)
        contents = read_text_file('Rectangle.json')
        self.assertIn('"id": 1', contents)
        self.assertIn('"width": 3', contents)
        self.assertIn('"height": 5', contents)
        self.assertIn('"x": 0', contents)
        self.assertIn('"y": 0', contents)
        self.assertIn('"id": 8', contents)
        self.assertIn('"width": 10', contents)
        self.assertIn('"height": 4', contents)
        self.assertIn('"x": 9', contents)
        self.assertIn('"y": 7', contents)
        polygons = [Rectangle(3, 5, 0, 0, 1), Base(34), Square(10, 9, 7, 8)]
        remove_files()
        Rectangle.save_to_file(polygons)
        contents = read_text_file('Rectangle.json')
        self.assertIn('"id": 1', contents)
        self.assertIn('"width": 3', contents)
        self.assertIn('"height": 5', contents)
        self.assertIn('"x": 0', contents)
        self.assertIn('"y": 0', contents)
        self.assertNotIn('"id": 34', contents)
        self.assertNotIn('"id": 8', contents)
        self.assertNotIn('"size": 10', contents)
        self.assertNotIn('"width": 10', contents)
        self.assertNotIn('"height": 10', contents)
        self.assertNotIn('"x": 9', contents)
        self.assertNotIn('"y": 7', contents)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(polygons, polygons)
        # endregion
        # region Square
        polygons = None
        remove_files()
        Square.save_to_file(polygons)
        self.assertEqual(read_text_file('Square.json'), '[]')
        polygons = []
        remove_files()
        Square.save_to_file(polygons)
        self.assertEqual(read_text_file('Square.json'), '[]')
        polygons = [Square(3, 0, 0, 1), Square(10, 9, 7, 8)]
        remove_files()
        Square.save_to_file(polygons)
        contents = read_text_file('Square.json')
        self.assertIn('"id": 1', contents)
        self.assertIn('"size": 3', contents)
        self.assertNotIn('"width": 3', contents)
        self.assertNotIn('"height": 3', contents)
        self.assertIn('"x": 0', contents)
        self.assertIn('"y": 0', contents)
        self.assertIn('"id": 8', contents)
        self.assertIn('"size": 10', contents)
        self.assertNotIn('"width": 10', contents)
        self.assertNotIn('"height": 10', contents)
        self.assertIn('"x": 9', contents)
        self.assertIn('"y": 7', contents)
        polygons = [Square(3, 0, 0, 1), Rectangle(10, 5, 9, 7, 8), Base(11)]
        remove_files()
        Square.save_to_file(polygons)
        contents = read_text_file('Square.json')
        self.assertIn('"id": 1', contents)
        self.assertIn('"size": 3', contents)
        self.assertNotIn('"width": 3', contents)
        self.assertNotIn('"height": 3', contents)
        self.assertIn('"x": 0', contents)
        self.assertIn('"y": 0', contents)
        self.assertNotIn('"id": 8', contents)
        self.assertNotIn('"size": 10', contents)
        self.assertNotIn('"size": 5', contents)
        self.assertNotIn('"width": 10', contents)
        self.assertNotIn('"height": 5', contents)
        self.assertNotIn('"x": 9', contents)
        self.assertNotIn('"y": 7', contents)
        self.assertNotIn('"id": 11', contents)
        with self.assertRaises(TypeError):
            Square.save_to_file(polygons, polygons)
        # endregion
        remove_files()

    def test_from_json_string(self):
        """Tests the from_json_string static method of the Base class.
        """
        polygon_list = Base.from_json_string('null')
        self.assertEqual(polygon_list, None)
        polygon_list = Rectangle.from_json_string('34')
        self.assertEqual(polygon_list, 34)
        polygon_list = Square.from_json_string('"foo_bar"')
        self.assertEqual(polygon_list, 'foo_bar')
        polygon_list = Base.from_json_string('[-4, 1, 2, 5]')
        self.assertEqual(polygon_list, [-4, 1, 2, 5])
        polygon_list = Rectangle.from_json_string(
            '[{"y": 8, "id": 89, "width": 10, "x": 4, "height": 4}]'
        )
        self.assertEqual(
            polygon_list,
            [{'id': 89, 'width': 10, 'height': 4, 'x': 4, 'y': 8}]
        )
        polygon_list = Square.from_json_string(
            '[{"id": 98, "x": 15, "size": 30, "y": 10}]'
        )
        self.assertEqual(
            polygon_list,
            [{'id': 98, 'size': 30, 'x': 15, 'y': 10}]
        )
        with self.assertRaises(json.JSONDecodeError):
            polygon_list = Base.from_json_string('[{"id": 45, "x": 3')
        with self.assertRaises(TypeError):
            polygon_list = Base.from_json_string('[{"id": 45, "x": 3', '34')

    def test_create(self):
        """Tests the create method of the Base class.
        """
        polygon = Base.create(**{
            'id': '89',
        })
        self.assertIsNone(polygon)
        # region Rectangle
        polygon = Rectangle.create(**{
            'id': '89', 'width': 3, 'height': 5,
            'x': 8, 'y': 16
        })
        self.assertEqual(polygon.id, '89')
        self.assertEqual(polygon.width, 3)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.x, 8)
        self.assertEqual(polygon.y, 16)
        polygon = Rectangle.create(**{
            'id': None, 'width': 3, 'height': 5,
            'x': 8, 'y': 16, 'foo': 23
        })
        self.assertEqual(polygon.id, None)
        self.assertEqual(polygon.width, 3)
        self.assertEqual(polygon.height, 5)
        self.assertEqual(polygon.x, 8)
        self.assertEqual(polygon.y, 16)
        with self.assertRaises(AttributeError):
            print(polygon.foo)
        # endregion
        # region Square
        polygon = Square.create(**{
            'id': '89', 'width': 3, 'height': 5,
            'size': 15, 'x': 8, 'y': 16
        })
        self.assertEqual(polygon.id, '89')
        self.assertEqual(polygon.size, 15)
        self.assertEqual(polygon.x, 8)
        self.assertEqual(polygon.y, 16)
        polygon = Square.create(**{
            'id': None, 'width': 13, 'height': 25,
            'x': 8, 'y': 16, 'foo': 34
        })
        self.assertEqual(polygon.id, None)
        self.assertNotEqual(polygon.size, 13)
        self.assertNotEqual(polygon.width, 13)
        self.assertNotEqual(polygon.height, 25)
        self.assertEqual(polygon.size, polygon.width)
        self.assertEqual(polygon.size, polygon.height)
        self.assertEqual(polygon.x, 8)
        self.assertEqual(polygon.y, 16)
        with self.assertRaises(AttributeError):
            print(polygon.foo)
        # endregion

    def test_load_from_file(self):
        """Tests the load_from_file class method.
        """
        # region Base
        remove_files()
        polygons = Base.load_from_file()
        self.assertTrue(len(polygons) == 0)
        polygons_list = [Base(3), Base(10)]
        with self.assertRaises(AttributeError):
            Base.save_to_file(polygons_list)
        # endregion
        # region Rectangle
        remove_files()
        polygons = Rectangle.load_from_file()
        self.assertTrue(len(polygons) == 0)
        polygons_list = [Rectangle(3, 17, 0, 0, 1), Rectangle(10, 5, 9, 7, 8)]
        Rectangle.save_to_file(polygons_list)
        polygons = Rectangle.load_from_file()
        self.assertTrue(len(polygons) == len(polygons_list))
        self.assertTrue(
            polygons[0].to_dictionary() == polygons_list[0].to_dictionary() or
            polygons[0].to_dictionary() == polygons_list[1].to_dictionary()
        )
        self.assertTrue(
            polygons[1].to_dictionary() == polygons_list[0].to_dictionary() or
            polygons[1].to_dictionary() == polygons_list[1].to_dictionary()
        )
        # endregion
        # region Square
        remove_files()
        polygons = Square.load_from_file()
        self.assertTrue(len(polygons) == 0)
        polygons_list = [Square(3, 0, 0, 1), Square(10, 9, 7, 8)]
        Square.save_to_file(polygons_list)
        polygons = Square.load_from_file()
        self.assertTrue(len(polygons) == len(polygons_list))
        self.assertTrue(
            polygons[0].to_dictionary() == polygons_list[0].to_dictionary() or
            polygons[0].to_dictionary() == polygons_list[1].to_dictionary()
        )
        self.assertTrue(
            polygons[1].to_dictionary() == polygons_list[0].to_dictionary() or
            polygons[1].to_dictionary() == polygons_list[1].to_dictionary()
        )
        # endregion
        remove_files()

    def test_docs(self):
        """Tests the documentation length of the Square
        and TestSquare classes.
        """
        base_attrs = (
            '__init__',
            'to_json_string',
            'save_to_file',
            'from_json_string',
            'create',
            'load_from_file',
            'save_to_file_csv',
            'load_from_file_csv',
            'draw',
        )
        test_base_attrs = (
            'test_init',
            'test_to_json_string',
            'test_save_to_file',
            'test_from_json_string',
            'test_create',
            'test_load_from_file',
            'test_docs',
        )
        min_char_count = 20
        min_word_count = 3
        class_doc = Base.__doc__.strip()
        self.assertGreater(len(class_doc), min_char_count)
        self.assertGreater(len(class_doc.split()), min_word_count)
        for attr_name in base_attrs:
            self.assertIsNotNone(attr_name)
            attr = getattr(Base, attr_name)
            self.assertIsNotNone(attr)
            attr_doc = attr.__doc__
            self.assertIsNotNone(attr_doc)
            attr_doc_trim = attr_doc.strip()
            self.assertGreater(len(attr_doc_trim), min_char_count)
            self.assertGreater(len(attr_doc_trim.split()), min_word_count)
        # the test class
        class_doc = TestBase.__doc__.strip()
        self.assertGreater(len(class_doc), min_char_count)
        self.assertGreater(len(class_doc.split()), min_word_count)
        for attr_name in test_base_attrs:
            self.assertIsNotNone(attr_name)
            attr = getattr(TestBase, attr_name)
            self.assertIsNotNone(attr)
            attr_doc = attr.__doc__
            self.assertIsNotNone(attr_doc)
            attr_doc_trim = attr_doc.strip()
            self.assertGreater(len(attr_doc_trim), min_char_count)
            self.assertGreater(len(attr_doc_trim.split()), min_word_count)
