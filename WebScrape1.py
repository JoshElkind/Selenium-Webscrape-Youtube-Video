from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
import ast



PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)
actions = ActionChains(driver)
songinplaylist = "fat rat mix 222"

driver.get("https://youtube.com")
search = driver.find_element_by_name("search_query")
search.send_keys(songinplaylist)
search.send_keys(Keys.RETURN)
time.sleep(2)
search1 = driver.find_element_by_id("video-title")
search1.click()
time.sleep(1)
adcheck = driver.find_elements_by_class_name("ytp-ad-text")
print (adcheck)
adcheck1 = 1
if adcheck1 > 0:
    print ("there is an ad")
    all_ad_class = driver.find_element_by_class_name("ytp-settings-button")
    actions.context_click(all_ad_class).perform()
    menurightclick = driver.find_element_by_class_name('ytp-menuitem-label')
    click_on = driver.find_element_by_xpath("//*[contains(text(), 'Copy debug info')]")
    click_on.click()
    debugclickboard = pyperclip.paste()
    fixedboardonlytrue = debugclickboard.replace("true", "True")
    fixedboardfinal = fixedboardonlytrue.replace("false", "False")
    ad_info_dict = ast.literal_eval(fixedboardfinal)
    print (ad_info_dict)
    

else:
    print ("no ad")



'''time.sleep(10)
driver.close()'''


{
  
}