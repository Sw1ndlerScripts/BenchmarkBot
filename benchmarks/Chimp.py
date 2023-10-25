from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from utils.TestWrapper import Test

import time


class Chimp(Test):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.buttonDelay = 0.1
        self.continueDelay = 0.1

    def buttonIsNumber(self, button: WebElement) -> bool:
        children = self.driverManager.getChildren(button)
        cellNumber = button.get_attribute("data-cellnumber")

        if len(children) == 0 or cellNumber != None:
            return True
        return False

    def getButtons(self) -> dict[int, WebElement]:
        numbersContainer = self.driverManager.waitForElement(
            By.CLASS_NAME, "desktop-only"
        )

        buttons = self.driverManager.getChildren(numbersContainer)
        buttons = filter(self.buttonIsNumber, buttons)

        numberedButtons = {}
        for button in buttons:
            cellNumber = button.get_attribute("data-cellnumber")

            if cellNumber != None:
                numberedButtons[int(cellNumber)] = button

        return numberedButtons

    def startTest(self):
        super().gotoTest("Chimp")

        startButton = self.driverManager.getElementByText("*", "Start Test")
        startButton.click()

    def pressButtons(self, buttons: dict[int, WebElement]):
        for i in range(1, len(buttons) + 1):
            buttons[i].click()
            time.sleep(self.buttonDelay)

    def getAmtNumbers(self):
        numbersText = self.driverManager.getElementByText("*", "NUMBERS")

        if numbersText == None:  # Game is finished
            return 41

        siblings = self.driverManager.getSiblings(numbersText)

        amtNumbers = siblings[1].text
        return int(amtNumbers)

    def runTest(self):
        self.startTest()

        while True:
            buttons = self.getButtons()
            self.pressButtons(buttons)

            time.sleep(self.continueDelay)

            if self.getAmtNumbers() == 41:
                break

            continueButton = self.driverManager.getElementByText("*", "Continue")
            continueButton.click()

            time.sleep(self.buttonDelay)

        self.saveScore()
