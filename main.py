
import time
import pyotp
import unittest
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By

from s3_form import S3Form
from ec2_form import EC2Form
from elasticache_form import CacheForm
from glue_form import GlueForm
from ecr_repo_form import ECRForm
from dynamodb_form import DynamoForm
from sqs_form import SQSForm
from rds_form import RDSForm


def log_in():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://self-service.hertz.io')

    # Log-in
    driver.find_element(
        By.XPATH, '//*[@id="formField:r0:"]').send_keys('<USERNAME>')
    driver.find_element(
        By.XPATH, '//*[@id="formField:r1:"]').send_keys('<PASSWORD>')
    driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[3]/div/form/div/div[2]/div/div/div/div/button').click()
    time.sleep(3)
    # enter MFA
    totp = pyotp.TOTP('MFA-SECRET')
    driver.find_element(
        By.XPATH, '//*[@id="formField:r6:"]').send_keys(totp.now())
    driver.find_element(
        By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[3]/div/div/div/button').click()
    return driver


def suite():
    driver = log_in()
    suite = unittest.TestSuite()
    suite.addTest(ECRForm('test_ecr_form', driver))
    suite.addTest(DynamoForm('test_dynamo_form', driver))
    suite.addTest(RDSForm('test_rds_form', driver))
    suite.addTest(SQSForm('test_sqs_form', driver))
    suite.addTest(S3Form('test_s3_form', driver))
    suite.addTest(EC2Form('test_ec2_form', driver))
    suite.addTest(CacheForm('test_cache_form', driver))
    suite.addTest(GlueForm('test_glue_form', driver))
    return suite


if __name__ == "__main__":

    runner = HTMLTestRunner(output='Reports', combine_reports=True)
    runner.run(suite())
