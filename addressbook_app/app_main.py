from addressbook import AddressBook

book = AddressBook()
book.add_contact("Nishanth", "Rajkumar", phone="9901104972")
book.add_contact("Jeffy", phone="9952429630")

for name, contact in book.contact_list.items():
    print(f"{name}: {contact}")

book.edit_contact("Jeffy", email="jeffy@gmail.com")
print(book.contact_list["Jeffy"])