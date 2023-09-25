from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

from time import sleep
# PATH = "C:\DRIVER\geckodriver.exe"
driver = webdriver.Firefox()

driver.get("https://www.mercadolibre.com.co/")
print(driver.title)
elem = driver.find_element(By.CLASS_NAME, "nav-search-input")
elem.clear()
elem.send_keys("monitor")
elem.send_keys(Keys.ENTER)
sleep(1)

esperarBusqueda = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/section/ol')))

# laVariableQueValidaPresencia = driver.find_element(By.XPATH, "")
# contenidoHTMLDeLaVariable = laVariableQueValidaPresencia.get_attribute('outerHTML')
# HTMLParseado = BeautifulSoup(contenidoHTMLDeLaVariable, 'html.parser')

contenidoBase = driver.find_element(By.XPATH, '/html/body/main/div/div[2]/section/ol')
contenidoHTML = contenidoBase.get_attribute('outerHTML')
htmlConvertido = BeautifulSoup(contenidoHTML, 'html.parser')
print(htmlConvertido)

print("Lo encontró")

driver.close()