class TestData:
    """
    Class contains of test data shared with all test cases
    """
    title = "New Title"
    content = "This is a new note"
    incorrect_title = "Neew Tilte"
    edited_title = "Edited New Title"


class TestConfig:
    """
    Class contains of config data
    """
    # please change local host value if you are running Appium Server on the different port
    local_host = "http://localhost:4723/wd/hub"
