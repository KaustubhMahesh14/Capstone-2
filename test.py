from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(r"C:\Users\kaust\Downloads\chromedriver_win32\chromedriver.exe",chrome_options =chrome_options)

driver.get("http://localhost:5000/")

driver.find_element("id","photo").click()

s = driver.find_element("id","inputGroupFile04")
s.send_keys(r"C:\kaustub.jpeg")

driver.find_element("id","inputGroupFileAddon04").click()
# s.click()

