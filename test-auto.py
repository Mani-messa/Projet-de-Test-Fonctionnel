from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time

edgedriver_path = r"D:\Driver\edgedriver.exe"
log_file = "log/log.txt"
driver = webdriver.Chrome()


driver.get('http://localhost/projet-test-auto/Projet-de-Test-Fonctionnel/index.html')
time.sleep(2)

with open(log_file, 'w', encoding = "UTF-8") as file:
    file.write("")
jeuDeTest = [
    ["admin", 123456],
    ["admin", "motdepasse"],
    ["username", 123456],
    ["username", "motdepasse"], 
    ["", ""]
]

for test in jeuDeTest :

    try:
        driver.find_element(By.ID, "username").send_keys(test[0])
        driver.find_element(By.ID, "password").send_keys(test[1])
        driver.find_element(By.CLASS_NAME, "btn.btn-login").click()
        time.sleep(2)

        driver.get(url = 'http://localhost/projet-test-auto/Projet-de-Test-Fonctionnel/index.html')
        time.sleep(2)

        with open(log_file, 'a', encoding = "UTF-8") as file:
            file.write(f'Test avec {test[0]} effectué à {time.ctime()} - Succès: test validé \n')

    except Exception as e:
        with open(log_file, 'a', encoding = "UTF-8") as file:
            file.write(f'Erreur lors du test avec {test[0]} à {time.ctime()} : test erreur\n')