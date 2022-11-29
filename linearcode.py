from selenium import webdriver
import time

path = r'C:\Users\Lalitha\OneDrive\Desktop\Py_Sel driver\chromedriver.exe'
# path = r"C:\Users\Lalitha\OneDrive\Desktop\Py_Sel driver\edgedriver_win64\msedgedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.implicitly_wait(30)
url='https://www.redbus.in/'
driver.get(url)
driver.maximize_window()
# clicking on booking bus icon
driver.find_element('id','redBus').click()
# FROM
driver.find_element('xpath', '//input[@placeholder="FROM"]').click()
driver.find_element('xpath', '//input[@placeholder="FROM"]').send_keys('Hyderabad')
driver.implicitly_wait(10)
driver.find_element('xpath', "//div[text()='Secunderabad, Hyderabad']").click()
# TO
driver.find_element('xpath', '//input[@placeholder="TO"]').click()
driver.find_element('xpath', '//input[@placeholder="TO"]').send_keys('Bangalore')
driver.implicitly_wait(10)
driver.find_element('xpath', '//div[text()="Majestic, Bangalore"]').click()
# ONBOARDING DATE
driver.find_element('xpath', '//input[@placeholder="ONWARD DATE"]').click()
driver.find_element('xpath', '//*[@id="rb-calmiddle"]/ul[2]/li[31]/span').click()
# SEARCHING BUS
driver.find_element('xpath', '//button[@class="D120_search_btn searchBuses"]').click()
driver.find_element('xpath', '//div[text()="Modify"]').click()
#### selecting a bus
time.sleep(5)
driver.find_element('xpath', '//span[text()="Ok, got it"]').click()
time.sleep(5)
driver.find_element('xpath', '//*[@id="10634205"]/div/div[2]/div[1]').click()
# driver.find_element('xpath','(//div[text()="View Seats"])[1]').click()
time.sleep(2)
time.sleep(15)
driver.find_element('xpath', '//span[@title="LB Nagar"]/../..//div[@class="radio-unchecked"]').click()
time.sleep(2)
driver.find_element('xpath', '//span[text()="Indiranagar"]/../..//div[@class="radio-css "]').click()
time.sleep(2)
# #### changing the boarding point and dropping point

driver.find_element('xpath', '//span[@class="fr bpdp-change"]').click()
time.sleep(2)
driver.find_element('xpath', '//span[@title="Secunderabad"]/../..//div[@class="radio-unchecked"]').click()
time.sleep(2)
driver.find_element('xpath', '//button[@class="button continue inactive text-trans-uc w-h-cont"]').click()
time.sleep(2)
# ### proceed to book
#
driver.find_element('xpath', '//button[text()="Proceed to book"]').click()

# #### passenger details
#
driver.find_element('xpath', '//input[@placeholder="Name"]').send_keys('Lalitha')
time.sleep(2)
driver.find_element('xpath', '//div[@id="div_23_0"]').click()
time.sleep(2)
driver.find_element('xpath', '//input[@placeholder="Age"]').send_keys('21')
time.sleep(2)
driver.find_element('xpath', '//input[@placeholder="Email ID"]').send_keys('vvlr0227@gmail.com')
time.sleep(2)
driver.find_element('xpath', '//label[@class="custinfo_label"]//input[@id="seatno-06"]').send_keys('7036282524')
time.sleep(2)
driver.find_element('xpath', '//span[@class="checkmark-radio"]').click()
time.sleep(2)
driver.find_element('xpath', '//label[@id="addOnFeatureCheckBox"]').click()
time.sleep(2)
driver.find_element('xpath', '//input[@class="button main-btn gtm-continueBooking"]').click()
time.sleep(5)
# payment method
driver.find_element('xpath', '//div[@id="Pay through UPI ID"]').click()
time.sleep(5)
driver.find_element('xpath', '//input[@placeholder="Enter UPI ID"]').send_keys('lalithavennapusa65@ybl')
time.sleep(3)
driver.find_element('xpath', '//div[text()="VERIFY"]').click()
time.sleep(5)
driver.find_element('xpath', '//div[text()="Pay Now"]').click()
