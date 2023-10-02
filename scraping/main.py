# En tu script principal (main.py o como desees llamarlo)
from controller.Selenium import SeleniumDriver
from controller.MercadoLibre import MercadoLibreScraper
from controller.ProcesadorDatos import DatosProcessor

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
procesador = DatosProcessor(datos)
procesador.formatear_valores()
procesador.guardar_en_excel("monitores.xlsx")

# Abre el archivo Excel
procesador.abrir_excel("monitores.xlsx")