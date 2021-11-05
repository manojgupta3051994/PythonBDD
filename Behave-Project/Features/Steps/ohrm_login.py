from behave import *
from selenium import webdriver

@given('Launch new Chrome Browser')
def LaunchBrowser(context):
    context.driver = webdriver.Chrome(executable_path=r'C:\Users\Manoj\Desktop\Python - Selenium Practice\Drivers\chromedriver.exe')
    

@when('Open an Orange hrm homepage')
def OpenHomePage(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')


@when('Enter username "{username}" and password "{password}"')
def EnterCreds(context,username,password):
    context.driver.find_element_by_id('txtUsername').send_keys(username)
    context.driver.find_element_by_id('txtPassword').send_keys(password)


@when('Click on Login Button')
def ClickLogin(context):
    context.driver.find_element_by_id('btnLogin').click()
    

@then('User is successfully logged in')
def LoggedIn(context):
    try:
        text = context.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/h1').text
    except:
        context.driver.close()
        assert False
    if text == "Dashboard":
        assert True
        context.driver.close()

        