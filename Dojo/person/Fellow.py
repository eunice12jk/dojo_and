import Person

class Fellow(Person):

    def __init__(self,first_name,last_name,fellow_id,lang):
        super(Fellow,self).__init__(first_name,last_name)
        self.fellow_id = fellow_id
        self.lang = lang
