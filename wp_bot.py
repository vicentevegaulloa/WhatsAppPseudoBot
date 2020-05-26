from selenium import webdriver
from params import ELEMENTS

class WhatsAppBot():

    """Functional WhatsApp pseudo Bot (Needs authentication with QR)."""

    def __init__(self):
        #Set driver.
        self.driver = webdriver.Chrome()
        #Set WhatsAppWeb
        self.driver.get('https://web.whatsapp.com/')
        while not self.is_auth():
            input("Make sure you´ve verified your QR, then press ENTER.")

    def is_auth(self):
        try:
            self.driver.find_element_by_class_name('landing-main')
            return False
        except:
            return True

    def send_msg(self, to, msg, count=1):
        user = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(to))
        user.click()
        msg_box = self.driver.find_element_by_xpath(ELEMENTS['msg_box'])
        for i in range(count):
            msg_box.send_keys(msg)
            button = self.driver.find_element_by_xpath(ELEMENTS['send_btn'])
            button.click()
        return
