# En tu script principal (main.py o como desees llamarlo)
from Selenium import SeleniumDriver
from MercadoLibre import MercadoLibreScraper
from ProcesadorDatos import DatosProcessor

# Inicializa el controlador Selenium
driver = SeleniumDriver().get_driver()

# Realiza la búsqueda y obtiene los datos
scraper = MercadoLibreScraper(driver)
scraper.buscar_productos("monitor")
scraper.esperar_resultados()
contenidoHTML = scraper.obtener_resultados_html()
datos = scraper.parsear_resultados(contenidoHTML)

# Cierra el navegador
driver.quit()

# Procesa los datos y los guarda en un archivo Excel
processor = DatosProcessor(datos)
processor.formatear_valores()
processor.guardar_en_excel("monitores.xlsx")

# Abre el archivo Excel
processor.abrir_excel("monitores.xlsx")
