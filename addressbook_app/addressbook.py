'''
    @Author: Nishanth
    @Date: 29-03-2022 20:54:00
    @Last Modified by: Nishanth
    @Last Modified time: 29-03-2022 20:54:00
    @Title: Management of list of contacts in address book
'''


class AddressBook:

    def __init__(self) -> None:
        self.contact_list = {}
    
    def add_contact(self, first_name = "", last_name = "", address = "", city = "", state = "", zip = "", phone = "", email = ""):
        """
            Description:
                add a contact using first & last names, address, city, state, zip, 
                phone number and email to the address book
            
            Parameter:
                first name, last name, address, city, state, zip, phone number and email.
                Default value = ""
            
            Return:
                None
        """
        contact = Contact()
        contact.create_contact(first_name, last_name, address, city, state, zip, phone, email)
        self.contact_list[contact.name] = contact
    
    def edit_contact(self, name, first_name = None, last_name = None, address = None, city = None, state = None, zip = None, phone = None, email = None):
        """
            Description:
                edits the contact of the matching name.
                if updated first_name and last_name are not provided, then old name remains
            
            Parameters:
                name(name of contact to edit), first name, last name, address, city, state, zip, phone number and email
                Default value = None
                If value is not given for any parameter, that parameter is ignored when setting contact details
            
            Return:
                None
        """
        if name not in self.contact_list.keys():
            raise KeyError("Name does not match any contact")
        contact_to_edit = self.contact_list[name]
        contact_to_edit.edit_contact(first_name, last_name, address, city, state, zip, phone, email)
        if contact_to_edit.name != name:
            self.contact_list.pop(name)
            self.contact_list[contact_to_edit.name] = contact_to_edit
    
    def delete_contact(self, name):
        """
            Description:
                Deletes the contact of the matching name.
            
            Parameters:
                name(name of contact to delete)
            
            Return:
                None
        """
        if name not in self.contact_list.keys():
            raise KeyError("Name does not match any contact")
        self.contact_list.pop(name)


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
    
    def getname(self):
        """
            Description:
                Gets the full name
            Parameters:
                self
            Return:
                returs full name as string
        """
        if self.first_name == self.last_name == "":
            return ""
        if self.first_name == "":
            return self.last_name
        if self.last_name == "":
            return self.first_name
        return self.first_name + " " + self.last_name

    name = property(getname)

    def create_contact(self, first_name = "", last_name = "", address = "", city = "", state = "", zip = "", phone = "", email = ""):
        """
            Description:
                Creates a contact using first & last names, address, city, state, zip, 
                phone number and email
            
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
    
    def edit_contact(self, first_name = None, last_name = None, address = None, city = None, state = None, zip = None, phone = None, email = None):
        """
            Description:
                Creates a contact using first & last names, address, city, state, zip, 
                phone number and email
            
            Parameter:
                first name, last name, address, city, state, zip, phone number and email.
                Default value = None.
                If value is not given for any parameter, that parameter is ignored when setting contact details
            
            Return:
                None
        """
        if first_name != None:
            self.first_name = first_name
        if last_name != None:
            self.last_name = last_name
        if address != None:
            self.address = address
        if city != None:
            self.city = city
        if state != None:
            self.state = state
        if zip != None:
            self.zip = zip
        if phone != None:
            self.phone = phone
        if email != None:
            self.email = email
    
    def __str__(self) -> str:
        contact_as_string = f"First Name: {self.first_name}, "
        contact_as_string += f"Last Name: {self.last_name}, "
        contact_as_string += f"Address: {self.address}, "
        contact_as_string += f"City: {self.city}, "
        contact_as_string += f"State: {self.state}, "
        contact_as_string += f"zip: {self.zip}, "
        contact_as_string += f"Phone: {self.phone}, "
        contact_as_string += f"Email: {self.email}"
        return contact_as_string