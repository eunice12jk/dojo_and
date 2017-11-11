"""
	Usage: 
			dojo add_person <first_name> <last_name> <position> [<wants_accommodation>]
			dojo create_room <room_type> <room_name>...
			dojo print_room <room>

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
	  