#after getting json file - (see in Readme)
# step-1
import json
file = open('sub.json',)
data = json.load(file)
LINK = "https://youtube.com/channel/"
with open('channel_links','w') as c_file:
    for i in data['body']['outline']['outline']:
        CHANNEL_ID = i['@xmlUrl'].split('channel_id=')[1]
        FULL_LINK = LINK + CHANNEL_ID + '\n'
        c_file.write(FULL_LINK)

# step-2
import selenium
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
MAIL_ID = 'mail.id@gmail.com' # your mail id
PASSWORD = 'password@123' # your password
chrome_options = Options()
chrome_options.add_argument("--disable-user-media-security=true")
from selenium import webdriver
PATH = "C:\\Users\\MANOJ\\Downloads\\chromedriver.exe" # your path where chrome driver is installed
driver = webdriver.Chrome(PATH,chrome_options=chrome_options)
driver.get('https://accounts.google.com/ServiceLogin?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620')
try:
    element = WebDriverWait(driver,20).until(
            EC.presence_of_element_located((By.ID,'identifierId'))
    )
    driver.find_element_by_id('identifierId').send_keys('MAIL_ID') # Entering username
    driver.find_element_by_id('identifierNext').click() # Clicking next
    try:
        time.sleep(10) # wait until page gets load
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type=password]"))
        )
        driver.find_element_by_css_selector("input[type=password]").send_keys("PASSWORD") # Entering password
        driver.find_element_by_id('passwordNext').click() # Clicking next
        time.sleep(10)
        with open('channel_links','r') as ffile:
            for link in ffile:
                try:
                    driver.get(link.rstrip())
                    driver.get(link.rstrip())
                    time.sleep(3)
                    driver.find_element_by_id('subscribe-button').click()
                    print(link) # print name of subscribed channel
                except:
                    print(link.rstrip(),'-------------------')  # print name of unable to subscribe channel
                    continue
    except Exception as e:
        print(e)
        driver.quit()
except:
    driver.quit()
driver.quit()
  
