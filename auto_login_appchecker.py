import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# urls for critical appchecks
urls = ['https://docs.google.com/spreadsheets/d/1mEhLZnwmX0VacWxECbEFmNLuXVizO05C1lu9e5mZ-Vs/edit#gid=637365405',
        'https://mysdpbc.org/',
        'https://www.palmbeachschools.org/',
        'https://hub.palmbeachschools.org/',
        'https://connected.palmbeachschools.org/simplesaml/launch.php?Source=enboard&Application=sisprod',
        'https://connected.palmbeachschools.org/simplesaml/launch.php?Source=enboard&Application=gmail',
        'https://erp.palmbeach.k12.fl.us:8005/psc/HRPRD/EMPLOYEE/HRMS/c/NUI_FRAMEWORK.PT_LANDINGPAGE.GBL?',
        'https://connected.palmbeachschools.org/simplesaml/launch.php?Source=enboard&Application=tririgaprod',
        'https://webclock.palmbeach.k12.fl.us/',
        'https://eforms.palmbeachschools.org/portal/',
        'https://connected.palmbeachschools.org/simplesaml/launch.php?Source=enboard&Application=esupport',
        'https://iq.palmbeachschools.org/WebIQ/search.aspx',
        'https://www2.palmbeachschools.org/directorysearch/indexportal.html',
        'https://connected.palmbeachschools.org/simplesaml/launch.php?Source=enboard&Application=bulletins',
        'https://go.boarddocs.com/fl/palmbeach/Board.nsf/Public',
        'https://files.palmbeachschools.org/default.aspx',
        'https://edw.palmbeachschools.org/ibmcognos/bi/?perspective=home',
        'https://connected.palmbeachschools.org/simplesaml/launch.php?Source=enboard&Application=parentlink',
        'https://destiny.palmbeachschools.org/',
        'https://apps.raptortech.com/Dashboard/Home/Index',
        'https://transintranet.palmbeachschools.org/Default.aspx',
        'https://10.254.18.202/ui/#/login'
        ]

# take user's password and username
usernamestr = input('Please input your username: ')
passwordstr = input('Please input your password, use correct capitalization: ')  # todo obfuscate entry field

# webdriver to control chrome
browser = webdriver.Chrome()


# takes in the html field names and logs in
def login(username_field, password_field, submit_field):
    username = browser.find_element(By.NAME, username_field)
    username.send_keys(usernamestr)

    password = browser.find_element(By.NAME, password_field)
    password.send_keys(passwordstr)

    submit_button = browser.find_element(By.NAME, submit_field)
    submit_button.click()

    time.sleep(2)


# open urls and login if necessary
for url in urls:
    browser.get(url)
    time.sleep(15)

    if 'erp' in url:
        login('userid', 'pwd', 'Submit')

    elif 'edw' in url:
        login()
        # todo find html name values

    elif 'files' in url:
        login()
        # todo find html name values

    elif 'transintranet' in url:
        login()
        # todo find html name values

    else:
        next()
