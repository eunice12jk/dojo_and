from Dojo.room.Room import *
from Dojo.person.Person import *

class Dojo(object):
    def create_room(self, arg):
        new_room = Office(arg['<room_name>'])
        print(new_room.room_name)

    def add_person(self, arg):
        new_person = Staff(arg["<first_name>"], arg["<last_name>"])
        print(new_person.first_name)