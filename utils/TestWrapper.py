from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from utils.DriverManager import GetDriverManager


TestUrls = {
    "ReactionTime": "https://humanbenchmark.com/tests/reactiontime",
    "Typing": "https://humanbenchmark.com/tests/typing",
    "Sequence": "https://humanbenchmark.com/tests/sequence",
    "Chimp": "https://humanbenchmark.com/tests/chimp",
    "Aim": "https://humanbenchmark.com/tests/aim",
    "VerbalMemory": "https://humanbenchmark.com/tests/verbal-memory",
}


class Test:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driverManager = GetDriverManager(driver)

    def gotoTest(self, test):
        self.driver.get(TestUrls[test])

    def gameFinished(self):
        scoreScreen = self.driverManager.getElement(By.CLASS_NAME, "view-score")
        if scoreScreen != None:
            return True

        saveScore = self.driverManager.getElementByText("button", "Save score")
        if saveScore != None:
            return True

        return False

    def saveScore(self):
        saveScore = self.driverManager.waitForElementByText("button", "Save score")
        saveScore.click()
