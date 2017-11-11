import unittest
from Dojo.room.Room import Room

class TestCreateRoom(unittest.TestCase):
    '''tests cases for create room'''
    def test_create_room_successfully(self):
        '''test for create room'''
        my_class_instance = Room()
        initial_room_count = len(my_class_instance.all_rooms)
        blue_office = my_class_instance.create_room("Blue", "office")
        self.assertTrue(blue_office)
        new_room_count = len(my_class_instance.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_office_instance(self):
        '''test for the instance office in room'''
        Blue = Office('Blue')
        assertIsInstance((type(Blue)), Office)
