import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from utils.DriverManager import DriverManager
from utils.TestWrapper import Test

from benchmarks.ReactionTime import ReactionTime
from benchmarks.Typing import Typing
from benchmarks.Sequence import Sequence
from benchmarks.Chimp import Chimp
from benchmarks.Aim import Aim
from benchmarks.VerbalMemory import VerbalMemory

# Constants

USE_ADBLOCK = False
ADBLOCK_PATH = "uBlock-Origin.crx" # Not included in repo

# Variables

service = Service()
options = webdriver.ChromeOptions()

options.add_argument("start-maximized")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

if USE_ADBLOCK:
    options.add_extension(ADBLOCK_PATH)

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
