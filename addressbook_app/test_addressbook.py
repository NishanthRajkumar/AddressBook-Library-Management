'''
    @Author: Nishanth
    @Date: 29-03-2022 20:38:00
    @Last Modified by: Nishanth
    @Last Modified time: 29-03-2022 20:38:00
    @Title: Unit testing the address book project
'''
import unittest
from addressbook import AddressBook, Contact

class AddressBookTest(unittest.TestCase):

    def setUp(self) -> None:
        self.book = AddressBook()
        self.book.add_contact("Nishanth", "Rajkumar", phone="9901104972")
        self.book.add_contact("Jeffy", phone="9952429630")

    def test_add_contact(self):
        self.assertEqual(len(self.book.contact_list), 2)
    
    def test_edit_contact(self):
        self.book.edit_contact(name="Jeffy", last_name="Raj")
        expected_contact = Contact()
        expected_contact.create_contact(first_name="Jeffy", last_name="Raj", phone="9952429630")
        updated_contact = self.book.contact_list["Jeffy Raj"]
        self.assertEqual(updated_contact.__str__(), expected_contact.__str__())
        self.assertRaises(KeyError, self.book.edit_contact, name="Sam", last_name="Raj")
    
    def test_delete_contact(self):
        self.book.delete_contact(name="Nishanth Rajkumar")
        self.assertFalse("Nishanth Rajkumar" in self.book.contact_list.keys())
    
    def test_add_multiple_contacts(self):
        contact1 = Contact()
        contact2 = Contact()
        contact3 = Contact()
        contact1.create_contact("Sam")
        contact1.create_contact("Walter")
        contact3.create_contact("Ralph")
        contact_list1 = [contact1, contact2]
        contact_list2 = [contact3, 12, "sggf"]
        self.assertTrue(self.book.add_multiple_contacts(contact_list1))
        self.assertRaises(TypeError, self.book.add_multiple_contacts, contact_list2)
        self.assertRaises(KeyError, self.book.add_multiple_contacts, contact_list1)


if __name__ == "__main__":
    unittest.main()