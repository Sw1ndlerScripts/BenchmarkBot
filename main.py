import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains

from utils.DriverManager import DriverManager
from utils.TestWrapper import Test

from benchmarks.ReactionTime import ReactionTime
from benchmarks.Typing import Typing
from benchmarks.Sequence import Sequence
from benchmarks.Chimp import Chimp
from benchmarks.Aim import Aim
from benchmarks.VerbalMemory import VerbalMemory

# Constants

USE_ADBLOCK = True

# Variables

service = Service()
options = webdriver.ChromeOptions()

options.add_argument("start-maximized")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

if USE_ADBLOCK:
    options.add_extension("uBlock-Origin.crx")

driver = webdriver.Chrome(service=service, options=options)

driverManager = DriverManager(driver)

# Main

reactionTime = ReactionTime(driver)
reactionTime.runTest()

typing = Typing(driver)
typing.runTest()

# sequence = Sequence(driver, driverManager)
# sequence.runTest()

chimp = Chimp(driver)
chimp.runTest()

aim = Aim(driver)
aim.runTest()

verbalMemory = VerbalMemory(driver)
verbalMemory.runTest()

print("Finished")

time.sleep(100000)
