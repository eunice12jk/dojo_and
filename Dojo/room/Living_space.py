import Room

class Living_Space(Room):
        def __init__(self,room_name):
            super(Living_Space,self).__init__(room_name)
            self.type = "living_space"
