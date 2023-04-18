import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class CacheForm(unittest.TestCase):
    def __init__(self, testName, driver) -> None:
        super(CacheForm, self).__init__(testName)
        self.driver = driver

    def test_cache_form(self):
        driver = self.driver
        time.sleep(2)  # necessary to wait bc of how ReactDOM loads objects

        # click button dropdown
        driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[3]/div/div/main/div[2]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div/div/div/div[2]/form/div/div/div/div/div/div[1]/div/div/div[1]/button').click()
        time.sleep(2)

        # click elasticache form button
        driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[3]/div/div/main/div[2]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div/div/div/div[2]/form/div/div/div/div/div/div[1]/div/div/div[3]/div[2]/div/div/div/ul/li[4]/ul/li[2]').click()
        time.sleep(2)

        # account dropdown
        account_dd = driver.find_element(
            By.XPATH, '//*[@id="formField:rf:"]')
        account_dd.click()
        time.sleep(5)
        account_dd.send_keys("<ACCOUNT-ID>")

        # instance type
        instance_type = driver.find_element(
            By.XPATH, '//*[@id="formField:rl:"]')
        instance_type.send_keys("cache.m5.large")

        # Shards
        shards = driver.find_element(By.XPATH, '//*[@id="formField:rr:"]')
        shards.clear()
        shards.send_keys('2')

        # replica per shard
        replica = driver.find_element(By.XPATH, '//*[@id="formField:rs:"]')
        replica.send_keys('2')
        replica.clear()
        replica.send_keys('0')

        # Cache name
        cache_name = driver.find_element(By.XPATH, '//*[@id="formField:rt:"]')
        cache_name.send_keys('cache-name')

        # Engine Type
        engine_type = driver.find_element(
            By.XPATH, '//*[@id="formField:ru:"]')
        engine_type.send_keys('Redis')

        # security Group
        sec_group = driver.find_element(By.XPATH, '//*[@id="formField:r14:"]')
        sec_group.send_keys('sg-1111111111')

        # Clustered
        clustered = driver.find_element(By.XPATH, '//*[@id="formField:r15:"]')
        clustered.send_keys('Enabled')

        # Custom Param Group
        clustered = driver.find_element(By.XPATH, '//*[@id="formField:r1b:"]')
        clustered.send_keys('Keyspace')

        # VPC ID
        vpc = driver.find_element(
            By.XPATH, '//*[@id="formField:r1h:"]')
        vpc.send_keys('Sandbox VPC')

        # subnet
        subnet = driver.find_element(By.XPATH, '//*[@id="formField:r1n:"]')
        subnet.send_keys('aws-controltower-PrivateSubnet1A')

        # Application Name
        app_name = driver.find_element(By.XPATH, '//*[@id="formField:r1t:"]')
        app_name.send_keys('Test@ppName')
        app_name.clear()
        app_name.send_keys('test-app-name')

        # Application Owner
        app_owner = driver.find_element(By.XPATH, '//*[@id="formField:r1u:"]')
        app_owner.send_keys('@pp Owner')
        app_owner.clear()
        app_owner.send_keys("Josiah Burnham")

        # Cost Center
        cost_center = driver.find_element(
            By.XPATH, '//*[@id="formField:r1v:"]')
        cost_center.send_keys('1')
        cost_center.clear()
        cost_center.send_keys('9999999999')
        cost_center.clear()
        cost_center.send_keys('2001')

        # Life Cycle
        lifecycle = driver.find_element(By.XPATH, '//*[@id="formField:r20:"]')
        lifecycle.send_keys('Dev')

        # Location
        location = driver.find_element(By.XPATH, '//*[@id="formField:r26:"]')
        location.send_keys('USEastNVirginia')

        # Increment
        increment = driver.find_element(By.XPATH, '//*[@id="formField:r2c:"]')
        increment.send_keys('2')
        increment.clear()
        increment.send_keys('999')
        increment.clear()
        increment.send_keys('02')

        driver.find_element(By.XPATH,
                            '//*[@id="root"]/div/div[3]/div/main/div[3]/div/div[3]/form/div/div/div/div[3]/div/div[1]/div/div/div/button').click()
        time.sleep(3)

        flashbar = driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[3]/div/main/div[3]/div/div[3]/form/div/div/div/div[1]/div/ul/li/div/div[1]/div/div[2]/div[2]').text
        self.assertEqual(
            'You have successfully added a ElastiCache to your cart.', flashbar)

    def tearDown(self):
        driver = self.driver
        driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[1]/div/div/header/div/div[1]/a').click()
