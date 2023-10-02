from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
from os import system

# Inicializar el navegador web
driver = webdriver.Firefox()
driver.get("https://www.mercadolibre.com.co/")

# Realizar la búsqueda de monitores
search_box = driver.find_element(By.CLASS_NAME, "nav-search-input")
search_box.clear()
search_box.send_keys("monitor")
search_box.send_keys(Keys.ENTER)

# Esperar a que se carguen los resultados de búsqueda
esperarBusqueda = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/section/ol')))

# Obtener el contenido HTML de los resultados de búsqueda
contenidoBase = driver.find_element(By.XPATH, '/html/body/main/div/div[2]/section/ol')
contenidoHTML = contenidoBase.get_attribute('outerHTML')

# Parsear el contenido HTML con BeautifulSoup
soup = BeautifulSoup(contenidoHTML, 'html.parser')

# Crear una lista para almacenar los datos de los monitores
monitores = []

# Iterar a través de los elementos de resultados y extraer la información
resultados = soup.find_all("div", class_="ui-search-result__content-wrapper")

for resultado in resultados:
    nombre = resultado.find("h2", class_="ui-search-item__title").text.strip()
    precio_element = resultado.find("div", class_="ui-search-price")
    precio = precio_element.find("span", class_="andes-money-amount__fraction").text.strip() if precio_element else "No disponible"
    cuotas_element = resultado.find("span", class_="ui-search-item__group__element shops__items-group-details ui-search-installments ui-search-color--BLACK")
    cuotas = cuotas_element.text.strip().replace("en", "").replace("x", "x $").replace("pesos", "") if cuotas_element else "No disponible"
    cuotas_interes = resultado.find("span", class_="ui-search-item__group__element shops__items-group-details ui-search-installments ui-search-color--LIGHT_GREEN")
    cuotas_sin_interes = cuotas_interes.text.strip().replace("en", "").replace("x", "x $").replace("pesos", "").replace("sin interés", " sin interés") if cuotas_interes else "No disponible"
    puntuacion_element = resultado.find("span", class_="ui-search-reviews__rating-number")
    puntuacion = puntuacion_element.text.strip() if puntuacion_element else "Sin puntuación"
    
    # Agregar los datos del monitor a la lista
    monitor = {
        "Nombre": nombre,
        "Precio": precio,
        "Cuotas": cuotas,
        "Cuotas sin interes" : cuotas_sin_interes,
        "Puntuación": puntuacion
    }
    
    monitores.append(monitor)

# Cerrar el navegador
driver.quit()

# Formatear los valores de las cuotas y cuotas sin interés
for monitor in monitores:
    for key,value in monitor.items():
        if (key == "Cuotas" or key == "Cuotas sin interes") and value == "No disponible":
            pass
        elif key == "Cuotas":
            valorLista = value.split("$")
            value = f"{valorLista[0]}${valorLista[-1]}"
            monitor[key] = value
        elif key == "Cuotas sin interes":
            valorLista = value.split("$")
            value = f"{valorLista[0]}${valorLista[-1]}"
            monitor[key] = value

# Imprimir la lista de monitores
for monitor in monitores:
    print(monitor)

# Crear un DataFrame y guardar en un archivo Excel
df = pd.DataFrame(monitores)
df.to_excel("monitores.xlsx", sheet_name="Monitores")


# Abrir el archivo Excel
system('monitores.xlsx')