#imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://branding500mg.com/whatsappapi/whatsappclass/getwhatsapp.php"
PARAMS = {}
r = requests.get(url=URL, params=PARAMS)

# extracting data in json format
data = r.json()
print(data)
phone = input("phone: ")
client = requests.Session()
#client.headers.update({'Connection': 'Keep-Alive'})
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument(f"user-data-dir=C:/Users/Grid/Desktop/whatsapp/sessions/91{phone}/")
driver = webdriver.Chrome(r'C:\chromeDriver\chromedriver.exe', chrome_options=chrome_options)
count = 0
for i in data:
    print(i['_to'])
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
