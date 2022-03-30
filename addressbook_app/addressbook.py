'''
    @Author: Nishanth
    @Date: 30-03-2022 17:10:00
    @Last Modified by: Nishanth
    @Last Modified time: 30-03-2022 17:10:00
    @Title: Management of list of contacts in address book
'''
import csv
import pickle
from typing import Callable, Type


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

    def getcity(self):
        return self.city
    def getstate(self):
        return self.state
    
    city_value = property(getcity)
    state_value = property(getstate)
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

class AddressBook:

    def __init__(self, name: str = "") -> None:
        self.name = name
        self.contact_list: dict[str, type[Contact]] = {}
        self.contact_list_by_state: dict[str, list[type[Contact]]] = {}
        self.contact_list_by_city: dict[str, list[type[Contact]]] = {}
    
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
        self.update_contact_list_by_location(contact_to_add)
    
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
    
    def add_multiple_contacts(self, list_of_contacts: list[type[Contact]]):
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
    
    def get_locationwise_search_result(self, search_name: str, location_condition: Callable[[type[Contact], str], bool], location_name: str) -> Type[Contact]:
        """
            Description:
                search Person in a City or State across the multiple Address Books
            
            Parameter:
                search_name: name to search for in the addressbooks.
                location_condition: The condition to match for location wise search result
            
            Return:
                returns a contact from the search results if available, else returns None
        """
        if search_name not in self.contact_list.keys():
            return None
        if location_condition(self.contact_list[search_name], location_name):
            return self.contact_list[search_name]
        return None

    def update_contact_list_by_location(self, contact: type[Contact]):
        """
            Description:
                Store contacts by city and state
            
            Parameter:
                contact of type Contact
            
            Return:
                None
        """
        if contact.city_value not in self.contact_list_by_city.keys():
            self.contact_list_by_city[contact.city_value] = list()
        self.contact_list_by_city[contact.city_value].append(contact)

        if contact.state_value not in self.contact_list_by_state.keys():
            self.contact_list_by_state[contact.state_value] = list()
        self.contact_list_by_state[contact.state_value].append(contact)
    
    def get_locationwise_contact_list(self, location_name: str, location_type: str = "state") -> list[type[Contact]]:
        """
            Description:
                get locationwise contact list
            
            Parameter:
                location_name: name of the location
                location_type: value is either "city" or "state". Default: "state"
            
            Return:
                returns a list of contacts 
        """
        location_type = location_type.casefold()
        if location_type != "state" and location_type != "city":
            raise ValueError("Location type input must either 'state' or 'city' only")
        if location_type == "state":
            if location_name not in self.contact_list_by_state.keys():
                raise KeyError(f"{location_name} is not in list of existing states of contacts")
            return self.contact_list_by_state[location_name]
        else:
            if location_name not in self.contact_list_by_city.keys():
                raise KeyError(f"{location_name} is not in list of existing cities of contacts")
            return self.contact_list_by_city[location_name]
    
    def get_locationwise_count(self, location_type: str = "state") -> dict[str, int]:
        """
            Description:
                returns a location wise count of the no of contacts
            
            Parameter:
                location_type: 'city' or 'state'. Default: 'state'
            
            Return:
                returns a dictionary
        """
        location_wise_count = {}
        if location_type != "state" and location_type != "city":
            raise ValueError("Location type input must either 'state' or 'city' only")
        if location_type == "state":
            for location_name, contact_list in self.contact_list_by_state.items():
                if location_name == "":
                    continue
                location_wise_count[location_name] = len(contact_list)
        else:
            for location_name, contact_list in self.contact_list_by_city.items():
                if location_name == "":
                    continue
                location_wise_count[location_name] = len(contact_list)
        return location_wise_count
    
    def get_sorted_contact_list(self, sort_by: str = "name"):
        """
            Description:
                Sorts contact list in alphabetical order
            
            Parameter:
                sort_condition is a callable type used as key selector in sorting.
                Accepted values are "name", "state", "city" and "zip"
            
            Return:
                None
        """
        sort_by = sort_by.casefold()
        if sort_by not in ["name", "state", "city", "zip"]:
            raise ValueError("Location type input must either 'state' or 'city' only")
        if sort_by == "name":
            sort_condition = lambda item: item[1].name
        elif sort_by == "state":
            sort_condition = lambda item: item[1].state
        elif sort_by == "city":
            sort_condition = lambda item: item[1].city
        elif sort_by == "zip":
            sort_condition = lambda item: item[1].zip
        self.contact_list = {key: val for key, val in sorted(self.contact_list.items(), key = sort_condition)}
    
    def save_as_txt_file(self):
        """
            Description:
                saves the contact list of the address book to text file.
                The name of the text file will be same as name of addressbook.
            
            Parameter:
                None
            
            Return:
                None
        """
        txt_file_stream = open(f"{self.name}.txt", mode='wb')
        #content = pickle.dumps(self.contact_list)
        pickle.dump(self.contact_list, txt_file_stream)
        txt_file_stream.close()
    
    def save_as_csv_file(self):
        contact_fields = ['first_name', 'last_name', 'address', 'city', 'state', 'zip', 'phone', 'email']
        csv_file_stream = open(f"{self.name}.csv", mode='w')
        csv_writer = csv.writer(csv_file_stream)
        csv_writer.writerow(contact_fields)
        for _, contact in self.contact_list.items():
            csv_writer.writerow([contact.first_name, contact.last_name, contact.address, contact.city, contact.state, contact.zip, contact.phone, contact.email])
        csv_file_stream.close()