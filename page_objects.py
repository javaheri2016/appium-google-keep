from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from testdata import TestData


class BaseTest:
    """
    Helping functions
    """

    def __init__(self, driver):
        self.driver = driver

    def do_wait_and_click(self, loc, sec=5):
        WebDriverWait(self.driver.instance, sec).until(EC.visibility_of_element_located(loc)).click()

    def get_element_text(self, loc, sec=5):
        elem_txt = WebDriverWait(self.driver.instance, sec).until(EC.visibility_of_element_located(loc)).text
        return elem_txt

    def do_send_keys(self, loc, text, sec=5):
        WebDriverWait(self.driver.instance, sec).until(EC.visibility_of_element_located(loc)).send_keys(text)

    def do_clear(self, loc, sec=5):
        WebDriverWait(self.driver.instance, sec).until(EC.visibility_of_element_located(loc)).clear()

    def is_visible(self, loc, sec=5):
        el = False
        try:
            el = WebDriverWait(self.driver.instance, sec).until(EC.visibility_of_element_located(loc)).is_displayed()
        except (TimeoutException, NoSuchElementException):
            return bool(el)
        return bool(el)


class MainScreen(BaseTest, TestData):

    new_note_btn = (MobileBy.ACCESSIBILITY_ID, "New list")
    whole_note = (MobileBy.ID, "com.google.android.keep:id/browse_note_interior_content")
    empty_view = (MobileBy.XPATH,
                  "//*[@resource-id='com.google.android.keep:id/empty_view_text']")
    added_note_title = (MobileBy.ID, "com.google.android.keep:id/index_note_title")
    search_bar = (MobileBy.ID, "com.google.android.keep:id/toolbar")
    search_query = (MobileBy.ID, "com.google.android.keep:id/search_actionbar_query_text")
    get_started = (MobileBy.ID, "com.google.android.keep:id/skip_welcome")
    no_thanks = (MobileBy.XPATH, "//android.widget.Button[@text='No, thanks']")

    def __init__(self, driver):
        self.driver = driver

    def get_started_btn(self):
        """
        Clicks on Get started button if visible
        """
        if self.is_visible(self.get_started) is True:
            self.do_wait_and_click(self.get_started)
        else:
            pass

    def google_offer_skip(self):
        """
        Skips Google offer bar if visible
        """
        if self.is_visible(self.no_thanks) is True:
            self.do_wait_and_click(self.no_thanks)
        else:
            pass

    def is_empty(self):
        """
        Verifies if main screen is empty - without any notes
        """
        assert self.is_visible(self.empty_view) is True

    def add_a_note(self):
        """
        Adds new note
        """
        self.do_wait_and_click(self.new_note_btn)

    def search_a_note(self):
        """
        Searches for a note with chosen title
        """
        self.do_wait_and_click(self.search_bar)
        self.do_send_keys(self.search_query, TestData.title)
        assert self.is_visible(self.added_note_title) is True

    def search_a_note_no_result(self):
        """
        Searches for a note with incorrect title
        """
        self.do_wait_and_click(self.search_bar)
        self.do_send_keys(self.search_query, TestData.incorrect_title)
        assert self.is_visible(self.empty_view) is True

    def open_a_note(self):
        """
        Opens a note
        """
        self.do_wait_and_click(self.added_note_title)

    def verify_if_note_exist(self, title):
        """
        Verifies if note with chosen title exists on the main scene
        """
        title_text = self.get_element_text(self.added_note_title)
        assert title_text == title


class NoteScreen(MainScreen):
    note_title = (MobileBy.ID, "com.google.android.keep:id/editable_title")
    note_content = (MobileBy.ID, "com.google.android.keep:id/description")
    note_edit_text = (MobileBy.ID, "com.google.android.keep:id/edit_note_text")
    note_checklist_item = (MobileBy.ACCESSIBILITY_ID, "New list")
    arrow_back = (MobileBy.ACCESSIBILITY_ID, "Navigate up")
    three_dots = (MobileBy.ACCESSIBILITY_ID, "Action")
    delete = (MobileBy.XPATH, "//android.widget.LinearLayout[1]/android.widget.ImageView")

    def __init__(self, driver):
        self.driver = driver

    def add_title(self):
        """
        Adds title to a note
        """
        self.do_wait_and_click(self.note_title)
        self.do_send_keys(self.note_title, TestData.title)

    def add_note_content(self):
        """
        Adds content to a note
        """
        self.do_wait_and_click(self.note_edit_text)
        self.do_send_keys(self.note_edit_text, TestData.content)

    def edit_note_title(self):
        """
        Edits a note's title
        """
        self.do_clear(self.note_title)
        self.do_send_keys(self.note_title, TestData.edited_title)

    def delete_a_note(self):
        """
        Deletes a note
        """
        self.do_wait_and_click(self.three_dots)
        self.do_wait_and_click(self.delete)

    def go_back_to_main(self):
        """
        Goes back to the main screen
        """
        self.do_wait_and_click(self.arrow_back)
        assert self.is_visible(self.new_note_btn) is True




