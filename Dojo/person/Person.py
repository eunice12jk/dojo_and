class Person(object):
    '''deines person in Dojo'''
    person_count = 0
    def __init__(self, first_name, last_name):
        '''main class that defines a person in the dojo'''
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + "." + last_name + "@andeladojo.com"

    def Name(self):
        '''defines a name for person'''
        return "{} {}".format(self.first_name, self.last_name)
    
juma = Person("Juma", "Nater")
print(juma.Name())
print(juma.email)