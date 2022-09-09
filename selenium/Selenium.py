import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# edge = webdriver.Edge()
# edge.get("https://www.baidu.com")


class Tester(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(
            "https://dangjian.hxq.komect.com/hldjLogin/?activityId=1717&corpId=753063193924136960&homeUrl=http"
            "://dangjian.hxq.komect.com/dkdtweb/")

    def login(self, phone):
        self.driver.find_element(By.CLASS_NAME, "input-user-phone").clear()
        self.driver.find_element(By.CLASS_NAME, "input-user-phone").send_keys(phone)
        self.driver.find_element(By.CLASS_NAME, "get-code").click()
        code = input("输入验证码:")
        self.driver.find_element(By.ID, "loginCode").clear()
        self.driver.find_element(By.ID, "loginCode").send_keys(code)
        self.driver.find_element(By.CLASS_NAME, "login-btn").click()

    def play(self):
        self.driver.find_element(By.CLASS_NAME, "btn-begin").click()  # 开始
        time.sleep(5)

        for i in range(5):
            try:
                self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[11]/div[3]/div[3]/div/div')
                hasc = True
            except:
                hasc = False

            if hasc:
                self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[11]/div[3]/div[3]/div/div').click()
            else:
                self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[11]/div[3]/div[1]/div/div').click()
            time.sleep(5)

        # self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[11]/div[3]/div[1]/div/div').click()
        # self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[11]/div[3]/div[2]/div/div').click()
        # self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[11]/div[3]/div[3]/div/div').click()
        # self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[11]/div[3]/div[4]/div/div').click()

        # self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[8]')

        print(self.driver.find_element(By.CLASS_NAME, "result-got").text)
        self.driver.find_element(By.CLASS_NAME, "btn-continue").click()  # 继续挑战
        time.sleep(3)

        self.driver.get_cookies()

    def start_game(self, n):
        print("score: " + self.driver.find_element(By.CLASS_NAME, "value").text)
        self.driver.find_element(By.CLASS_NAME, "with-computer").click()

        for i in range(n):
            print(i)
            self.play()

    def __del__(self):
        self.driver.quit()


if __name__ == '__main__':
    instance = Tester()
    phone = "xx"
    instance.login(phone)
    instance.start_game(10)
