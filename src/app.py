import time
import glob
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
#from pyvirtualdisplay.smartdisplay import SmartDisplay



def handler(event=None, context=None):
    display = Display(visible=False, extra_args=[':25'], size=(2560, 1440), backend="xvfb") 
    display.start()
    print('Started Display')
    #Pyautogui requires os.environ["Display"] variable to be set. 
    import pyautogui

    chrome_options = Options()
    # Headless environment starts without browser UI so no extensions
    #chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-tools")
    #chrome_options.add_argument("--no-zygote") #This will not load the extension
    #chrome_options.add_argument("--single-process") #Single process will break the app
    chrome_options.add_argument("window-size=2560x1440")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument("--user-data-dir=/tmp/chrome-user-data")
    chrome_options.add_extension("/opt/GoFullPage.crx")
    download_directory = {"download.default_directory": "/tmp/"}
    chrome_options.add_experimental_option("prefs", download_directory)
    webdriver_service = Service("/opt/chromedriver/stable/chromedriver")
    browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    browser.get("https://example.com")
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
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("enter")

    # Close options
    print("Close options...")
    print(len(browser.window_handles)) #Expected 2
    browser.close()
    print(len(browser.window_handles)) #Expected 1
    time.sleep(1)
    # Take screenshot
    print("Take screenshot...")
    browser.switch_to.window(browser.window_handles[0])
    pyautogui.hotkey("shift", "alt", "p")
    time.sleep(5)
    print(len(browser.window_handles)) #Expected 2
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(1)
    browser.find_element(By.ID, "btn-download").click()


    time.sleep(5)
    browser.quit()

    # importing earlier conflicts with selenium actions
    import boto3
    s3 = boto3.client("s3")
    BUCKET_NAME = "cloudbytes.dev"

    for image in glob.iglob("/tmp/*.png"): 
        s3.upload_file(image, BUCKET_NAME, os.path.basename(image))

    return {"status":"success"}
