from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class InternetTwitterSpeedBot():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(2)
        self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        self.driver.find_element(By.CLASS_NAME, "js-start-test").click()
        sleep(100)
        try:
            self.down = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
            self.up = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)
        except NoSuchElementException:
            self.driver.find_element(By.CLASS_NAME, "close-btn").click()
            self.down = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
            self.up = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)
        finally:
            print(f"Down: {self.down}")
            print(f"Up: {self.up}")

    def tweet_at_provider(self, email, password, promised_down, promised_up, provider):
        self.driver.get("https://twitter.com/")
        sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]').click()
        sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/'
                                           'div/div[3]/div[5]/a').click()
        sleep(7)
        email_input = self.driver.find_element(By.NAME, "text")
        email_input.send_keys(email)
        sleep(3)
        self.driver.find_element(By.XPATH, "//div[@role='button'][contains(.,'Ďalej')]").click()
        sleep(5)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        sleep(2)
        self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        sleep(5)
        tweet_input = self.driver.find_element(By.CLASS_NAME, "public-DraftEditor-content")
        tweet_input.send_keys(f"Hey {provider}, why is my internet speed {self.down}down/{self.up}up,"
                              f" when I pay for {promised_down}down/{promised_up}up?")
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "div[data-testid='tweetButtonInline'][role='button']").click()
