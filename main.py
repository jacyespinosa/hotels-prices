from selenium import webdriver
import time

EMAIL = "EMAIL"
PASSWORD = "PASSWORD"
DESTINATION = 'Hyatt Regency Coconut Point Resort & Spa'
# chrome_driver_path = "/Users/jacy.espinosa/Documents/chromedriver"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

chrome_driver_path = "/Users/jacy.espinosa/Documents/chromedriver"
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(chrome_options=options, executable_path=chrome_driver_path)


driver.get("https://www.hotels.com/")



def login():
    email = driver.find_element_by_xpath('//*[@id="sign-in-email"]')
    password = driver.find_element_by_xpath('//*[@id="sign-in-password"]')
    #Enter Email
    email.send_keys(EMAIL)
    time.sleep(0.1)
    password.send_keys(PASSWORD)

    submit = driver.find_element_by_xpath('//*[@id="sign-in-button"]')
    submit.click()


while True:
    #ENTER DESTINATION INFORMATION
    destination = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div/form/div[1]/div/div/div/div/input')
    destination.send_keys(DESTINATION)

    #CLOSE POPUP
    try:
        popup = driver.find_element_by_xpath('//*[@id="modal-panel-coupon-code-0"]/header/button')
        popup.click()
    except:
        continue


    #SELECT DATES
    checkIn = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div/form/div[2]/div[1]/div[1]/div/div[1]/button')
    next = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div/form/div[2]/div[1]/div[2]/div[1]/div/div/button[2]')
    try:
        if driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div/form/div[2]/div[1]/div[2]/div[1]/div/div/ul/li[9]/div/h2[text()="April 2022"]'):
            checkInDate = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div/form/div[2]/div[1]/div[2]/div[1]/div/div/ul/li[9]/div/table/tbody/tr[4]/td[1]/button')
            checkInDate.click()
    except:
        next.click()






