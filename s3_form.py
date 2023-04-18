import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class S3Form(unittest.TestCase):
    def __init__(self, testName, driver) -> None:
        super(S3Form, self).__init__(testName)
        self.driver = driver

    def test_s3_form(self):
        driver = self.driver
        time.sleep(2)  # necessary to wait bc of how ReactDOM loads objects

        # click button dropdown
        driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[3]/div/div/main/div[2]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div/div/div/div[2]/form/div/div/div/div/div/div[1]/div/div/div[1]/button').click()
        time.sleep(2)

        # click s3 form button
        driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[3]/div/div/main/div[2]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div/div/div/div[2]/form/div/div/div/div/div/div[1]/div/div/div[3]/div[2]/div/div/div/ul/li[5]/ul/li').click()
        time.sleep(2)

        # function
        s3_function = driver.find_element(By.XPATH, '//*[@id="formField:rf:"]')

        s3_function.send_keys('Test-Bucket')
        s3_function.clear()
        s3_function.send_keys('test-bucket')

        # account dropdown
        account_dd = driver.find_element(
            By.XPATH, '//*[@id="formField:rg:"]')
        account_dd.click()
        time.sleep(5)
        account_dd.send_keys("#<ACCOUNT-ID>")

        # versioning
        versioning = driver.find_element(
            By.XPATH, '//*[@id="formField:rm:"]')
        versioning.send_keys("Enabled")

        # IAM Role Name
        role_name = driver.find_element(By.XPATH, '//*[@id="formField:rs:"]')
        role_name.send_keys('bucket-role-name')
        role_name.clear()

        # Application Name
        app_name = driver.find_element(By.XPATH, '//*[@id="formField:rt:"]')
        app_name.send_keys('Test@ppName')
        app_name.clear()
        app_name.send_keys('test-app-name')

        # Application Owner
        app_owner = driver.find_element(By.XPATH, '//*[@id="formField:ru:"]')
        app_owner.send_keys('@pp Owner')
        app_owner.clear()
        app_owner.send_keys("Josiah Burnham")

        # Cost Center
        cost_center = driver.find_element(
            By.XPATH, '//*[@id="formField:rv:"]')
        cost_center.send_keys('1')
        cost_center.clear()
        cost_center.send_keys('9999999999')
        cost_center.clear()
        cost_center.send_keys('2001')

        # Life Cycle
        lifecycle = driver.find_element(By.XPATH, '//*[@id="formField:r10:"]')
        lifecycle.send_keys('Dev')

        # Location
        location = driver.find_element(By.XPATH, '//*[@id="formField:r16:"]')
        location.send_keys('USEastNVirginia')

        # Increment
        increment = driver.find_element(By.XPATH, '//*[@id="formField:r1c:"]')
        increment.send_keys('2')
        increment.clear()
        increment.send_keys('999')
        increment.clear()
        increment.send_keys('02')

        driver.find_element(By.XPATH,
                            '//*[@id="root"]/div/div[3]/div/main/div[3]/div/div[3]/div/div/form/div/div/div/div[3]/div/div[1]/div/div/div/button').click()
        time.sleep(3)

        flashbar = driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[3]/div/main/div[3]/div/div[3]/div/div/form/div/div/div/div[1]/div/ul/li/div/div[1]/div/div[2]/div[2]').text
        self.assertEqual(
            'You have successfully added a S3 Bucket to your cart.', flashbar)

    def tearDown(self):
        driver = self.driver
        driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[1]/div/div/header/div/div[1]/a').click()
