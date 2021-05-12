# Google Keep Python and Appium Basic Automation

This project covers basic test automation for the mobile app called "Google Keep".
Google Keep app is available in Google Play and AppStore.

Author: Katarzyna Javaheri-Szpak, katarzyna.javaheri@gmail.com

# Directory structure

```
.
├── driver.py                   # driver configs
├── page_objects.py             # Base class and POM classes 
├── requirements.in             # file using pip-compile to be compiled to reqirements.txt
├── requirements.txt            # pip requirements file
├── test_cases.py               # test cases wrapped in one scenario
├── testdata.py                 # test data and test config classes
└── README.md
```

# Technology 

- [Python](https://www.python.org/)
- [Appium](https://appium.io/)
- [Android Studio Emulator](https://developer.android.com/studio)
- [Page Object Pattern](https://selenium-python.readthedocs.io/page-objects.html)
- [Unittest](https://docs.python.org/3/library/unittest.html)


# Prerequisites

1. Download and install:
- [Android Studio](https://developer.android.com/studio)
- [Appium Desktop](https://github.com/appium/appium-desktop/releases)
  
2. Install the app on emulator and login to Google Account
- [Google Keep App](https://play.google.com/store/apps/details?id=com.google.android.keep)


3. Verify if your Appium localhost port is correct (default is: http://localhost:4723) (testdata.py)
4. Verify if device name is correct (default is: emulator-5554) (driver.py)

### How to verify a device name?

Activate the emulator in Android Studio

Run a command in terminal

```
adb devices
```
Device name should appear

# Local environment setup

To use this project Python 3.7. is required.
```
python3.7 -m venv venv
```
Activate venv:

MacOS/Linux
```
source venv/bin/activate
```
Windows
```
\path\to\env\Scripts\activate
```
Example for Windows
```
C:\Users\'Username'\venv\Scripts\activate.bat
```

```
pip install -r requirements.txt
```

### The convention for managing Python dependency is as follows:

- we add the dependency into requirements.in
- we call pip-compile to create requirements.txt
- we commit both files to repository.


# How to run the tests?

Just run a command:

```
pytest
```

in a main directory of the project