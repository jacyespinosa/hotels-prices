from selenium import webdriver
import time

EMAIL = "ENTER EMAIL"
PASSWORD = "ENTER PASSWORD"


chrome_driver_path = "ENTER PATH"
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(chrome_options=options, executable_path=chrome_driver_path)


driver.get("https://www.hotels.com/profile/signin.html?target=H4sIAAAAAAAAAAXB0QkAIAgFwI30v3XCUtCMfOD63SlwazB3N2lCvGhm8H25zIVLADu7SBH-Afk_Wf4sAAAA")



def login():
    email = driver.find_element_by_xpath('//*[@id="sign-in-email"]')
    password = driver.find_element_by_xpath('//*[@id="sign-in-password"]')
    #Enter Email
    email.send_keys(EMAIL)
    time.sleep(0.1)
    password.send_keys(PASSWORD)

    submit = driver.find_element_by_xpath('//*[@id="sign-in-button"]')
    submit.click()


time.sleep(0.1)
login()

