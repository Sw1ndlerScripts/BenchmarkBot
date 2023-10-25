from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from utils.TestWrapper import Test


class Aim(Test):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def getTarget(self) -> WebElement:
        # children = self.driverManager.getChildren(self.container)
        # for child in children:
        #     aimTarget = child.get_attribute("data-aim-target")
        #     if aimTarget != None:
        #         return child
        # return None

        # Quickest way to get the target
        return self.driverManager.getElement(
            By.XPATH, "/html/body/div/div/div[4]/div[1]/div/div[1]/div/div/div"
        )

    def getTargetBody(self, target: WebElement) -> WebElement:
        """
        Target has 0 size, so this is a workaround to get the body of the target
        """

        children = self.driverManager.getChildren(target)
        return children[0]

    def startTest(self):
        super().gotoTest("Aim")

        container = self.driverManager.waitForElement(By.CLASS_NAME, "desktop-only")
        self.container = container

    def runTest(self):
        self.startTest()

        while super().gameFinished() == False:
            target = self.getTarget()
            targetBody = self.getTargetBody(target)

            self.driverManager.absoluteClick(targetBody)

        self.saveScore()
