from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



# Selenium WebDriver'ı başlatın (Chrome için örnek)
driver = webdriver.Chrome()
driver.maximize_window()


# Web sitesine gidin    
driver.get("https://online.spor.istanbul/uyegiris")


# Giriş yapın (örnek olarak, kullanıcı adı ve şifre doldurun)
username_input = driver.find_element("name","txtTCPasaport")
password_input = driver.find_element("name", "txtSifre")
username_input.send_keys("66148073320")
password_input.send_keys("45230681")
password_input.send_keys(Keys.ENTER)

# Web sitesine gidin
driver.get("https://online.spor.istanbul/satiskiralik")
time.sleep(3)


plaj_voleybol_button = driver.find_element("id","select2-ddlBransFiltre-container")
plaj_voleybol_button.click()
time.sleep(3)   
plaj_voleybol_listbox = driver.find_element(By.CSS_SELECTOR,"[id*='999c119c-2fd2-40ce-b0ef-0344c26f4c7f']")
print(plaj_voleybol_listbox)
plaj_voleybol_listbox.click()
time.sleep(3)
plaj_voleybol_button2 = driver.find_element("id","select2-ddlSalonFiltre-container")
plaj_voleybol_button2.click()
time.sleep(3)
plaj_voleybol_listbox2 = driver.find_element(By.CSS_SELECTOR,"[id*='e87a3b34-d250-4fce-b628-f94d91afb510']")
plaj_voleybol_listbox2.click()
time.sleep(3)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
rezervasyon_button = driver.find_element("id","pageContent_rptList_rpChild_5_dvCheckbox_13")
rezervasyon_button.click()
driver.switch_to.alert.accept()
time.sleep(3)
kiralık_checkbox = driver.find_element("id","pageContent_cboxKiralikSatisSozlesmesi")
kiralık_checkbox.click()
time.sleep(3)
sepete_ekle_button = driver.find_element("id","pageContent_lbtnSepeteEkle")
sepete_ekle_button.click()


     
time.sleep(10)

# Tarayıcıyı kapatın
driver.quit()
