import unittest
from unittest.mock import patch

from contacts_manager.data import Data


class TestData(unittest.TestCase):

    @patch('contacts_manager.data.open')
    def test_load_contacts_existing_file(self, mock_open):
        # Mock the open function to return a valid file object
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.read.return_value = '[{"name": "John", "surname": "Doe", "telephone": "1234567890", "email": "john.doe@example.com"}]'

        data = Data()

        # Assert that one contact is loaded
        self.assertEqual(len(data.contacts), 1)

        # Assert that the contact details are correct
        self.assertEqual(data.contacts[0].name, "John")
        self.assertEqual(data.contacts[0].surname, "Doe")

    @patch('contacts_manager.data.open')
    def test_load_contacts_nonexistent_file(self, mock_open):
        # Mock the open function to raise FileNotFoundError
        mock_open.side_effect = FileNotFoundError

        data = Data()

        # Assert that contacts list remains empty
        self.assertEqual(len(data.contacts), 0)

    @patch('contacts_manager.data.open')
    def test_list_contacts_empty(self, mock_open):
        # Mock the open function to return a valid file object
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.read.return_value = '[]'

        data = Data()
        data.list_contacts()

        # Assert that 0 contact is loaded
        self.assertEqual(len(data.contacts), 0)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=["New Name", "New Surname", "New Phone", "new_email@example.com"])
    @patch('contacts_manager.data.open')
    def test_edit_contact_success(self, mock_open, mock_input, mock_print):
        # Mock data loading and contact existence
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.read.return_value = '[{"name": "John", "surname": "Doe", "telephone": "1234567890", "email": "john.doe@example.com"}]'

        data = Data()

        # Edit the first contact
        data.edit_contact(1)

        # Assert that contact details are updated
        self.assertEqual(data.contacts[0].name, "New Name")
        self.assertEqual(data.contacts[0].surname, "New Surname")
        self.assertEqual(data.contacts[0].telephone, "New Phone")
        self.assertEqual(data.contacts[0].email, "new_email@example.com")

        # Assert that the print function is called with success message
        self.assertIn("Contatto modificato", mock_print.call_args[0][0])

    @patch('builtins.print')
    def test_edit_contact_nonexistent_id(self, mock_print):
        data = Data()
        data.edit_contact(1)

        # Assert that the print function is called with error message
        self.assertIn("ID Contatto non esistente!", mock_print.call_args[0][0])

    @patch('contacts_manager.data.open')
    def test_delete_contact_success(self, mock_open):
        # Mock data loading and contact existence
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.read.return_value = '{"contacts": [{"name": "John", "surname": "Doe", "telephone": "1234567890", "email": "john.doe@email.com"}'
