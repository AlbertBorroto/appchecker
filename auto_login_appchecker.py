import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# urls for critical appchecks
urls = ['https://mysdpbc.org/',
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
passwordstr = input('Please input your password: ')

# create webdriver object to control chrome
browser = webdriver.Chrome()


def login(username_field, password_field):
    """
    takes the following arguments and populates username and password into the webpage
    :param username_field: html name field of username box
    :param password_field: html name field of password box
    """
    username = browser.find_element(By.NAME, username_field)
    username.send_keys(usernamestr)

    password = browser.find_element(By.NAME, password_field)
    password.send_keys(passwordstr)


# open urls and login if necessary
# todo write code to log into webquest webpage takes additional verification.
# todo write button press for bulletins logon
for url in urls:
    browser.execute_script(f"window.open('{url}')")
    browser.switch_to.window(browser.window_handles[-1])
    time.sleep(6)

    if 'mysdpbc' in url:
        login('Username', 'Password')
        submit_button = browser.find_element(By.ID, 'login-button')
        submit_button.click()
        time.sleep(6)

    if 'erp' in url:
        login('userid', 'pwd')
        submit_button = browser.find_element(By.NAME, 'Submit')
        submit_button.click()
        time.sleep(6)

    elif 'eforms' in url:
        login('DFS__UserID', 'DFS__Password')
        submit_button = browser.find_element(By.XPATH, "//input[@type='submit']")
        submit_button.click()
        time.sleep(6)

    elif 'edw' in url:
        login('CAMUsername', 'CAMPassword')
        submit_button = browser.find_element(By.XPATH, "//button[@type='button']")
        submit_button.click()
        time.sleep(6)

    elif 'files' in url:
        login('ctl00$body$TextBoxUserID', 'ctl00$body$TextBoxPassword')
        submit_button = browser.find_element(By.NAME, 'ct100$body$ButtonLogin')
        submit_button.click()
        time.sleep(6)

    elif 'transintranet' in url:
        login('Username', 'Password')
        submit_button = browser.find_element(By.NAME, 'LoginButton')
        submit_button.click()
        time.sleep(6)

    else:
        continue

#updateruns = input("Would you like to run the Chrome update check? (y/n): ")
#for updaterun in updateruns:
        #    if "y" in updaterun:
        #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    #if "n" in updaterun:
#      continue
