Almost a Circle
This project contains some tasks for reviewing everything learned previously in Python.

Tasks To Complete
 0. If it's not tested it doesn't work
tests/ contains unit tests for all the files, classes and methods and all Python files are PEP 8 or pycodestyle (version 2.x) validated.
 1. Base class
models/ contains a file (__init__.py) that makes the folder become a package.
models/base.py contains a class Base that will be the “base” of all other classes in this project:
Private class attribute __nb_objects = 0.
Class constructor: def __init__(self, id=None):. The public instance attribute id is assigned with this argument's value if the argument's value is not None, otherwise __nb_objects is incremented and __nb_objects's new value is assigned to the public instance attribute id.
 2. First Rectangle
models/rectangle.py contains a class Rectangle that inherits from Base:
Public instance attributes: first_name, last_name, and age.
Class constructor: def __init__(self, width, height, x=0, y=0, id=None):. Calls the super class with id and assigns the right argument to the associated private instance attribute (E.g.; __width -> width and __x -> x).
 3. Validate attributes
Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded).
The input must be an integer. width and height must be greater than 0. x and y must be greater than or equal to zero.
 4. Area first
Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.
 5. Display #0
Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character #. There's no need to handle x and y here.
 6. __str__
Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>.
 7. Display #1
Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y.
 8. Update #0
Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute. args[0] -> id, args[1] -> width, args[2] -> height, args[3] -> x, and args[4] -> y.
 9. Update #1
Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes:
**kwargs must be skipped if *args exists and is not empty.
Each key in this dictionary (**kwargs) represents an attribute to the instance.
 10. And now, the Square!
models/square.py contains a class Square that inherits from Rectangle:
Public instance attributes: first_name, last_name, and age.
Class constructor: def __init__(self, size, x=0, y=0, id=None):. Calls the super class with id, x, y, width, and height.
The overloading __str__ method should return [Square] (<id>) <x>/<y> - <size> - in this case, width or height.
 11. Square size
Update the class Square by adding the public getter and setter size:
The setter should assign (in this order) the width and the height - with the same value.
The setter should have the same value validation as the Rectangle for width and height - No need to change the exception error message (It should be the one from width).
 12. Square update
Update the class Square by adding the public method def update(self, *args, **kwargs): that assigns attributes:
*args is the list of arguments. args[0] -> id, args[1] -> size, args[2] -> x, and args[3] -> y.
**kwargs must be skipped if *args exists and is not empty.
Each key in this dictionary (**kwargs) represents an attribute to the instance.
 13. Rectangle instance to dictionary representation
Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle. This dictionary must contain id, width, height, x, and y.
 14. Square instance to dictionary representation
Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square. This dictionary must contain id, size, x, and y.
 15. Dictionary to JSON string
Update the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries:
list_dictionaries is a list of dictionaries.
If list_dictionaries is None or empty, return the string: "[]".
 16. JSON string to file
Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file:
list_objs is a list of instances who inherit from Base - example: list of Rectangle.
If list_objs is None, save an empty list.
The filename must be: <Class name>.json - example: Rectangle.json.
You must use the static method to_json_string.
You must overwrite the file if it already exists.
 17. JSON string to dictionary
Update the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string:
json_string is a string representing a list of dictionaries.
If json_string is None or empty, return an empty list.
 18. Dictionary to Instance
Update the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set:
You must use the method def update(self, *args, **kwargs).
**dictionary must be used as **kwargs of the method update.
You are not allowed to use eval.
 19. File to Instance
Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances:
The filename must be: <Class name>.json - example: Rectangle.json.
If the file doesn’t exist, return an empty list.
The type of these instances depends on cls (current class using this method).
You must use the previously implemented from_json_string and create methods.
 20. JSON ok, but CSV?
Update the class Base by adding the class methods def save_to_file_csv(cls, list_objs): and def load_from_file_csv(cls): that serializes and deserializes in CSV:
The filename must be: <Class name>.csv - example: Rectangle.csv.
Has the same behavior as the JSON serialization/deserialization
Format of the CSV:
Rectangle: <id>,<width>,<height>,<x>,<y>.
Square: <id>,<size>,<x>,<y>.
 21. Let's draw it
Update the class Base by adding the static method def draw(list_rectangles, list_squares): that opens a window and draws all the Rectangles and Squares:
You must use the Turtle graphics module.
No constraints for color, shape etc… be creative!
