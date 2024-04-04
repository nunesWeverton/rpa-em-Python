from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

from time import sleep

# Instala o ChromeDriver e cria um serviço
service = Service(ChromeDriverManager().install())

# Inicializa o navegador Chrome, passando o serviço
navegador = webdriver.Chrome(service=service)

# url inicial da amazon
navegador.get("https://www.amazon.com.br/?&tag=hydrbrabk-20&ref=pd_sl_7rwd1q78df_e&adgrpid=155790195778&hvpone=&hvptwo=&hvadid=677606588104&hvpos=&hvnetw=g&hvrand=9648656520974425255&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9074209&hvtargid=kwd-10573980&hydadcr=26346_11691057&gad_source=1")
sleep(2)

search = navegador.find_element(By.ID, "twotabsearchtextbox")
search.click()
search.send_keys("notebook") #pesquisa pelos notebook na area de pesquisa 
search.send_keys(Keys.RETURN) # pressiona a tecla enter para realizar a pesquisa.

sleep(5)

try:
    iconeDepartamento = navegador.find_element(By.XPATH, '//*[@id="priceRefinements"]/div[2]/a/i')
    lista_itens_visivel = iconeDepartamento.get_attribute("class") == "a-icon a-icon-section-expand"

    if lista_itens_visivel:
        print("O ícone está visível. Clicando no departamento...")
        departamento = navegador.find_element(By.XPATH, '//*[@id="n-title"]/span')
        departamento.click()
    else:
        print("O ícone não está visível.")
except NoSuchElementException:
    print("O ícone não foi encontrado. Não é possível clicar no departamento.")

sleep(2)

notebook = navegador.find_element(By.XPATH, '//*[@id="n/16364755011"]/span/a/span')
notebook.click()

sleep(2)

try:
    iconeOferta = navegador.find_element(By.XPATH, '//*[@id="priceRefinements"]/div[2]/a/i')
    listaItensVisivelOferta = iconeOferta.get_attribute("class") == "a-icon a-icon-section-expand"

    if listaItensVisivelOferta:
        print("O ícone está visível. Clicando no departamento...")
        ofertaEDesconto = navegador.find_element(By.XPATH, '//*[@id="p_n_deal_type-title"]/span')
        ofertaEDesconto.click()
    else:
        print("O ícone não está visível.")
        
except:
    print("O ícone não foi encontrado. Não é possível clicar no oferta e desconto.")

#ofertaEDesconto = navegador.find_element(By.XPATH, '//*[@id="p_n_deal_type-title"]/span')
##ofertaEDesconto.click()

ofertaDoDia = navegador.find_element(By.XPATH, '//*[@id="p_n_deal_type/23565492011"]/span/a/span')
ofertaDoDia.click()

sleep(5)

listaDeNotebook = navegador.find_element(By.XPATH, '//*[@id="search"]/div[1]')
notebookOferta =  listaDeNotebook.find_elements(By.CLASS_NAME, 'sg-col-inner')
notebook = {}

for item in notebookOferta:
    try:
        nomeNotebook = item.find_element(By.CSS_SELECTOR, '.a-section.a-spacing-small.puis-padding-left-small.puis-padding-right-small')
        print(nomeNotebook.text,'\n') 
    except NoSuchElementException:
        print("Elemento span não encontrado no item.")

sleep(400)
