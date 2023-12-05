from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time

edgedriver_path = r"D:\Driver\edgedriver.exe"

driver = webdriver.Chrome()

# log_file = "log/log1.txt"
driver.get("http://localhost/projet-test-auto/Projet-de-Test-Fonctionnel/admin.html")
time.sleep(2)

driver.find_element(By.ID, "link-dashboard").click()

driver.find_element(By.ID, "link-users").click()

driver.find_element(By.CLASS_NAME, "btn.btn-success").click()

driver.find_element(By.ID, "username").send_keys("Amalia-mess")

driver.find_element(By.ID, "email").send_keys("amalia.mess@gmail.com")

driver.find_element(By.ID, "password").send_keys(96637441)

driver.find_element(By.CLASS_NAME, "btn.btn-primary").click()

driver.find_element(By.ID, "link-settings").click()

# driver.execute_script("document.getElementByClasseName('setting-item').click()")
selectcolor=Select(driver.find_element(By.ID , "theme-selector"))
selectcolor.select_by_visible_text("Sombre")
time.sleep(2)
selectcolor.select_by_visible_text("Clair")

selectpolice=Select(driver.find_element(By.ID, "font-size-selector"))
selectpolice.select_by_visible_text("Petite")
time.sleep(2)
selectpolice.select_by_visible_text("Moyenne")
time.sleep(2)
selectpolice.select_by_visible_text("Grande")
time.sleep(2)


selectcarte=Select(driver.find_element(By.ID, "border-style-selector"))
selectcarte.select_by_visible_text("Arrondi")
time.sleep(2)
selectcarte.select_by_visible_text("Carré")

driver.find_element(By.ID, "link-analytics").click()

driver.find_element(By.ID, "link-support").click()

# driver.find_element(By.ID, "link-support").click()

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-success"))
)
element.click()
time.sleep(2)

driver.find_element(By.ID, "title").send_keys("Problème de connexion")
driver.find_element(By.ID, "description").send_keys("Impossible de se connecter")
time.sleep(2)

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-primary"))
)
element.click()
time.sleep(2)

button_element = driver.find_element(By.CSS_SELECTOR, "nav.admin-nav a[href= 'index.html']")
button_element.click()
time.sleep(5)