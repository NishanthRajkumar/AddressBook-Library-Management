'''
    @Author: Nishanth
    @Date: 30-03-2022 08:16:00
    @Last Modified by: Nishanth
    @Last Modified time: 30-03-2022 08:16:00
    @Title: Management of list of contacts in address book
'''


class AddressBook:

    def __init__(self, name: str = "") -> None:
        self.contact_list = {}
        self.name = name
    
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
        contact_to_add = Contact()
        contact_to_add.create_contact(first_name, last_name, address, city, state, zip, phone, email)
        if contact_to_add == self.contact_list.get(contact_to_add.name):
            raise KeyError(f"{contact_to_add.name} already exists in addressbook")
        self.contact_list[contact_to_add.name] = contact_to_add
    
    def edit_contact(self, name: str, first_name: str = None, last_name: str = None, address: str = None, city: str = None, state: str = None, zip: str = None, phone: str = None, email: str = None):
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
    
    def delete_contact(self, name: str):
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
    
    def add_multiple_contacts(self, list_of_contacts: list):
        """
            Description:
                add the list of contacts to address book
            
            Parameter:
                list of contacts as list type
            
            Return:
                True if successfully added
        """
        for item in list_of_contacts:
            if isinstance(item, Contact) == False:
                raise TypeError("List of contacts had non contact objects")
            if item.name in self.contact_list.keys():
                raise KeyError(f"Contact with name {item.name} already exists")
            self.contact_list[item.name] = item
        return True


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
                phone number and email. Only give parameter of contact to update.
                The remaining values will remain same as the old value
            
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
    
    def __eq__(self, contact) -> bool:
        if isinstance(contact, Contact):
            return self.name == contact.name
        return False