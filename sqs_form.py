import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class SQSForm(unittest.TestCase):
    def __init__(self, testName, driver) -> None:
        super(SQSForm, self).__init__(testName)
        self.driver = driver

    def test_sqs_form(self):
        time.sleep(2)  # necessary to wait bc of how ReactDOM loads objects
        driver = self.driver

        # click button dropdown
        driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[3]/div/div/main/div[2]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div/div/div/div[2]/form/div/div/div/div/div/div[1]/div/div/div[1]/button').click()
        time.sleep(2)

        # click SQS button
        driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[3]/div/div/main/div[2]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div/div/div/div[2]/form/div/div/div/div/div/div[1]/div/div/div[3]/div[2]/div/div/div/ul/li[1]/ul/li/a').click()
        time.sleep(2)

        # --------------------------

        # account dropdown
        account_dd = driver.find_element(
            By.XPATH, '//*[@id="formField:rf:"]')
        account_dd.click()
        time.sleep(5)
        account_dd.send_keys("<ACCOUNT-ID>")

        # queue
        queue = driver.find_element(
            By.XPATH, '//*[@id="formField:rl:"]')
        queue.send_keys('test_queue_name.fifo')

        # fifo
        fifo = driver.find_element(
            By.XPATH, '//*[@id=":rp:"]')  # false
        fifo.click()

        # delay
        delay = driver.find_element(
            By.XPATH, '//*[@id="formField:rq:"]')
        delay.clear()
        delay.send_keys('012')
        time.sleep(1)
        delay.clear()
        delay.send_keys('899')

        # receive message wait time
        message = driver.find_element(
            By.XPATH, '//*[@id="formField:rr:"]')
        message.clear()
        message.send_keys('22')
        time.sleep(1)
        message.clear()
        message.send_keys('0.925')

        # visibility timeout
        timeout = driver.find_element(
            By.XPATH, '//*[@id="formField:rs:"]')
        timeout.clear()
        timeout.send_keys('300000')
        time.sleep(1)
        timeout.clear()
        timeout.send_keys('2000')

        # message retention
        retention = driver.find_element(
            By.XPATH, '//*[@id="formField:rt:"]')
        retention.clear()
        retention.send_keys('9233')

        # application name
        app_name = driver.find_element(
            By.XPATH, '//*[@id="formField:rv:"]')
        app_name.send_keys('SQS Queue')

        # application owner
        app_owner = driver.find_element(
            By.XPATH, '//*[@id="formField:r10:"]')
        app_owner.send_keys('!@#$Test')
        time.sleep(1)
        app_owner.clear()
        app_owner.send_keys('Dr. Bartholemu Jr.')

        # cost center
        cost = driver.find_element(
            By.XPATH, '//*[@id="formField:r11:"]')
        cost.send_keys('9009')

        # life cycle dropdown
        life_cycle = driver.find_element(
            By.XPATH, '//*[@id="formField:r12:"]')
        life_cycle.click()
        life_cycle.send_keys('Stage')

        # add to cart
        driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[3]/div/main/div[3]/div/div[3]/form/div/div/div/div[2]/div/div[1]/div/div/div/button').click()
        time.sleep(5)

        flashbar = driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[3]/div/main/div[3]/div/div[3]/div/ul/li/div/div[1]/div/div[2]/div[2]').text
        self.assertEqual(
            'You have successfully added a SQS Queue to your cart.', flashbar)

    def tearDown(self):
        driver = self.driver
        # go back to splash page for next unit test
        driver.find_element(
            By.XPATH, '//*[@id="top-nav"]/div/div/header/div/div[1]/a').click()
