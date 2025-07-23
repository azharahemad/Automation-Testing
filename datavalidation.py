from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.maximize_window()
driver.implicitly_wait(5)

def Login(driver, username, password):
    user_field = driver.find_element(By.XPATH,"//input[@placeholder='Username']")
    passw_field = driver.find_element(By.XPATH,"//input[@placeholder='Password']")

    user_field.clear()
    user_field.send_keys(username)

    passw_field.clear()
    passw_field.send_keys(password)

    driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

def Logout(driver):
    driver.find_element(By.XPATH,"//li[@class='oxd-userdropdown']").click()
    driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()


credentials = [('iqefoe', 'ifqewjf3023'),
               ('qfopqjfpq', 'f295u30^'),
               ('oorowrjf', '774^^$*'),
               ('Admin', 'admin123'),
               ('woORJPuuif','0042&*HG)'),
               ('Fcash&gdhf','f(#)(ajjJJSJ834)')]

Pass = 0
Fail = 0

for user, password in credentials:
    Login(driver, user, password)

    if driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index":
        time.sleep(3)
        print(f'Login Passed with Correct Credentials. Username: {user}, Password: {password}')
        Pass += 1
        Logout(driver)
    else:
        print(f'Login Failed with Incorrect Credentials. Username: {user}, Password: {password}')
        Fail += 1
    
    time.sleep(1)

print(f"Passed Cases: {Pass}")
print(f"Failed Cases: {Fail}")

driver.close()
