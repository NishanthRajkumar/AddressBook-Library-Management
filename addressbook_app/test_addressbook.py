'''
    @Author: Nishanth
    @Date: 29-03-2022 20:38:00
    @Last Modified by: Nishanth
    @Last Modified time: 29-03-2022 20:38:00
    @Title: Unit testing the address book project
'''
import unittest
from addressbook import AddressBook

class AddressBookTest(unittest.TestCase):

    def test_add_contact(self):
        book = AddressBook()
        book.add_contact("Nishanth", "Rajkumar", phone="9901104972")
        book.add_contact("Jeffy", phone="9952429630")

        self.assertEqual(len(book.contact_list), 2)


if __name__ == "__main__":
    unittest.main()