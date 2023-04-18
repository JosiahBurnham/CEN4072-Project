import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class RDSForm(unittest.TestCase):
    def __init__(self, testName, driver) -> None:
        super(RDSForm, self).__init__(testName)
        self.driver = driver

    def test_rds_form(self):
        time.sleep(2)  # necessary to wait bc of how ReactDOM loads objects
        driver = self.driver

        # click button dropdown
        driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[3]/div/div/main/div[2]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div/div/div/div[2]/form/div/div/div/div/div/div[1]/div/div/div[1]/button').click()
        time.sleep(2)

        # click RDS button
        driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[3]/div/div/main/div[2]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div/div/div/div[2]/form/div/div/div/div/div/div[1]/div/div/div[3]/div[2]/div/div/div/ul/li[4]/ul/li[4]/a').click()
        time.sleep(2)

        # --------------------------

        # account dropdown
        account_dd = driver.find_element(
            By.XPATH, '//*[@id="formField:rf:"]')
        account_dd.click()
        time.sleep(5)
        account_dd.send_keys("#<ACCOUNT-ID>")

        # storage
        storage = driver.find_element(
            By.XPATH, '//*[@id="formField:rl:"]')
        storage.clear()
        storage.send_keys('505')
        time.sleep(1)
        storage.clear()
        storage.send_keys('4')
        time.sleep(1)
        storage.clear()
        storage.send_keys('76')

        # db instance_class
        instance_class = driver.find_element(
            By.XPATH, '//*[@id="formField:rm:"]')
        instance_class.send_keys('db.t2.large')

        # db instance_ID
        instance_ID = driver.find_element(
            By.XPATH, '//*[@id="formField:rs:"]')
        instance_ID.send_keys('my id 5')
        time.sleep(1)
        instance_ID.clear()
        instance_ID.send_keys('id#0003')
        time.sleep(1)
        instance_ID.clear()
        instance_ID.send_keys('idfifteen')

        # db engine
        engine = driver.find_element(
            By.XPATH, '//*[@id="formField:rt:"]')
        engine.send_keys('MySQL')

        # storage_type
        storage_type = driver.find_element(
            By.XPATH, '//*[@id="formField:r13:"]')
        storage_type.send_keys('GP2')

        # vpc id
        vpc = driver.find_element(
            By.XPATH, '//*[@id="formField:r19:"]')
        vpc.send_keys('Sandbox VPC')

        # subnet
        subnet = driver.find_element(
            By.XPATH, '//*[@id="formField:r1f:"]')
        subnet.send_keys('aws-controltower-PrivateSubnet1A')

        # ref sec group
        sec = driver.find_element(
            By.XPATH, '//*[@id="formField:r1l:"]')
        sec.send_keys('sg-111111111111')
        sec.clear()

        # application name
        app_name = driver.find_element(
            By.XPATH, '//*[@id="formField:r1m:"]')
        app_name.send_keys('pricing@engine')
        app_name.clear()
        app_name.send_keys('application engine')

        # application owner
        app_owner = driver.find_element(
            By.XPATH, '//*[@id="formField:r1n:"]')
        app_owner.send_keys('Jake-Test-50')
        time.sleep(1)
        app_owner.clear()
        app_owner.send_keys('JakeTest')

        # cost center
        cost = driver.find_element(
            By.XPATH, '//*[@id="formField:r1o:"]')
        cost.send_keys('0.04')
        time.sleep(1)
        cost.clear()
        cost.send_keys('1224')

        # life cycle dropdown
        life_cycle = driver.find_element(
            By.XPATH, '//*[@id="formField:r1p:"]')
        life_cycle.click()
        life_cycle.send_keys('Dev')

        # location
        location = driver.find_element(
            By.XPATH, '//*[@id="formField:r1v:"]')
        location.send_keys('USEastNVirginia')

        # increment
        increment = driver.find_element(
            By.XPATH, '//*[@id="formField:r25:"]')
        increment.send_keys('00')
        increment.clear()
        increment.send_keys('99')

        # add to cart
        driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[3]/div/main/div[3]/div/div[3]/form/div/div/div/div[3]/div/div[1]/div/div/div/button').click()
        time.sleep(5)

        flashbar = driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[3]/div/main/div[3]/div/div[3]/form/div/div/div/div[1]/div/ul/li/div/div[1]/div/div[2]/div[2]').text
        print(flashbar)
        self.assertEqual(
            'You have successfully added a RDS Instance to your cart.', flashbar)

    def tearDown(self):
        driver = self.driver
        # go back to splash page for next unit test
        driver.find_element(
            By.XPATH, '//*[@id="top-nav"]/div/div/header/div/div[1]/a').click()
