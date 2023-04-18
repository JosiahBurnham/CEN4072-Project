import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class EC2Form(unittest.TestCase):
    def __init__(self, testName, driver) -> None:
        super(EC2Form, self).__init__(testName)
        self.driver = driver

    def test_ec2_form(self):
        driver = self.driver
        time.sleep(2)  # necessary to wait bc of how ReactDOM loads objects

        # click button dropdown
        driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[3]/div/div/main/div[2]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div/div/div/div[2]/form/div/div/div/div/div/div[1]/div/div/div[1]/button').click()
        time.sleep(2)

        # click EC2 form button
        driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[3]/div/div/main/div[2]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div/div/div/div[2]/form/div/div/div/div/div/div[1]/div/div/div[3]/div[2]/div/div/div/ul/li[2]/ul/li[1]').click()
        time.sleep(2)

        # function
        ec2_function = driver.find_element(
            By.XPATH, '//*[@id="formField:rf:"]')

        ec2_function.send_keys('test-instance')

        # account dropdown
        account_dd = driver.find_element(
            By.XPATH, '//*[@id="formField:rg:"]')
        account_dd.click()
        time.sleep(5)
        account_dd.send_keys("<ACCOUNT-ID>")

        # key pair
        key_pair = driver.find_element(
            By.XPATH, '//*[@id="formField:rm:"]')
        key_pair.send_keys("key-pair-name")

        # instance type
        instance_type = driver.find_element(
            By.XPATH, '//*[@id="formField:rn:"]')
        instance_type.send_keys('t2.micro')

        # Iam Role Profile
        iamrole = driver.find_element(By.XPATH, '//*[@id="formField:rt:"]')
        iamrole.send_keys('Iam Role Name')
        iamrole.clear()
        iamrole.send_keys('iam-role-name')

        # OS Distribution
        os_dist = driver.find_element(By.XPATH, '//*[@id="formField:ru:"]')
        os_dist.send_keys('RHEL 8')

        # VPC ID
        vpc = driver.find_element(
            By.XPATH, '//*[@id="formField:r14:"]')
        vpc.send_keys('Sandbox VPC')

        # subnet
        subnet = driver.find_element(By.XPATH, '//*[@id="formField:r1a:"]')
        subnet.send_keys('aws-controltower-PrivateSubnet1A')

        # security grouop
        sec_group = driver.find_element(By.XPATH, '//*[@id="formField:r1g:"]')
        sec_group.send_keys('sg-111111111111')
        sec_group.clear()

        # sg ingress
        ingress = driver.find_element(By.XPATH, '//*[@id="formField:r1h:"]')
        ingress.send_keys('0.0')
        ingress.clear()
        ingress.send_keys('0.0.0.0/0')
        ingress.clear

        # volume size
        vol_size = driver.find_element(By.XPATH, '//*[@id="formField:r1j:"]')
        vol_size.send_keys('1000')
        vol_size.clear()
        vol_size.send_keys('45')

        # volume name
        vol_name = driver.find_element(By.XPATH, '//*[@id="formField:r1k:"]')
        vol_name.send_keys('vol name')

        # swap size
        swap_size = driver.find_element(By.XPATH, '//*[@id="formField:r1l:"]')
        swap_size.send_keys('1500')
        swap_size.clear()
        swap_size.send_keys('45')

        # Location
        location = driver.find_element(By.XPATH, '//*[@id="formField:r1m:"]')
        location.send_keys('USEastNVirginia')

        # Life Cycle
        lifecycle = driver.find_element(By.XPATH, '//*[@id="formField:r1s:"]')
        lifecycle.send_keys('Dev')

        # Sec Posture
        sec_posture = driver.find_element(
            By.XPATH, '//*[@id="formField:r22:"]')
        sec_posture.send_keys('PCI')

        # Application Name
        app_name = driver.find_element(By.XPATH, '//*[@id="formField:r28:"]')
        app_name.send_keys('Test@ppName')
        app_name.clear()
        app_name.send_keys('test-app-name')

        # Application Owner
        app_owner = driver.find_element(By.XPATH, '//*[@id="formField:r29:"]')
        app_owner.send_keys('@pp Owner')
        app_owner.clear()
        app_owner.send_keys("Josiah Burnham")

        # Cost Center
        cost_center = driver.find_element(
            By.XPATH, '//*[@id="formField:r2a:"]')
        cost_center.send_keys('1')
        cost_center.clear()
        cost_center.send_keys('9999999999')
        cost_center.clear()
        cost_center.send_keys('2001')

        # Increment
        increment = driver.find_element(By.XPATH, '//*[@id="formField:r2b:"]')
        increment.send_keys('2')
        increment.clear()
        increment.send_keys('999')
        increment.clear()
        increment.send_keys('02')

        # OS Type
        os_type = driver.find_element(
            By.XPATH, '//*[@id="formField:r2c:"]')
        os_type.send_keys('Linux')

        driver.find_element(By.XPATH,
                            '//*[@id="root"]/div/div[3]/div/main/div[3]/div/div[3]/form/div/div/div/div[3]/div/div[1]/div/div/div/button').click()
        time.sleep(3)

        flashbar = driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[3]/div/main/div[3]/div/div[3]/form/div/div/div/div[1]/div/ul/li/div/div[1]/div/div[2]/div[2]').text
        self.assertEqual(
            'You have successfully added a EC2 Instance to your cart.', flashbar)

    def tearDown(self):
        driver = self.driver
        driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[1]/div/div/header/div/div[1]/a').click()
