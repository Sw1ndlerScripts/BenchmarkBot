from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from utils.TestWrapper import Test


class ReactionTime(Test):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def startTest(self):
        super().gotoTest("ReactionTime")  # Navigate to the url

        reactionBox = self.driverManager.waitForElement(By.CLASS_NAME, "view-splash")
        reactionBox.click()

        self.reactionBox = reactionBox

    def runTest(self):
        self.startTest()

        while True:
            self.clickForGreen()

            if super().gameFinished():
                break

            self.clickOnResult()

        self.saveScore()

    def clickForGreen(self):
        colorDiv = self.driverManager.waitForElementClass(self.reactionBox, "view-go")
        colorDiv.click()

    def clickOnResult(self):
        continueButton = self.driverManager.waitForElementClass(
            self.reactionBox, "view-result"
        )
        continueButton.click()
