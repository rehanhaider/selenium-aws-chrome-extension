## Run selenium and chrome driver to scrape data from cloudbytes.dev
import time
import json
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
#from pyvirtualdisplay import Display


def handler(event=None, context=None):
    #display = Display(visible=False, extra_args=[':25'], size=(2560, 1440), backend="xvfb") 
    #display.start()
    print('Started Display')

    #import pyautogui
    chrome_options = Options()
    chrome_options.binary_location = "/opt/chrome/chrome"
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-tools")
    #chrome_options.add_argument("--no-zygote")
    #chrome_options.add_argument("--single-process")
    chrome_options.add_argument("window-size=2560x1440")
    chrome_options.add_argument("--user-data-dir=/tmp/chrome-user-data")
    chrome_options.add_argument("--remote-debugging-port=9222")
    #chrome_options.add_argument("--data-path=/tmp/chrome-user-data")
    #chrome_options.add_argument("--disk-cache-dir=/tmp/chrome-user-data")
    chrome_options.add_extension("/opt/GoFullPage.crx")
    download_directory = {"download.default_directory": "/tmp/"}
    chrome_options.add_experimental_option("prefs", download_directory)
    browser = webdriver.Chrome("/opt/chromedriver", options=chrome_options)
    
    # Open Extension options
    print("Open Extension options...")
    browser.switch_to.window(browser.window_handles[1])
    browser.get("chrome-extension://fdpohaocaechififmbbbbbknoalclacl/options.html")

    # Provide Download Permission
    print("Provide Download Permission...")
    browser.find_element(By.ID, "perm-toggle").click()
    browser.find_element(By.NAME, "downloads").click()
    browser.switch_to.active_element
    time.sleep(1)
    #pyautogui.press("tab")
    time.sleep(1)
    #pyautogui.press("enter")

    # Close options
    print("Close options...")
    print(len(browser.window_handles)) #Expected 2
    browser.close()
    print(len(browser.window_handles)) #Expected 1
    time.sleep(1)
    # Take screenshot
    print("Take screenshot...")
    browser.switch_to.window(browser.window_handles[0])
    #pyautogui.hotkey("shift", "alt", "p")
    time.sleep(5)
    print(len(browser.window_handles)) #Expected 2
    #browser.switch_to.window(browser.window_handles[1])
    #time.sleep(1)
    #browser.find_element(By.ID, "btn-download").click()

    time.sleep(5)
    browser.quit()

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "success",
            }
        ),
    }
