from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from utils.TestWrapper import Test

import time


class VerbalMemory(Test):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.buttonDelay = 0.05

    def startTest(self):
        super().gotoTest("VerbalMemory")

        startButton = self.driverManager.waitForElement(
            By.XPATH, "//button[text()='Start']"
        )
        startButton.click()

        self.seenWords = []

    def getCurrentWord(self):
        word = self.driverManager.waitForElement(By.CLASS_NAME, "word").text
        return word

    def getButtons(self):
        seen = self.driverManager.getElementByText("button", "SEEN")
        new = self.driverManager.getElementByText("button", "NEW")

        return {"seen": seen, "new": new}

    def getScore(self):
        scoreText = self.driverManager.getElement(By.CLASS_NAME, "score").text
        score = scoreText.split("| ")[1]

        return int(score)

    def selectAnswer(self, word: str, fail: bool = False):
        buttons = self.getButtons()

        if fail:
            # flip the buttons
            buttons["seen"], buttons["new"] = buttons["new"], buttons["seen"]

        if word in self.seenWords:
            buttons["seen"].click()
        else:
            buttons["new"].click()

        self.seenWords.append(word)

    def runTest(self):
        self.startTest()

        while True:
            word = self.getCurrentWord()

            self.selectAnswer(word)

            time.sleep(self.buttonDelay)

            if self.getScore() == 300:
                # Fail the rest of the words
                while super().gameFinished() == False:
                    self.selectAnswer(word, fail=True)
                    time.sleep(self.buttonDelay)

            if super().gameFinished():
                break

        self.saveScore()
