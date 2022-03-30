'''
    @Author: Nishanth
    @Date: 30-03-2022 08:16:00
    @Last Modified by: Nishanth
    @Last Modified time: 30-03-2022 08:16:00
    @Title: Management of list of address books in Library system
'''
from addressbook import AddressBook, Contact

class AddressBookLibrary:

    def __init__(self) -> None:
        self.addressbook_list: dict[str, type[AddressBook]] = {}
    
    def add_multiple_addressbooks(self, list_of_addressbooks: list[type[AddressBook]]):
        """
            Description:
                adds the list of addressbooks given to the library
            
            Parameter:
                list of addressbook objects as list
            
            Return:
                True, if all are succesfully added
        """
        for item in list_of_addressbooks:
            if isinstance(item, AddressBook) == False:
                raise TypeError("List of addressbook had non addressbook objects")
            if item.name in self.addressbook_list.keys():
                raise KeyError(f"Addresbook with name {item.name} already exists")
            self.addressbook_list[item.name] = item
        return True
    
    def get_locationwise_search_result(self, search_name: str, location_name: str, location_type: str = "state") -> list[type[Contact]]:
        """
            Description:
                search Person in a City or State across the multiple Address Books
            
            Parameter:
                search_name: name to search for in the addressbooks.
                location_name: name of location to filter the search results.
                location_type: location type should be "city" or "state". Default: "state"
            
            Return:
                returns a list of contacts from the search results
        """
        location_type = location_type.casefold()
        if location_type != "state" and location_type != "city":
            raise ValueError("Location type input must either 'state' or 'city' only")
        if location_type == "state":
            location_condition = lambda contact, state: contact.state == state
        else:
            location_condition = lambda contact, city: contact.city == city
        search_results = []
        for _, addressbook in self.addressbook_list.items():
            contact = addressbook.get_locationwise_search_result(search_name, location_condition, location_name)
            if contact != None:
                search_results.append(contact)
        return search_results