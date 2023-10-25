from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains

class DriverManager:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.actionChains = ActionChains(driver, duration=0)

    def getElementByText(self, type: str, text: str) -> WebElement:
        return self.getElement(By.XPATH, f"//{type}[text()='{text}']")

    def getElement(self, by: By, value: str) -> WebElement:
        try:
            return self.driver.find_element(by, value)
        except NoSuchElementException:
            return None

    def waitForElement(self, by: By, value: str) -> WebElement:
        element = None
        while element == None:
            element = self.getElement(by, value)
        return element
    
    def waitForElementByText(self, type: str, text: str) -> WebElement:
        element = None
        while element == None:
            element = self.getElementByText(type, text)
        return element

    def waitForElementClass(self, element: WebElement, value: str) -> WebElement:
        while True:
            classes = element.get_attribute("class")
            if value in classes:
                return element

    def getChildren(self, element: WebElement) -> list[WebElement]:
        return element.find_elements(By.XPATH, ".//*")

    def getParent(self, element: WebDriver) -> WebElement:
        return element.find_element(By.XPATH, "./..")

    def getSiblings(self, element: WebElement) -> list[WebElement]:
        parent = self.getParent(element)
        return self.getChildren(parent)
    
    def absoluteClick(self, element: WebElement) -> None:
        """
        Clicks an element using action chains, bypassing the need for the element to be in view or clickable
        """

        self.actionChains.move_to_element(element).click().perform()

driverManager = None
def GetDriverManager(driver: WebDriver) -> DriverManager:
    global driverManager

    if driverManager == None:
        driverManager = DriverManager(driver)
        
    return driverManager