from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement(object):
    def __init__(self, driver, value,by):
        self.driver = driver
        self.value = value
        self.by = by 
        self.locator = (self.by, self.value)

        self.web_element = None 
        self.find()
    
    def find(self):
        # this is brittle sophisticated way is to use wait
        #self.driver.find_element(by= self.by, value=self.locator)
        
        element = WebDriverWait(self.driver, 10).until(
            EC.visibilitiy_of_element_located(locator= self.locator)
        )
        # This populates the web element we make it find itself
        self.web_element = element 
        return None
    
    def click(self):
        element = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(locator=  self.locator)
        )
        element.click()
        return None
     
    def input_text(self, txt):
        self.web_element_send_keys(txt)
        return None 
    
    @property
    def text(self):
        text =  self.web_element.text
        return text