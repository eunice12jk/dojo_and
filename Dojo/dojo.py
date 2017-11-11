from Dojo.room.Room import *
from Dojo.person.Person import *

class Dojo(object):
    def create_room(self, arg):
        new_room = Office(arg['<room_name>'])
        print(new_room.room_name)

    def add_person(self, arg):
        new_person = Staff(arg["<first_name>"], arg["<last_name>"])
        print(new_person.first_name)

"""

import Dojo.room.Office
import Dojo.room.Living_space
import Dojo.person.Staff
import Dojo.person.Fellow
import sys
import random

class Dojo(object):
    def __init__(self):
        self.fellows = [] 
        self.staff = []
        
    def print_room(self, room_name):
        room_list = []
        room_list.append(room_name)
        print(room_list)
        
    def create_room_office(self, room_type, room_name):
        if room_type == "office":
            return "An office called {} has been successfully created!".format(
                self.room_name)
