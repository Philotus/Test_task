from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

import time
from datetime import datetime
import random
import string


driver = webdriver.Chrome(ChromeDriverManager().install())
data = []
def config_reader():
    global login_text, password_text, workdir
    lines = ["","",""]
    i = 0
    with open("config.txt", "r") as file:
        for line in file:
            lines[i] = line
            i+= 1
    login_text = lines[0]
    password_text = lines[1]
    workdir = lines[2]

def print_in_file(Text):
    file_name = "Test_" + now_time + ".txt"
    full_file_loc = workdir + "/" + file_name
    with open(full_file_loc, mode='a', newline='') as file:
        for i in Text:
            file.write(i)

def generate_random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))



def signin_up(login_text,password_text):
    global new_login_text
    new_login_text = login_text
    driver.find_element(By.XPATH, '//*[@id="signin2"]').click()


    time.sleep(1)


    login = driver.find_element(By.XPATH, '//*[@id="sign-username"]')
    login.clear()
    login.send_keys(login_text)

    password = driver.find_element(By.XPATH, '//*[@id="sign-password"]')
    password.clear()
    password.send_keys(password_text)

    

    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/button[2]').click()


    time.sleep(2)


    alert = driver.switch_to.alert
    alert_text = alert.text
    time.sleep(1)
    if(alert_text == "Sign up successful."):
        alert_text+="\n"
        data.append(alert_text)
        alert.dismiss()
        time.sleep(1)
    if(alert_text == "This user already exist."):
        
        new_login_text = login_text + now.strftime("%d%m%y%H%M%S")
        alert.dismiss()
        
        time.sleep(1)

        driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/button[1]').click()

        time.sleep(1)

        signin_up(new_login_text,password_text)


def logining_in(login_text, password_text):
    driver.find_element(By.XPATH, '//*[@id="login2"]').click()


    time.sleep(1)


    login = driver.find_element(By.XPATH, '//*[@id="loginusername"]')
    login.clear()
    login.send_keys(login_text)

    password = driver.find_element(By.XPATH, '//*[@id="loginpassword"]')
    password.clear()
    password.send_keys(password_text)

    driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]').click()

    
    res = driver.find_element(By.XPATH, '//*[@id="nameofuser"]').text
    if(res == f"Welcome {login_text}"):
        data.append("Loged in successfuly\n")


def Buying():
    time.sleep(1)
    Check_list = [False, False, False]
    buttons = driver.find_elements(By.CLASS_NAME, 'list-group-item')
    buttons[2].click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[6]/div/div/h4/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a').click()
    time.sleep(1)

    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.dismiss()



    driver.find_element(By.XPATH, '//*[@id="cartur"]').click()
    time.sleep(1)
    if(driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/table/tbody/tr[1]/td[2]').text == "MacBook Pro" and int(driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/table/tbody/tr[1]/td[3]').text) == 1100):
        Check_list[0] = True
    if(len(driver.find_elements(By.CLASS_NAME, "success")) == 1):
        Check_list[1] = True
    if(int(driver.find_element(By.XPATH, '//*[@id="totalp"]').text) == 1100):
        Check_list[2] = True
    time.sleep(2)
    if(Check_list[0] == True and Check_list[1] == True and Check_list[2] == True):
        driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]/button').click()
    else:
        for i in Check_list:
            print (i)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="name"]').send_keys(generate_random_word(8))
    driver.find_element(By.XPATH, '//*[@id="country"]').send_keys(generate_random_word(8))
    driver.find_element(By.XPATH, '//*[@id="city"]').send_keys(generate_random_word(8))
    driver.find_element(By.XPATH, '//*[@id="card"]').send_keys(generate_random_word(8))
    driver.find_element(By.XPATH, '//*[@id="month"]').send_keys(generate_random_word(8))
    driver.find_element(By.XPATH, '//*[@id="year"]').send_keys(generate_random_word(8))
    time.sleep(1)

    driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]').click()
    time.sleep(1)
    driver.save_screenshot(f'{workdir}/Test'+ now_time + ".png")

    data.append(driver.find_element(By.XPATH, '/html/body/div[10]/p').text.splitlines()[0])


driver.get("https://www.demoblaze.com/index.html")
time.sleep(3)
now = datetime.now()
now_time = now.strftime("%d_%m_%y_%H_%M_%S")

config_reader()
signin_up(login_text,password_text)
new_login_text = new_login_text.replace('\n', '')
new_login_text += "\n"
data.append(new_login_text)
data.append(password_text)


logining_in(new_login_text,password_text)
Buying()
print_in_file(data)