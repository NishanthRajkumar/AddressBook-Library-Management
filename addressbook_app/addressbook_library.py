'''
    @Author: Nishanth
    @Date: 30-03-2022 08:16:00
    @Last Modified by: Nishanth
    @Last Modified time: 30-03-2022 08:16:00
    @Title: Management of list of address books in Library system
'''
from addressbook import AddressBook

class AddressBookLibrary:

    def __init__(self) -> None:
        self.addressbook_list = {}
    
    def add_multiple_addressbooks(self, list_of_addressbooks: list):
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