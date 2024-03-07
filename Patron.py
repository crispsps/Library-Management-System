#Patron

""" Patron Class
Develop a Patron class to represent library patrons with attributes like name, p_id, contact information, etc.
Implement methods for adding, updating, and removing patrons.
Include a method to display patron details."""
class Patron:
    
    def __init__(self, name, p_id, contact) -> None:
        self.name = name
        self.p_id = p_id
        self.contact = contact
        
    #p_id should not be changed, there can only be a unique p_id for each patron
    def update(self, name = None, contact = None):
        if name:
            self.name = name
        if contact:
            self.contact = contact
    
    def display(self):
        print(f'{self.name},{self.p_id},{self.contact}')
    
    def remove(self):
        del self
        