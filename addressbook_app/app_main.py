'''
    @Author: Nishanth
    @Date: 30-03-2022 08:16:00
    @Last Modified by: Nishanth
    @Last Modified time: 30-03-2022 08:16:00
    @Title: Management of list of contacts in address book
'''
from addressbook import AddressBook
from addressbook_library import AddressBookLibrary

book1 = AddressBook("book1")
book1.add_contact("Nishanth", "Rajkumar", phone="9901104972")
book1.add_contact("Jeffy", phone="9952429630")

for name, contact in book1.contact_list.items():
    print(f"{name}: {contact}")

book1.edit_contact("Jeffy", email="jeffy@gmail.com")
print(book1.contact_list["Jeffy"])

book2 = AddressBook("book2")
book2.add_contact("Nish", email="nish@gmail.com", city="Bangalore")
book2.add_contact("Neth", email="neth@gmail.com", city="Melbourne")

mylibrary = AddressBookLibrary()
mylibrary.add_multiple_addressbooks([book1, book2])

for name, addressbook in mylibrary.addressbook_list.items():
    print(f"Addressbook name: {name}")
    for name, contact in addressbook.contact_list.items():
        print(f"{name}: {contact}")