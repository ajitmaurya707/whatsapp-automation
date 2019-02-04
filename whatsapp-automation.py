#imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://example.com/yourdataurl.php"
'''
Data json example
[{'id': '12', '_user_id': '13', '_from': 'xxxxxxxxxx', '_to': 'xxxxxxxxxx', '_message': 'Whatsapp-automation A bulk whatsapp messaging app', '_apikey': 'NWM1MTc2N2UxYWY3Zg==', 'is_sent': '0'}, {'id': '11', '_user_id': '13', '_from': 'xxxxxxxxxx', '_to': 'xxxxxxxxxx', '_message': 'Whatsapp-automation A bulk whatsapp messaging app', '_apikey': 'NWM1MTc2N2UxYWY3Zg==', 'is_sent': '0'}, {'id': '10', '_user_id': '11', '_from': 'xxxxxxxxxx', '_to': '8126458906', '_message': 'Whatsapp-automation A bulk whatsapp messaging app', '_apikey': 'NWM1MDRhNWEwZjZkOA==', 'is_sent': '0'}, {'id': '13', '_user_id': '13', '_from': 'xxxxxxxxxx', '_to': '9717746592', '_message': 'Whatsapp-automation A bulk whatsapp messaging app', '_apikey': 'NWM1MTc2N2UxYWY3Zg==', 'is_sent': '0'}, {'id': '14', '_user_id': '13', '_from': 'xxxxxxxxxx', '_to': '9555061457', '_message': 'Whatsapp-automation A bulk whatsapp messaging app', '_apikey': 'NWM1MTc2N2UxYWY3Zg==', 'is_sent': '0'}, {'id': '15', '_user_id': '11', '_from': 'xxxxxxxxxx', '_to': '9990377643', '_message': 'Whatsapp-automation A bulk whatsapp messaging app', '_apikey': 'NWM1MDRhNWEwZjZkOA==', 'is_sent': '0'}]
You can change data format as you want
'''
PARAMS = {}
r = requests.get(url=URL, params=PARAMS)

# extracting data in json format
data = r.json()
#input number from which you want to send whatsapp message
phone = input("phone: ")
client = requests.Session()
#client.headers.update({'Connection': 'Keep-Alive'})
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
#Change user-data-dir path with your local path, where you want to save session
chrome_options.add_argument(f"user-data-dir=C:/Users/Grid/Desktop/whatsapp/sessions/91{phone}/")

#Change chrome driver path driver = webdriver.Chrome(r'C:\chromeDriver\chromedriver.exe', chrome_options=chrome_options)
driver = webdriver.Chrome(r'C:\chromeDriver\chromedriver.exe', chrome_options=chrome_options)
count = 0
for i in data:
    driver.get(f"https://web.whatsapp.com/send?phone=91{i['_to']}")
    if count >= 1:
        alert = driver.switch_to.alert
        alert.accept()
    while True:
        try:
            driver.find_element_by_class_name("_3F6QL").send_keys(i['_message'])
            break
        except Exception as e:
            pass

    while True:
        try:
            driver.find_element_by_class_name("_35EW6").click()
            print("Now sleep")
            break
        except Exception as e:
            pass
    count +=1
driver.close()
