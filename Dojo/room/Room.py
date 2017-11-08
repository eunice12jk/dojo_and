class Room(object):

    def __init__(self,room_name):
        self.room_name = room_name
        
        
        
    def create_room(self,room_type,room_name):
        return "An {} called {} has been successfully created!".format(self.room_type,self.room_name)