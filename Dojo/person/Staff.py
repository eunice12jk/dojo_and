import Dojo.person.Person


class Staff(Person):
    '''staff class for the staff employed'''
    def __init__(self, first_name, last_name, staff_id):
        super(Staff, self).__init__(first_name, last_name)
        self.staff_id = staff_id
