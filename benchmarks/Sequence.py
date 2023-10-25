from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from utils.TestWrapper import Test

import time


class Sequence(Test):  # Unfinished
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def startTest(self):
        super().gotoTest("Sequence")

        startButton = self.driverManager.waitForElement(
            By.XPATH, "//button[text()='Start']"
        )
        startButton.click()

        squaresContainer = self.driverManager.waitForElement(By.CLASS_NAME, "squares")

        children = self.driverManager.getChildren(squaresContainer)
        children = [
            child for child in children if child.get_attribute("class") == "square"
        ]

        self.squares = children

    def getLevel(self):
        levelText = self.driverManager.waitForElement(
            By.XPATH, "//span[text()='Level:']"
        )

        parent = self.driverManager.getParent(levelText)
        level = parent.find_element(By.XPATH, "./span[2]")

        return int(level.text)

    def sequenceFinished(self):
        for i, square in enumerate(self.squares):
            classes = square.get_attribute("class")
            if "active" in classes:
                return i
        return None

    def getSequence(self) -> list:
        sequence = []
        for i, square in enumerate(self.squares):
            classes = square.get_attribute("class")

            if "active" in classes:
                sequence.append(i)

                while "active" in square.get_attribute("class"):
                    pass

        return sequence

    def playSequence(self, sequence):
        for i in sequence:
            self.squares[i].click()
            time.sleep(1.5)

    def runTest(self):
        self.startTest()
        time.sleep(1)

        while True:
            # while True:
            #     firstSquare = self.sequenceFinished()

            #     if firstSquare != None:
            #         break

            #     pass

            level = self.getLevel()

            # time.sleep(0.5)

            sequence = self.getSequence()
            # sequence.insert(0, firstSquare)

            print(sequence)

            print("Started Playing")
            self.playSequence(sequence)

            while level == self.getLevel():
                pass

            print("Next Level")

            time.sleep(0.25)
