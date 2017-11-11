import Dojo.room.Office
import Dojo.room.Living_space


class Room(object):
    '''main class to be used fo room'''

    def __init__(self, room_name, room_type=None):
        ''' model for the room defining room name'''
        self.room_name = room_name
        self.room_type = room_type


    def print_room(self, room_name):
        room_list = []
        room_list.append(room_name)
        return room_list
            
    def create_room_office(self, room_type, room_name):
        if room_type == "office":
            return "An office called {} has been successfully created!".format(
                self.room_name)

    def room_name_list(self):
        list_of_rooms = []
        list_of_rooms.append(Room.room_name)
        return list_of_rooms


class Office(Room):
    def __init__(self, room_name, room_type=None):
        super(Office, self).__init__(room_name, room_type=None)
        self.type = "office"


class Living_Space(Room):
    def __init__(self, room_name):
        super(Living_Space, self).__init__(room_name)
        self.type = "living_space"
