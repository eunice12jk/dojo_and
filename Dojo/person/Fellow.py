import Dojo.person.Person

class Fellow(Person):
    '''defines a fellow on the Dojo'''
    def __init__(self, first_name, last_name, fellow_id):
        '''defines a person by name'''
        super(Fellow, self).__init__(first_name, last_name)
        self.fellow_id = fellow_id
