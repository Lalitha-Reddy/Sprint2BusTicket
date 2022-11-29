from selenium import webdriver
# from Data.reading_objects import ReadExcel
from Library.config import Config
from Data import reading_objects
import time
import re

# read_xl = ReadExcel()
var = reading_objects.read_locators()

class RedBus:
    def __init__(self, driver):
        self.driver = driver

    def bus_tickets(self):
        self.driver.find_element(*var['red_bus_']).click()

    def from_destination(self):
        self.driver.find_element(*var['from_dst']).click()

    def enter_from_destination(self):

        self.driver.find_element(*var['enter_from_dst']).send_keys("Secunderabad, Hyderabad")
        # assert re.findall('[a-zA-Z]', fd_place)
        time.sleep(10)
        # self.driver.implicitly_wait(10)
        # self.driver.find_element(*var['select_from_dst']).click()

    def select_from_destination(self):
        self.driver.find_element(*var['select_from_dst']).click()

    def to_destination(self):
        self.driver.find_element(*var['to_dst']).click()

    def enter_to_destination(self):
        self.driver.find_element(*var['enter_to_dst']).send_keys("Majestic, Bangalore")
        # assert re.findall("[a-zA-Z]", to_place)


    def select_to_destination(self):
        self.driver.find_element(*var['select_to_dst']).click()

    def onward_date(self):
        self.driver.find_element(*var['onward_date_']).click()

    def enter_onward_date(self):
        self.driver.find_element(*var['enter_onward_date_']).click()

    def search_buses_btn(self):
        self.driver.find_element(*var['search_buses_']).click()

    def modify_btn(self):
        self.driver.find_element(*var['modify_btn_']).click()
        # time.sleep(5)

    # def modify_from_destination(self,md_fd_place):
    #     time.sleep(5)
    #     self.driver.find_element(*var['modify_from_dstnation']).click()
    #     self.driver.find_element(*var['modify_from_destination']).send_keys(md_fd_place)
    #     # assert re.findall('\w', md_fd_place)
    #
    # def modify_to_destination(self,md_to_place):
    #     time.sleep(5)
    #     self.driver.find_element(*var['modify_to_dst456']).click()
    #     self.driver.find_element(*var['modify_to_dst123']).send_keys(md_to_place)
    #     assert re.findall('\\w', md_to_place)

    def modify_search_btn(self):
        time.sleep(5)
        self.driver.find_element(*var['modify_search_btn_']).click()
        time.sleep(10)

    def ok_got_it_btn(self):
        time.sleep(5)
        self.driver.find_element(*var['ok_got_button']).click()

    def primo_buses(self):
        # time.sleep(5)
        self.driver.find_element('xpath','//li[@class="clearfix"]/span[contains(text(),"Primo Bus")]').click()
        time.sleep(5)

    # def departure_time(self):
    #     # time.sleep(5)
    #     self.driver.find_element('xpath', '(//label[@title="After 6 pm"])[1]').click()
    # #
    # def bus_types(self):
    #     self.driver.find_element('xpath', '//label[text()="SLEEPER"]').click()
    #
    # def arrival_time(self):
    #     self.driver.find_element('xpath', '(//label[@title="After 6 pm"])[2]').click()

    def view_seats_btn(self):
        self.driver.find_element(*var['click_on_view_seats']).click()
        time.sleep(15)

    # def hide_seats(self):
    #     self.driver.find_element('xpath', '//div[@class="button hide-seats fr"]').click()

    def boarding_point(self):
        self.driver.find_element(*var['boarding_point_']).click()
        time.sleep(5)

    def dropping_point(self):
        self.driver.find_element(*var['dropping_point_']).click()
        time.sleep(5)

    def fare_details(self):
        self.driver.find_element(*var['fare_details_']).click()
        time.sleep(3)

    def change_btn(self):
        self.driver.find_element(*var['change_btn_']).click()
        time.sleep(3)

    def change_boarding_point(self):
        self.driver.find_element(*var['change_boarding_point_']).click()
        time.sleep(3)

    def continue_btn(self):
        self.driver.find_element(*var['continue_btn_']).click()
        time.sleep(4)

    def proceed_to_book(self):
        self.driver.find_element(*var['proceed_to_book_']).click()
        time.sleep(4)

    def enter_name(self):
        self.driver.find_element(*var['name_']).send_keys("Lalitha")
        # assert re.findall('\\w', name)
        # assert re.findall('\D', name)
        time.sleep(5)

    def select_female_radio_btn(self):
        self.driver.find_element(*var['female_radio_btn_']).click()
        time.sleep(4)

    def enter_age(self):
        self.driver.find_element(*var['age_']).click()
        self.driver.find_element(*var['age_']).send_keys("21")
        # assert re.findall('^\d{2}$', age)
        time.sleep(3)

    def enter_email(self):
        time.sleep(2)
        # self.driver.find_element(*var['email_id']).click()
        self.driver.find_element(*var['email_id']).send_keys("vvlr0227@gmail.com")
        # assert re.findall('\W', email)
        time.sleep(3)

    def enter_phone_no(self):
        # if isinstance(phone,float):
        #     phone = str(int(phone))
        # assert len(phone) == 10
        self.driver.find_element(*var['Phone_']).send_keys("7036282524")
        # assert re.findall('^\d{10}$', phone)
        time.sleep(3)

    def insurance_checkbox(self):
        self.driver.find_element(*var['insurance_checkbox_']).click()
        time.sleep(2)

    def donate_covid_checkbox(self):
        self.driver.find_element(*var['donate_covid_checkbox_']).click()
        time.sleep(3)

    def proceed_to_pay(self):
        self.driver.find_element(*var['proceed_to_pay_']).click()
        time.sleep(4)

    def select_payment_method(self):
        self.driver.find_element(*var['payment_method_']).click()
        time.sleep(3)

    def enter_upi_id(self):
        self.driver.find_element(*var['upi_id_']).send_keys("lalithavennapusa21@ybl")
        # assert re.findall('\\W', upi_id)
        time.sleep(5)

    def verify_btn(self):
        self.driver.find_element(*var['verify_btn_']).click()
        # time.sleep(7)

    def pay_now_btn(self):
        time.sleep(3)
        self.driver.find_element(*var['pay_now_btn_']).click()