from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

driver.get("https://online.spor.istanbul/satiskiralik")

plaj_voleybol_listbox = driver.find_element("id","select2-ddlBransFiltre-result-9pr0-999c119c-2fd2-40ce-b0ef-0344c26f4c7f")
plaj_voleybol_listbox.click()
plaj_voleybol_listbox2 = driver.find_element("id","select2-ddlSalonFiltre-result-3ey2-e87a3b34-d250-4fce-b628-f94d91afb510")
plaj_voleybol_listbox2.click()
rezervasyon_button = driver.find_element("id","pageContent_rptList_rpChild_5_lbRezervasyon_14")
rezervasyon_button.click()
rezervasyon_button.send_keys(Keys.ENTER)
kiralık_checkbox = driver.find_element("id","pageContent_cboxKiralikSatisSozlesmesi")
kiralık_checkbox.click()
sepete_ekle_button = driver.find_element("id","pageContent_lbtnSepeteEkle")
sepete_ekle_button.click()

time.sleep(30)

    # Tarayıcıyı kapatın
driver.quit()
