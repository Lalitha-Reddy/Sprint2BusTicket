import time
from Library.config import Config
from POM.Red_bus import RedBus
from Data import reading_objects
import pytest

class TestRedBus:
    # read_xl = ReadExcel()
    # details = read_xl.read_test_data(Config.BUSTICKET_DATA)
    # @pytest.mark.parametrize('fd_place,to_place,name,age,email,phone,upi_id', details)
    # def test_bus(self, fd_place, to_place,name, age, email, phone, upi_id, _driver):
    def test_bus(self, _driver):
        _driver.implicitly_wait(30)
        bs = RedBus(_driver)
        bs.bus_tickets()
        bs.from_destination()
        bs.enter_from_destination()
        bs.select_from_destination()
        bs.to_destination()
        bs.enter_to_destination()
        bs.select_to_destination()
        bs.onward_date()
        bs.enter_onward_date()
        bs.search_buses_btn()
        bs.modify_btn()
        # bs.modify_from_destination()
        # bs.modify_to_destination()
        bs.modify_search_btn()
        bs.ok_got_it_btn()
        # bs.primo_buses()
        # bs.departure_time()
        # bs.bus_types()
        # bs.arrival_time()
        bs.view_seats_btn()
        bs.boarding_point()
        bs.dropping_point()
        bs.fare_details()
        bs.change_btn()
        bs.change_boarding_point()
        bs.continue_btn()
        bs.proceed_to_book()
        bs.enter_name()
        bs.select_female_radio_btn()
        bs.enter_age()
        bs.enter_email()
        bs.enter_phone_no()
        bs.insurance_checkbox()
        bs.donate_covid_checkbox()
        bs.proceed_to_pay()
        bs.select_payment_method()
        bs.enter_upi_id()
        bs.verify_btn()
        bs.pay_now_btn()











































































##############################################################################
# from POM.Red_bus import RedBus
#
# class Test_Bus:
#     def test_busticket(self, _driver):
#         try:
#             bs = RedBus(_driver)
#             bs.bus_tickets()
#             bs.from_destination()
#             bs.enter_from_destination()
#             bs.select_from_destination()
#             bs.to_destination()
#             bs.enter_to_destination()
#             bs.select_to_destination()
#             bs.onward_date()
#             bs.enter_onward_date()
#             bs.search_buses_btn()
#             bs.modify_btn()
#             bs.modify_from_destination()
#             bs.modify_to_destination()
#             bs.modify_search_btn()
#             # bs.ok_got_it_btn()
#             # bs.primo_buses()
#             # bs.departure_time()
#             # bs.bus_types()
#             # bs.arrival_time()
#             bs.view_seats_btn()
#             # bs.hide_seats()
#             bs.boarding_point()
#             bs.dropping_point()
#             bs.fare_details()
#             bs.change_btn()
#             bs.change_boarding_point()
#             bs.continue_btn()
#             bs.proceed_to_book()
#             bs.enter_name()
#             bs.select_male_radio_btn()
#             bs.enter_age()
#             bs.enter_email()
#             bs.enter_phone_no()
#             bs.insurance_checkbox()
#             bs.donate_covid_checkbox()
#             bs.proceed_to_pay()
#             bs.select_payment_method()
#             bs.enter_upi_id()
#             bs.verify_btn()
#             bs.pay_now_btn()
#         except:
#             pass










#########################################################3