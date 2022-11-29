import pytest
from selenium import webdriver
from Library.config import Config

@pytest.fixture(params=["Chrome"])
def _driver(request):
    if request.param == "Chrome":
        driver = webdriver.Chrome(executable_path=Config.Chrome_Driver)

    elif request.param == "Edge" :
        driver = webdriver.Edge(executable_path=Config.Edge_Driver)



    driver.get(Config.url)
    driver.maximize_window()
    driver.implicitly_wait(50)
    yield driver
    driver.save_screenshot("test_redbus.png")
    print(driver.title)
    driver.close()