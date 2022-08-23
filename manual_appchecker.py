import webbrowser
import time
import subprocess

# list of critical app URLs
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

# path to chrome exe
chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'

# open a new window of chrome
subprocess.Popen(chrome_path)

# loop through urls and open them
for url in urls:
    webbrowser.open_new(url)
    time.sleep(1)