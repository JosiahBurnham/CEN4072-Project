import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class DynamoForm(unittest.TestCase):
    def __init__(self, testName, driver) -> None:
        super(DynamoForm, self).__init__(testName)
        self.driver = driver

    def test_dynamo_form(self):
        time.sleep(2)  # necessary to wait bc of how ReactDOM loads objects
        driver = self.driver

        # click button dropdown
        driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[3]/div/div/main/div[2]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div/div/div/div[2]/form/div/div/div/div/div/div[1]/div/div/div[1]/button').click()
        time.sleep(2)

        # click RDS button
        driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[3]/div/div/main/div[2]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div/div/div/div[2]/form/div/div/div/div/div/div[1]/div/div/div[3]/div[2]/div/div/div/ul/li[4]/ul/li[1]/a').click()
        time.sleep(2)

        # --------------------------

        # account dropdown
        account_dd = driver.find_element(
            By.XPATH, '//*[@id="formField:rf:"]')
        account_dd.click()
        time.sleep(5)
        account_dd.send_keys("<ACCOUNT-ID>")

        # table
        table = driver.find_element(
            By.XPATH, '//*[@id="formField:rl:"]')
        table.clear()
        table.send_keys('Table_Name-80085!')
        time.sleep(1)
        table.clear()
        table.send_keys('Table Name Main')
        time.sleep(1)
        table.clear()
        table.send_keys('Table.Main.Users')

        # hash_key
        hash_key = driver.find_element(
            By.XPATH, '//*[@id="formField:rm:"]')
        hash_key.send_keys('my key (5)')
        time.sleep(1)
        hash_key.clear()
        hash_key.send_keys('id#0003')
        time.sleep(1)
        hash_key.clear()
        hash_key.send_keys('key-user_me')

        # hash_key_type
        hash_key_type = driver.find_element(
            By.XPATH, '//*[@id="formField:rn:"]')

       # range_key
        range_key = driver.find_element(
            By.XPATH, '//*[@id="formField:rt:"]')
        range_key.send_keys('00101')

        # range_key_type
        range_key_type = driver.find_element(
            By.XPATH, '//*[@id="formField:ru:"]')
        range_key_type.send_keys('Binary')

        # ttl
        ttl = driver.find_element(
            By.XPATH, '//*[@id=":r16:"]')
        ttl.click()

        # application name
        app_name = driver.find_element(
            By.XPATH, '//*[@id="formField:r18:"]')
        app_name.send_keys('#hashtag AppName')
        app_name.clear()
        app_name.send_keys('the name of the application')

        # application owner
        app_owner = driver.find_element(
            By.XPATH, '//*[@id="formField:r19:"]')
        app_owner.send_keys('!Jake Test42')
        time.sleep(1)
        app_owner.clear()
        app_owner.send_keys('Mr. Testing')

        # cost center
        cost = driver.find_element(
            By.XPATH, '//*[@id="formField:r1a:"]')
        cost.send_keys('00005')
        time.sleep(1)
        cost.clear()
        cost.send_keys('9999')

        # life cycle dropdown
        life_cycle = driver.find_element(
            By.XPATH, '//*[@id="formField:r1b:"]')
        life_cycle.click()
        life_cycle.send_keys('UAT')

        time.sleep(5)
        # add to cart
        driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[3]/div/main/div[3]/div/div[3]/form/div/div/div/div[3]/div/div[1]/div/div/div/button').click()
        time.sleep(5)

        flashbar = driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[3]/div/main/div[3]/div/div[3]/form/div/div/div/div[1]/div/ul/li/div/div[1]/div/div[2]/div[2]').text
        self.assertEqual(
            'You have successfully added a DynamoDB Table to your cart.', flashbar)

    def tearDown(self):
        driver = self.driver
        # go back to splash page for next unit test
        driver.find_element(
            By.XPATH, '//*[@id="top-nav"]/div/div/header/div/div[1]/a').click()
