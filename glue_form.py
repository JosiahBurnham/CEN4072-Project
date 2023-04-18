import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class GlueForm(unittest.TestCase):
    def __init__(self, testName, driver) -> None:
        super(GlueForm, self).__init__(testName)
        self.driver = driver

    def test_glue_form(self):
        driver = self.driver
        time.sleep(2)  # necessary to wait bc of how ReactDOM loads objects

        # click button dropdown
        driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[3]/div/div/main/div[2]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div/div/div/div[2]/form/div/div/div/div/div/div[1]/div/div/div[1]/button').click()
        time.sleep(2)

        # click glue form button
        driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[3]/div/div/main/div[2]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div/div/div/div[2]/form/div/div/div/div/div/div[1]/div/div/div[3]/div[2]/div/div/div/ul/li[4]/ul/li[3]').click()
        time.sleep(3)

        # account dropdown
        account_dd = driver.find_element(
            By.XPATH, '//*[@id="formField:rf:"]')
        account_dd.click()
        time.sleep(5)
        account_dd.send_keys("#<ACCOUNT-ID>")

        # Database Name
        db_name = driver.find_element(
            By.XPATH, '//*[@id="formField:rl:"]')
        db_name.send_keys("DatabaseName")
        db_name.clear()
        db_name.send_keys('database-name')
        db_name.clear()
        db_name.send_keys('database')

        # Shards
        desc = driver.find_element(By.XPATH, '//*[@id="formField:rm:"]')
        desc.send_keys('description')

        driver.find_element(By.XPATH,
                            '//*[@id="root"]/div/div[3]/div/main/div[3]/div/div[3]/form/div/div/div/div[3]/div/div[1]/div/div/div/button').click()
        time.sleep(3)

        flashbar = driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[3]/div/main/div[3]/div/div[3]/form/div/div/div/div[1]/div/ul/li/div/div[1]/div/div[2]/div[2]').text
        self.assertEqual(
            'You have successfully added a Glue Database to your cart.', flashbar)

    def tearDown(self):
        driver = self.driver
        driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[1]/div/div/header/div/div[1]/a').click()
