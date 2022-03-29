'''
    @Author: Nishanth
    @Date: 29-03-2022 19:38:00
    @Last Modified by: Nishanth
    @Last Modified time: 29-03-2022 17:38:00
    @Title: Management of list of contacts in address book
'''

from venv import create


class AddressBook:

    def __init__(self) -> None:
        self.contact_list = {}


class Contact:

    def __init__(self) -> None:
        self.first_name = ""
        self.last_name = ""
        self.address = ""
        self.city = ""
        self.state = ""
        self.zip = ""
        self.phone = ""
        self.email = ""
    
    def create_contact(self, first_name, last_name = None, address = None, city = None, state = None, zip = None, phone = None, email = None):
        """
            Description:
                Creates a contact using first & last names, address, city, state, zip, phone number and email
            
            Parameter:
                first name, last name, address, city, state, zip, phone number and email
            
            Return:
                None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        self.email = email