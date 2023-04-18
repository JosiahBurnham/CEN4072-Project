import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class ECRForm(unittest.TestCase):
    def __init__(self, testName, driver) -> None:
        super(ECRForm, self).__init__(testName)
        self.driver = driver

    def test_ecr_form(self):
        time.sleep(2)  # necessary to wait bc of how ReactDOM loads objects
        driver = self.driver

        # click button dropdown
        driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[3]/div/div/main/div[2]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div/div/div/div[2]/form/div/div/div/div/div/div[1]/div/div/div[1]/button').click()
        time.sleep(2)

        # click ECR button
        driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[3]/div/div/main/div[2]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div/div/div/div[2]/form/div/div/div/div/div/div[1]/div/div/div[3]/div[2]/div/div/div/ul/li[3]/ul/li/a').click()
        time.sleep(2)

        # account dropdown
        account_dd = driver.find_element(
            By.XPATH, '//*[@id="formField:rf:"]')
        account_dd.click()
        time.sleep(5)
        account_dd.send_keys("<ACCOUNT-ID>")

        # repo name
        repo_name = driver.find_element(
            By.XPATH, '//*[@id="formField:rl:"]')
        repo_name.send_keys('test-repo-name')
        time.sleep(2)

        # dev account
        dev_account = driver.find_element(
            By.XPATH, '//*[@id="formField:rm:"]')
        dev_account.clear()
        dev_account.send_keys('1234567891234')  # 13 chars
        time.sleep(2)
        dev_account.clear()
        dev_account.send_keys('123456789123')  # 12 chars
        time.sleep(2)

        # QA account
        qa_account = driver.find_element(
            By.XPATH, '//*[@id="formField:rn:"]')
        qa_account.clear()
        qa_account.send_keys('987654321012')  # 12 chars
        time.sleep(2)

        # staging account
        staging = driver.find_element(
            By.XPATH, '//*[@id="formField:ro:"]')
        staging.clear()
        staging.send_keys('123456789')  # 9 chars
        time.sleep(2)
        staging.clear()
        staging.send_keys('123456789123')  # 12 chars
        time.sleep(2)

        # prod account
        prod = driver.find_element(
            By.XPATH, '//*[@id="formField:rp:"]')
        prod.clear()
        prod.send_keys('000000000001')  # 12 chars
        time.sleep(2)

        # application name
        app_name = driver.find_element(
            By.XPATH, '//*[@id="formField:rq:"]')
        app_name.send_keys('pricing engine')
        time.sleep(2)

        # application owner
        app_owner = driver.find_element(
            By.XPATH, '//*[@id="formField:rr:"]')
        app_owner.send_keys('Jake#Test')
        time.sleep(2)
        app_owner.clear()
        app_owner.send_keys('Jake Test Jr.')
        time.sleep(2)

        # cost center
        cost = driver.find_element(
            By.XPATH, '//*[@id="formField:rs:"]')
        cost.send_keys('0004')
        time.sleep(2)

        # life cycle dropdown
        life_cycle = driver.find_element(
            By.XPATH, '//*[@id="formField:rt:"]')
        life_cycle.click()
        life_cycle.send_keys('Prod')
        time.sleep(2)

        # add to cart
        driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[3]/div/main/div[3]/div/div[3]/form/div/div/div/div[3]/div/div[1]/div/div/div/button').click()
        time.sleep(5)

        flashbar = driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[3]/div/main/div[3]/div/div[3]/form/div/div/div/div[1]/div/ul/li/div/div[1]/div/div[2]/div[2]').text
        self.assertEqual(
            'You have successfully added a ECR Repository to your cart.', flashbar)

    def tearDown(self):
        driver = self.driver
        # go back to splash page for next unit test
        driver.find_element(
            By.XPATH, '//*[@id="top-nav"]/div/div/header/div/div[1]/a').click()
