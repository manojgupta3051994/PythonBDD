from behave import *
from selenium import webdriver

@given('Launch Chrome Browser')
def LaunchBrowser(context):
    context.driver = webdriver.Chrome(executable_path=r'C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe')
    

@when('Open Orange hrm homepage')
def OpenHomePage(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')
    

@then('Verify that the logo is present on page')
def VerifyLogo(context):
    status = context.driver.find_element_by_xpath("//*[@id='divLogo']/img").is_displayed()
    assert status is True


@then('Close Browser')
def CloseBrowser(context):
    context.driver.close()
    