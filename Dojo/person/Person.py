class Person(object):
    
    person_count = 0


    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name + "." + last_name + "@andeladojo.com" 
        
 
        
    
    def Name(self):
        return "{} {}".format(self.first_name,self.last_name)
        
        
    