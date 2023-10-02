from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

class MercadoLibreScraper:
    def __init__(self, driver):
        self.driver = driver
    
    def buscar_productos(self, keyword):
        self.driver.get("https://www.mercadolibre.com.co/")
        search_box = self.driver.find_element(By.CLASS_NAME, "nav-search-input")
        search_box.clear()
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.ENTER)
    
    def esperar_resultados(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/section/ol')))
    
    def obtener_resultados_html(self):
        contenidoBase = self.driver.find_element(By.XPATH, '/html/body/main/div/div[2]/section/ol')
        contenidoHTML = contenidoBase.get_attribute('outerHTML')
        return contenidoHTML
    
    def parsear_resultados(self, contenidoHTML):
        soup = BeautifulSoup(contenidoHTML, 'html.parser')
        resultados = soup.find_all("div", class_="ui-search-result__content-wrapper")

        # Lista para almacenar los datos de los monitores
        monitores = []

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
                "Cuotas sin interes": cuotas_sin_interes,
                "Puntuación": puntuacion
            }

            monitores.append(monitor)

        return monitores  # Devuelve la lista de monitores