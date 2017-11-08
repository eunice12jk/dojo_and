import Person


class Staff(Person):

    def __init__(self,first_name,last_name,staff_id,dept):
        super(Staff,self).__init__(first_name,last_name)
        self.staff_id = staff_id
        self.dept = dept
