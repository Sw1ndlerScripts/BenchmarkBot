from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from utils.TestWrapper import Test


class Typing(Test):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def startTest(self):
        super().gotoTest("Typing")

        self.lettersContainer = self.driverManager.waitForElement(
            By.CLASS_NAME, "letters"
        )

    def runTest(self):
        self.startTest()

        letters = self.getLetters()
        self.lettersContainer.send_keys(letters)

        self.saveScore()

    def getLetters(self):
        letterElements = self.driverManager.getChildren(self.lettersContainer)

        letters = []
        for letterElement in letterElements:
            letter = letterElement.text

            if letter == "":
                letters.append(" ")
            else:
                letters.append(letter)

        return "".join(letters)
