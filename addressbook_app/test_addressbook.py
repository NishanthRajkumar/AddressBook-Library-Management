'''
    @Author: Nishanth
    @Date: 30-03-2022 17:10:00
    @Last Modified by: Nishanth
    @Last Modified time: 30-03-2022 17:10:00
    @Title: Unit testing the address book project
'''
import csv
import pickle
import unittest
from addressbook import AddressBook, Contact
from addressbook_library import AddressBookLibrary

class AddressBookTest(unittest.TestCase):

    def setUp(self) -> None:
        self.library = AddressBookLibrary()
        self.book1 = AddressBook("book1")
        self.book2 = AddressBook("book2")
        self.book1.add_contact("Nishanth", "Rajkumar", phone="9901104972")
        self.book1.add_contact("Jeffy", phone="9952429630")
        self.book2.add_contact("Nish", email="nish@gmail.com", city="Bangalore", state="KA", zip="560061")
        self.book2.add_contact("Neth", email="neth@gmail.com", city="Melbourne", state="Vic")
        self.book2.add_contact("Jeff", phone="9011090729", city="Bangalore", state="Karnataka", zip="560062")
        self.book2.add_contact("Blessy", phone="9011090728", city="Mysore", state="Karnataka", zip= "560083")

    def test_add_contact(self):
        self.assertEqual(len(self.book1.contact_list), 2)
        self.assertRaises(KeyError, self.book2.add_contact, "Nish")
    
    def test_edit_contact(self):
        self.book1.edit_contact(name="Jeffy", last_name="Raj")
        expected_contact = Contact()
        expected_contact.create_contact(first_name="Jeffy", last_name="Raj", phone="9952429630")
        updated_contact = self.book1.contact_list["Jeffy Raj"]
        self.assertEqual(updated_contact.__str__(), expected_contact.__str__())
        self.assertRaises(KeyError, self.book1.edit_contact, name="Sam", last_name="Raj")
    
    def test_delete_contact(self):
        self.book1.delete_contact(name="Nishanth Rajkumar")
        self.assertFalse("Nishanth Rajkumar" in self.book1.contact_list.keys())
    
    def test_add_multiple_contacts(self):
        contact1 = Contact()
        contact2 = Contact()
        contact3 = Contact()
        contact1.create_contact("Sam")
        contact1.create_contact("Walter")
        contact3.create_contact("Ralph")
        contact_list1 = [contact1, contact2]
        contact_list2 = [contact3, 12, "sggf"]
        self.assertTrue(self.book1.add_multiple_contacts(contact_list1))
        self.assertRaises(TypeError, self.book1.add_multiple_contacts, contact_list2)
        self.assertRaises(KeyError, self.book1.add_multiple_contacts, contact_list1)
    
    def test_add_multiple_addressbooks(self):
        self.assertTrue(self.library.add_multiple_addressbooks([self.book1, self.book2]))
        book3 = AddressBook("book2")
        self.assertRaises(KeyError, self.library.add_multiple_addressbooks, [book3])
    
    def test_location_wise_search_results(self):
        book3 = AddressBook("book3")
        book3.add_contact("Neth", phone="45011097", city="Melbourne")
        book3.add_contact("Nish", email="nish@gmail.com", state="Karnataka")
        self.library.add_multiple_addressbooks([self.book1, self.book2, book3])
        self.assertEqual(len(self.library.get_locationwise_search_result("Neth", "Melbourne", "city")), 2)
        self.assertEqual(len(self.library.get_locationwise_search_result("Nish", "KA", "state")), 1)
        self.assertEqual(len(self.library.get_locationwise_search_result("Nish", "KA")), 1)
    
    def test_location_wise_contact_list(self):
        self.assertEqual(len(self.book2.get_locationwise_contact_list("Bangalore", "city")), 2)
        self.assertEqual(len(self.book2.get_locationwise_contact_list("Karnataka")), 2)
        self.assertRaises(ValueError, self.book2.get_locationwise_contact_list, "Karnataka", "stat")
        self.assertRaises(KeyError, self.book2.get_locationwise_contact_list, "BLR", "city")
        self.assertRaises(KeyError, self.book2.get_locationwise_contact_list, "Victoria")

    def test_locationwise_count(self):
        statewise_count = self.book2.get_locationwise_count()
        citywise_count = self.book2.get_locationwise_count("city")
        self.assertEqual(len(statewise_count), 3)
        self.assertEqual(statewise_count["Karnataka"], 2)
        self.assertEqual(len(citywise_count), 3)
        self.assertEqual(citywise_count["Bangalore"], 2)
        self.assertRaises(ValueError, self.book2.get_locationwise_count, "cities")
    
    def test_contact_sort(self):
        self.book2.get_sorted_contact_list()
        self.assertEqual(list(self.book2.contact_list)[0], "Blessy")
        self.assertEqual(list(self.book2.contact_list)[-1], "Nish")

        self.book2.get_sorted_contact_list("state")
        self.assertEqual(list(self.book2.contact_list)[0], "Nish")
        self.assertEqual(list(self.book2.contact_list)[-1], "Neth")

        self.book2.get_sorted_contact_list("city")
        self.assertEqual(list(self.book2.contact_list)[0], "Nish")
        self.assertEqual(list(self.book2.contact_list)[-1], "Blessy")

        self.book2.get_sorted_contact_list("zip")
        self.assertEqual(list(self.book2.contact_list)[0], "Neth")
        self.assertEqual(list(self.book2.contact_list)[-1], "Blessy")

    def test_save_as_text_file(self):
        self.book2.save_as_txt_file()
        file_stream = open(f"{self.book2.name}.txt", mode='rb')
        content = pickle.load(file_stream)
        file_stream.close()
        self.assertEqual(self.book2.contact_list, content)
    
    def test_save_as_csv_file(self):
        self.book2.save_as_csv_file()
        file_stream = open(f"{self.book2.name}.csv", mode='r')
        csv_file = csv.reader(file_stream)
        read_header = False
        expected_list = {}
        for row in csv_file:
            contact = Contact()
            if len(row) == 0:
                continue
            if read_header == False:
                read_header = True
                continue
            contact.first_name, contact.last_name, contact.address = (row[0], row[1], row[2])
            contact.city, contact.state, contact.zip, contact.phone, contact.email = (row[3], row[4], row[5], row[6], row[7])
            expected_list[contact.name] = contact
        file_stream.close()
        self.assertEqual(self.book2.contact_list.keys(), expected_list.keys())

if __name__ == "__main__":
    unittest.main()