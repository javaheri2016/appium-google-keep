import unittest
from appium.webdriver.common.mobileby import MobileBy
from page_objects import MainScreen, NoteScreen
from driver import Driver
from testdata import TestData


class NotesTestCases(unittest.TestCase):

    def setUp(self):
        """
        Initializes a driver
        """
        self.driver = Driver()

    def test_verify_empty_notes(self):
        """
        Verifies if main screen is empty
        """
        main = MainScreen(self.driver)
        main.get_started_btn()
        main.google_offer_skip()
        main.is_empty()

    def test_add_a_note(self):
        """
        Adds a new note
        """
        main = MainScreen(self.driver)
        note = NoteScreen(self.driver)
        main.add_a_note()
        note.add_title()
        note.go_back_to_main()
        main.verify_if_note_exist(TestData.title)

    def test_search_a_note(self):
        """
        Search for a note
        """
        main = MainScreen(self.driver)
        note = NoteScreen(self.driver)
        main.search_a_note()
        note.go_back_to_main()

    def test_edit_a_note(self):
        """
        Edits a note
        """
        main = MainScreen(self.driver)
        note = NoteScreen(self.driver)
        main.open_a_note()
        note.edit_note_title()
        note.go_back_to_main()
        main.verify_if_note_exist(TestData.edited_title)

    def test_search_not_existed_note(self):
        """
        Search a note by old title - before edition
        """
        main = MainScreen(self.driver)
        main.search_a_note_no_result()

    def test_delete_a_note(self):
        """
        Deletes a note
        """
        main = MainScreen(self.driver)
        note = NoteScreen(self.driver)
        main.open_a_note()
        note.delete_a_note()
        main.is_empty()

    def tearDown(self):
        """
        Turns off a driver
        """
        self.driver.instance.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(NotesTestCases)
    unittest.TextTestRunner(verbosity=2).run(suite)
