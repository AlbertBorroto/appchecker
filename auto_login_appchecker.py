import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

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


def login(username_field, password_field, submit_field):
    """
    takes the following arguments and logs into the webpage
    :param username_field: html name field of username box
    :param password_field: html name field of password box
    :param submit_field: html type field for the submit button
    :return:
    """
    username = browser.find_element(By.NAME, username_field)
    username.send_keys(usernamestr)

    password = browser.find_element(By.NAME, password_field)
    password.send_keys(passwordstr)

    submit_button = browser.find_element(By.XPATH, f"//input[@type='{submit_field}']")
    submit_button.click()

    time.sleep(5)


# open urls and login if necessary
# todo write code to log into webquest webpage takes additional verification.
# todo write button press for bulletins logon
for url in urls:
    browser.get(url)
    time.sleep(8)

    if 'mysdpbc' in url:
        login('Username', 'Password', 'submit')

    if 'erp' in url:
        login('userid', 'pwd', 'submit')

    elif 'eforms' in url:
        login('DFS__UserID', 'DFS__Password', 'submit')

    elif 'edw' in url:
        login('CAMUsername', 'CAMPassword', 'button')
        # todo write specific log in since xpath varies from other urls

    elif 'files' in url:
        login('ctl00$body$TextBoxUserID', 'ctl00$body$TextBoxPassword', 'submit')

    elif 'transintranet' in url:
        login('UserName', 'Password', 'submit')

    else:
        continue
