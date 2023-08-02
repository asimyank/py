from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Selenium WebDriver'ı başlatın (Chrome için örnek)
driver = webdriver.Chrome()

# Web sitesine gidin
    
driver.get("https://online.spor.istanbul/uyegiris")

# Giriş yapın (örnek olarak, kullanıcı adı ve şifre doldurun)
username_input = driver.find_element("name","txtTCPasaport")
password_input = driver.find_element("name", "txtSifre")
username_input.send_keys("66148073320")
password_input.send_keys("45230681")
password_input.send_keys(Keys.ENTER)

driver.get("https://online.spor.istanbul/uyespor")


seans_sec_button = driver.find_element("id","pageContent_rptListe_lbtnSeansSecim_0")
seans_sec_button.click()

driver.get("https://online.spor.istanbul/uyeseanssecim")

seans_sec_checkbox = driver.find_element("id","pageContent_rptList_ChildRepeater_4_cboxSeans_1")
seans_sec_checkbox.click()
rezervasyon_onay_checkbox = driver.find_element("id","pageContent_cboxOnay")
rezervasyon_onay_checkbox.click()
recaptcha_checkbox = driver.find_element("class","recaptcha-checkbox-border")
recaptcha_checkbox.click()
for _ in range(30):
    element = driver.find_element("By",CLASS_NAME, "g-recaptcha")

    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    time.sleep(0.1)

    element.click()
  
kaydet_button = driver.find_element("id","lbtnKaydet")
kaydet_button.click()


    # Beklemek için bir süre verin (sayfanın yüklenmesi için)
time.sleep(30)

    # Tarayıcıyı kapatın
driver.quit()
