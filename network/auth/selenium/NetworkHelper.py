import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.options import Options

if __name__ == '__main__':
    f = open("network.ticket.ini", "r")
    url = f.readline().strip()
    username = f.readline().strip()
    passwd = f.readline().strip()
    f.close()

    opt = Options()
    opt.ignore_zoom_level = True
    driver = webdriver.Ie(options=opt)
    driver.get(url)

    js = "expandCollapse('infoBlockID', true);"
    driver.execute_script(js)

    driver.find_element(By.ID, "overridelink").click()
    driver.find_element(By.ID, "password_name").send_keys(username)
    driver.find_element(By.ID, "password_pwd").send_keys(passwd)
    driver.find_element(By.ID, "password_submitBtn").click()

    time.sleep(2)
    driver.quit()

